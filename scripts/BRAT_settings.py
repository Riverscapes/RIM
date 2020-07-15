import arcpy
import os
from arcpy import env
from create_project import make_folder
from arcpy.sa import *
from arcpy.da import *
arcpy.CheckOutExtension('Spatial')
arcpy.env.overwriteOutput = True


def BRAT_settings (folder, BRAT, BRAT_out, SP_cut, grad_cut):
    """
    folder: path to working folder
    BRAT: path to BRAT output file
    BRAT_out: what you want the name of the output BRAT file with the settings field to be called
    SP_cut: the streampower at which dams will fail
    grad_cut: the gradient cutoff between classic and steep setting
    """

    # make a copy of the input BRAT shapefile and save to an output folder
    out_folder = make_folder(folder, "Output")
    arcpy.CopyFeatures_management(BRAT, os.path.join(out_folder, BRAT_out))
    
    # make new field in output BRAT shapefile for settings
    arcpy.AddField_management(os.path.join(out_folder, BRAT_out), 'setting', "TEXT")
    arcpy.AddField_management(os.path.join(out_folder, BRAT_out), 'Slope', "DOUBLE")

    # calculate slope as a percent
    with arcpy.da.UpdateCursor(os.path.join(out_folder, BRAT_out), ['Slope', 'iGeo_Slope']) as Ucursor:
        for Urow in Ucursor:
            Urow[0] = Urow[1] * 100
            Ucursor.updateRow(Urow)

    # make setting type for areas where capacity is 0 "unsuitable"
    arcpy.MakeFeatureLayer_management(os.path.join(out_folder, BRAT_out), 'BRAT_noCap', "oCC_EX = 0")
    ## populate setting field
    with arcpy.da.UpdateCursor('BRAT_noCap', 'setting') as Ucursor:
        for Urow in Ucursor:
            Urow[0] = 'unsuitable'
            Ucursor.updateRow(Urow)

    # create feature layer or segments where capacity is greater than 0 to make selections
    arcpy.MakeFeatureLayer_management(os.path.join(out_folder, BRAT_out), 'BRAT_out', "oCC_EX > 0")

    # steeper setting
    ## gradient
    arcpy.SelectLayerByAttribute_management('BRAT_out', 'NEW_SELECTION', '"Slope" >=%d' % grad_cut)
    ## SP
    #arcpy.SelectLayerByAttribute_management('BRAT_out', 'SUBSET_SELECTION', '"iHyd_SPLow" <=%d' % SP_cut)
    ## populate setting field
    with arcpy.da.UpdateCursor('BRAT_out', 'setting') as Ucursor:
        for Urow in Ucursor:
            Urow[0] = 'steep'
            Ucursor.updateRow(Urow)
    
    # floodplain setting
    ## gradient
    arcpy.SelectLayerByAttribute_management('BRAT_out', 'NEW_SELECTION', '"Slope" <=%d' % 3)
    ## SP
    arcpy.SelectLayerByAttribute_management('BRAT_out', 'SUBSET_SELECTION', '"iHyd_SPLow" >=%d' % SP_cut)
    ## populate setting field
    with arcpy.da.UpdateCursor('BRAT_out', 'setting') as Ucursor:
        for Urow in Ucursor:
            Urow[0] = 'floodplain'
            Ucursor.updateRow(Urow)
    
    # "Classic" setting
    ## gradient
    arcpy.SelectLayerByAttribute_management('BRAT_out', 'NEW_SELECTION', '"Slope" <=%d' % grad_cut)
    ## SP
    arcpy.SelectLayerByAttribute_management('BRAT_out', 'SUBSET_SELECTION', '"iHyd_SPLow" <=%d' % SP_cut)
    ## populate setting field
    with arcpy.da.UpdateCursor('BRAT_out', 'setting') as Ucursor:
        for Urow in Ucursor:
            Urow[0] = 'classic'
            Ucursor.updateRow(Urow)

    

folder = r"C:\Users\A02295870\Box\0_ET_AL\NonProject\etal_Drone\2019\Inundation_sites\Snake_headwaters\BRAT\settings"
BRAT = r"C:\Users\A02295870\Box\0_ET_AL\NonProject\etal_Drone\2019\Inundation_sites\Snake_headwaters\BRAT\BatchRun_03\Outputs\Output_01\02_Analyses\Conservation_Restoration_Model_Perennial.shp"
BRAT_out = 'oCC_EX_6_25_peren.shp'
SP_cut = 25
grad_cut = 6

BRAT_settings(folder, BRAT, BRAT_out, SP_cut, grad_cut)






