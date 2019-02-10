# -------------------------------------------------------------------------------
# Name:           AutStageA.py
# Description:    Extract and Mask NDVI from HDF based on AOI
# Purpose:        Automated prediction system for vegetation cover based on MODIS- NDVI satellite data and neural networks
# Author:         Sohaib K. M. Abujayyab
# Created:        11/02/2019
# Requirements: None
# -------------------------------------------------------------------------------

# Import system modules
import arcpy
import os

arcpy.env.overwriteOutput = True

arcpy.env.workspace = arcpy.GetParameterAsText(0)
rasterList = arcpy.ListRasters()
inMaskData = arcpy.GetParameterAsText(1)
OutputFolder = arcpy.GetParameterAsText(2)

#Extract NDVI from HDF
for raster in rasterList:
    arcpy.AddMessage(str(raster))
    OutputFolderpath = os.path.abspath(OutputFolder)
    OutputFolderpath2 = os.path.join(OutputFolderpath, '')
    OutputTif = str(OutputFolderpath2) + str(raster[9:-29])
    arcpy.AddMessage(str(OutputTif))
    Output=arcpy.ExtractSubDataset_management(raster, "in_memory/Output", "0")

    # Execute ExtractByMask
    arcpy.gp.ExtractByMask_sa("in_memory/Output", inMaskData, OutputTif+ ".tif")
    del Output
