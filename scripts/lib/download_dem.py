# Name:     Download DEM
#
# Purpose:  Identify all the NED 10m DEM rasters that intersect with a HUC8
#           boundary polygon. Download and unzip all the rasters then mosaic
#           them into a single compressed GeoTIF raster possessing a specific
#           spatial reference.
#
# Author:   Philip Bailey
#
# Date:     15 Jun 2019
#
# -------------------------------------------------------------------------------
import argparse
import statistics
import sys
import os
import traceback
import gdal
import geojson
import gdal
import math
import rasterio
from lib.util import ProgressBar
from shapely.geometry import shape
from lib.raster import Geotransform
from lib.download import download_unzip
from lib.science_base import get_dem_urls
from lib.loghelper import Logger

# NED data sometimes has small discrepencies in its cell widths. For this reason we need a tolerance,
# below which value we just treat everything as if its fine. This way we don't need to resample which can
# lead to stitching errors in gdal warp using VRT
# Same-ish values are usually different by 1e-9 and different-ish values are usually different by 9e-6
# So this should be somewhere in between. any more
CELL_SIZE_THRESH_STDDEV = 1e-13
# Also we need a number cell width difference. Above this difference we don't even bother and throw an exception
CELL_SIZE_MAX_STDDEV = 1e-8


def download_dem(vector_path, epsg, buffer_dist, download_folder, unzip_folder, force_download=False):
    """
    Identify rasters within HUC8, download them and mosaic into single GeoTIF
    :param vector_path: Path to bounding polygon ShapeFile
    :param epsg: Output spatial reference
    :param buffer_dist: Distance in DEGREES to buffer the bounding polygon
    :param unzip_folder: Temporary folder where downloaded rasters will be saved
    :param force_download: The download will always be performed if this is true.
    :return:
    """

    log = Logger('DEM')

    # Query Science Base API for NED 10m DEM rasters within HUC 8 boundary
    urls = get_dem_urls(vector_path, buffer_dist)
    log.info('{} DEM raster(s) identified on Science Base.'.format(len(urls)))

    rasters = {}

    for url in urls:
        base_path = os.path.basename(os.path.splitext(url)[0])
        final_unzip_path = os.path.join(unzip_folder, base_path)
        file_path = download_unzip(url, download_folder, final_unzip_path, force_download)
        raster_path = find_rasters(file_path)

        # Sanity check that all rasters going into the VRT share the same cell resolution.
        dataset = gdal.Open(raster_path)
        gt = dataset.GetGeoTransform()

        # Store the geotransform for later
        gtHelper = Geotransform(gt)

        # Create a tuple of useful numbers to use when trying to figure out if we have a problem with cellwidths
        rasters[raster_path] = gtHelper
        dataset = None

    if (len(rasters.keys()) == 0):
        raise Exception('No DEM urls were found')

    # Pick one result to compare with and loop over to see if all the rasters have the same, exact dimensions
    elif len(rasters.keys()) > 1:
        widthStdDev = statistics.stdev([gt.CellWidth() for gt in rasters.values()])
        heightStdDev = statistics.stdev([gt.CellHeight() for gt in rasters.values()])

        # This is the broad-strokes check. If the cell widths are vastly different then this won't work and you'll get stitching artifacts when you resample
        # so we bail out.
        if widthStdDev > CELL_SIZE_MAX_STDDEV or heightStdDev > CELL_SIZE_MAX_STDDEV:
            log.warning('Multiple DEM raster cells widths encountered.')
            [log.warning('cell width {} :: ({}, {})'.format(rp, gt.CellWidth(), gt.CellHeight())) for rp, gt in rasters.items()]
            # raise Exception('Cannot continue. Raster cell sizes are too different and resampling will cause edge effects in the stitched raster')

        # Now that we know we have a problem we need to figure out where the truth is:
        # if widthStdDev > CELL_SIZE_THRESH_STDDEV or heightStdDev > CELL_SIZE_THRESH_STDDEV:
        #     for rpath, gt in rasters.items():
        #         log.warning('Correcting Raster: {} from:({},{}) to:({},{})'.format(rpath, gt.CellWidth(), gt.CellHeight(), widthAvg, heightAvg))
        #         gt.SetCellWidth(widthAvg)
        #         gt.SetCellHeight(heightAvg)
        #         dataset = gdal.Open(raster_path)
        #         dataset.SetGeoTransform(gt.gt)
        #         dataset = None

    return list(rasters.keys())


