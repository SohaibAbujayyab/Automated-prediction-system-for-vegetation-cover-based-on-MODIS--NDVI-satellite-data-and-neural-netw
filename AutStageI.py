# -------------------------------------------------------------------------------
# Name:           AutStageI.py
# Description:    Point To Raster
# Purpose:        Automated prediction system for vegetation cover based on MODIS- NDVI satellite data and neural networks
# Author:         Sohaib K. M. Abujayyab
# Created:        11/02/2019
# Requirements: None
# -------------------------------------------------------------------------------

# Import system modules
import arcpy, os
from arcpy import env

arcpy.env.overwriteOutput = True
arcpy.env.addOutputsToMap = True

#
in_features = arcpy.GetParameterAsText(0)
ListOfFields = arcpy.GetParameterAsText(1)    # list of selected fields
arcpy.env.mask =  arcpy.GetParameterAsText(2)
OutputFolder =  arcpy.GetParameterAsText(3)

arcpy.env.extent = in_features
myExtent = arcpy.env.extent

count = 1     # Start a counter to name output Raster files
for field in ListOfFields.split(';'):
    arcpy.AddMessage("Field   " + field)
    outRaster = os.path.join(OutputFolder, "NDVI" + str(count))  # Assemble the output poly name and path
    count = count + 1
    assignmentType = "MOST_FREQUENT"
    priorityField = ""
    cellSize = 300 #231.6563583

    # Execute PointToRaster
    #arcpy.PointToRaster_conversion(in_features, field, outRaster,
                                   #assignmentType, priorityField, cellSize)
    arcpy.AddMessage("Output Raster   " + outRaster)
    arcpy.AddMessage(str(myExtent))
    in_features2 = in_features + " " + field + " " + "PointElevation"
    arcpy.gp.TopoToRaster_sa(in_features2, outRaster, cellSize, myExtent, "20", "", "", "ENFORCE",
                             "CONTOUR", "20", "", "1", "0", "2.5", "100", "", "", "", "", "", "", "", "")
