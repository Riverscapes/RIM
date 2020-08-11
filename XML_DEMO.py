from settings import ModelConfig
from lib.util import safe_makedirs
from lib.loghelper import Logger
import os
import sys
import datetime
import traceback
import time
import argparse
import uuid
from lib.project import RSProject, RSLayer

"""

Instructuions:

    1. create a file called .env in the root and add the following line (without the quotes):
                "PROJECTFILE=C:/path/to/my/folder/that/will/have/project.rs.xml"
    2. Run `BuildXML` from VSCode's Run dropdown menu


"""

# change to this value after the pull request is finished: http://xml.riverscapes.xyz/Projects/XSD/V1/Inundation.xsd
cfg = ModelConfig('https://raw.githubusercontent.com/Riverscapes/RiverscapesXML/innundation/Projects/XSD/V1/Inundation.xsd')

# Define the types of layers we're going to use up top so we can re-use them later
LayerTypes = {
    # RSLayer(name, id, tag, rel_path)
    'AP_01': RSLayer('2019 August', 'AP_01', 'Raster', '01_Inputs/01_Imagery/AP_01/orthomosaic.tif')
}


def build_xml(projectpath):
    # Create the top-level nodes
    log = Logger('build_xml')
    log.info('Starting the build of the XML')
    project_name = 'Inundation Mapper'
    project = RSProject(cfg, projectpath)
    project.create(project_name, 'Inundation')

    # Add the root metadata
    project.add_metadata({
        'ModelVersion': cfg.version,
        'date_created': str(int(time.time())),
        'HUC8': '16010201',
        'InundationVersion': cfg.version,
        'watershed': 'Upper Bear',
        'site_name': 'Mill Creek',
    })

    # Create the realizations container node
    realizations = project.XMLBuilder.add_sub_element(project.XMLBuilder.root, 'Realizations')

    # Example InundationContext Realization
    # ================================================================================================
    r1_node = project.XMLBuilder.add_sub_element(realizations, 'InundationContext', None, {
        'id': 'INN_CTX01',
        'dateCreated': datetime.datetime.now().isoformat(),
        'guid': str(uuid.uuid1()),
        'productVersion': cfg.version
    })
    #  add a <Name> node
    project.XMLBuilder.add_sub_element(r1_node, 'Name', project_name)

    # Realization <MetaData>
    project.add_metadata({
        'mapper': 'Karen Bartelt',
        'date_mapped': '02042020',
        'year1': 'estimated pre beaver',
        'year2': '2019',
        'RS_used': 'RS_01'
    }, r1_node)

    # Add an <Input> and <Output> nodes
    r1_inputs = project.XMLBuilder.add_sub_element(r1_node, 'Inputs')
    r1_outputs = project.XMLBuilder.add_sub_element(r1_node, 'Outputs')

    # Now we can add inputs to the context raster
    project.add_project_raster(r1_inputs, LayerTypes['AP_01'], replace=False)

    # Example DCE Realization
    # ================================================================================================
    r2_node = project.XMLBuilder.add_sub_element(realizations, 'InundationDCE', None, {
        'id': 'DCE_01',
        'dateCreated': datetime.datetime.now().isoformat(),
        'guid': str(uuid.uuid1()),
        'productVersion': cfg.version
    })
    project.XMLBuilder.add_sub_element(r2_node, 'Name', 'August 2019')
    # Add an <Input> and <Output> nodes
    r2_inputs = project.XMLBuilder.add_sub_element(r2_node, 'Inputs')
    r2_outputs = project.XMLBuilder.add_sub_element(r2_node, 'Outputs')

    # Example CD Realization
    # ================================================================================================
    r3_node = project.XMLBuilder.add_sub_element(realizations, 'InundationCD', None, {
        'id': '',
        'dateCreated': datetime.datetime.now().isoformat(),
        'guid': str(uuid.uuid1()),
        'productVersion': cfg.version
    })
    project.XMLBuilder.add_sub_element(r3_node, 'Name', '2019 vs estimated pre beaver')
    # Add an <Input> and <Output> nodes
    r3_inputs = project.XMLBuilder.add_sub_element(r3_node, 'Inputs')
    r3_outputs = project.XMLBuilder.add_sub_element(r3_node, 'Outputs')

    # Finally write the file
    log.info('Writing file')
    project.XMLBuilder.write()
    log.info('Done')


def edit_xml(projectpath):
    log = Logger('edit_xml')
    log.info('Loading the XML to make edits...')
    # Load up a new RSProject class
    project = RSProject(cfg, projectpath)

    # Now, instead of creating nodes we can just find them
    r1_node = project.XMLBuilder.find_by_id('INN_CTX01')

    # Now we can add new metadata values to this node
    project.add_metadata({'EditedVal': 'Some Realization Value here'}, r1_node)

    # Same is true for Rasters if we want
    r1_input_raster_node = project.XMLBuilder.find_by_id('AP_01')
    project.add_metadata({'EditedVal Raster': 'Some Raster Value here'}, r1_input_raster_node)

    # Don't forget to write back to the file
    log.info('Writing file')
    project.XMLBuilder.write()
    log.info('Done')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('projectpath', help='NHD flow line ShapeFile path', type=str)
    parser.add_argument('--verbose', help='(optional) a little extra logging ', action='store_true', default=False)

    args = cfg.parse_args_env(parser)

    if args.projectpath is None or len(args.projectpath) < 10:
        raise Exception('projectpath has invalid value')

    # Initiate the log file
    log = Logger('Inundation XML')
    log.setup(logPath=os.path.join(args.projectpath, 'Inundation.log'), verbose=args.verbose)

    try:
        log.info('Starting')
        build_xml(args.projectpath)
        edit_xml(args.projectpath)
        log.info('Exiting')

    except Exception as e:
        log.error(e)
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)

    sys.exit(0)