def find_rasters(search_dir):
    """
    Recursively search a folder for any *.img or *.tif rasters
    :param search_dir: Folder to be searched
    :return: List of full paths to any rasters found
    """

    for root, subFolder, files in os.walk(search_dir):
        for item in files:
            if item.endswith('.img') or item.endswith('.tif'):
                return os.path.join(root, item)

    raise Exception('Failed to find IMG raster in folder {}'.format(search_dir))


def verify_areas(raster_path, boundary_shp):
    """[summary]

    Arguments:
        raster_path {[type]} -- path
        boundary_shp {[type]} -- path

    Raises:
        Exception: [description] if raster area is zero
        Exception: [description] if shapefile area is zero

    Returns:
        [type] -- rastio of raster area over shape file area
    """
    log = Logger('Verify Areas')

    log.info('Verifying raster and shape areas')

    # This comes back in the raster's unit
    raster_area = 0
    with rasterio.open(raster_path) as ds:
        cell_count = 0
        gt = ds.get_transform()
        cell_area = math.fabs(gt[1]) * math.fabs(gt[5])
        # Incrememntally add the area of a block to the count
        progbar = ProgressBar(len(list(ds.block_windows(1))), 50, "Calculating Area")
        progcount = 0
        for ji, window in ds.block_windows(1):
            r = ds.read(1, window=window, masked=True)
            progbar.update(progcount)
            cell_count += r.count()
            progcount += 1

        progbar.finish()
        # Multiply the count by the area of a given cell
        raster_area = cell_area * cell_count
        log.debug('raster area {}'.format(raster_area))

    if (raster_area == 0):
        raise Exception('Raster has zero area: {}'.format(raster_path))

    # We could just use Rasterio's CRS object but it doesn't seem to play nice with GDAL so....
    raster_ds = gdal.Open(raster_path)
    raster_srs = gdal.osr.SpatialReference(wkt=raster_ds.GetProjection())

    # Load and transform ownership polygons by adminstration agency
    driver = gdal.ogr.GetDriverByName("ESRI Shapefile")
    data_source = driver.Open(boundary_shp, 0)
    layer = data_source.GetLayer()
    in_spatial_ref = layer.GetSpatialRef()

    # https://github.com/OSGeo/gdal/issues/1546
    raster_srs.SetAxisMappingStrategy(in_spatial_ref.GetAxisMappingStrategy())
    transform = gdal.osr.CoordinateTransformation(in_spatial_ref, raster_srs)

    shape_area = 0
    for polygon in layer:
        geom = polygon.GetGeometryRef()
        geom.Transform(transform)
        shape_area = shape_area + geom.GetArea()

    log.debug('shape file area {}'.format(shape_area))
    if (shape_area == 0):
        raise Exception('Shapefile has zero area: {}'.format(boundary_shp))

    area_ratio = raster_area / shape_area

    if (area_ratio < 1 and area_ratio > 0.9):
        log.warning('Raster Area covers only {0:.2f}% of the shapefile'.format(area_ratio * 100))
    if (area_ratio <= 0.9):
        log.error('Raster Area covers only {0:.2f}% of the shapefile'.format(area_ratio * 100))
    else:
        log.info('Raster Area covers {0:.2f}% of the shapefile'.format(area_ratio * 100))

    return area_ratio


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('vector', help='ShapeFile path to boundary polygon', type=argparse.FileType('r'))
    parser.add_argument('parent', help='Science Base GUID of parent item', type=str)
    parser.add_argument('epsg', help='EPSG spatial reference', type=int)
    parser.add_argument('folder', help='folder where DEM will be produced', type=str)
    args = parser.parse_args()

    try:
        download_dem(args.vector.name, args.epsg, 0.5, args.folder, os.path.join(args.folder, 'dem.tif'))

    except Exception as e:
        print(e)
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    main()
