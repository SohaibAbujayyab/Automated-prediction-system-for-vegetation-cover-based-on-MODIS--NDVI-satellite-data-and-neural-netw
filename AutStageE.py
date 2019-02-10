# -------------------------------------------------------------------------------
# Name:           AutStageE.py
# Description:    Data preliminary processing  (Delete features from a feature class based on an expression)
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

ListOftiles = arcpy.GetParameterAsText(0)
a = arcpy.GetParameterAsText(1)
# List of Fields
ListOfFields = arcpy.GetParameterAsText(2)    # list of selected fields
str1 = arcpy.GetParameterAsText(3)
str2 = arcpy.GetParameterAsText(4)

# Set local variables
tempLayer = "pointsLayer"

for feature in ListOftiles.split(';'):
    arcpy.AddMessage("Tile " + str(feature))
    s = len(ListOfFields.split(';')) - 1
    count =0
    arcpy.AddMessage("count of fields   " + str(s))
    Expression4 = ""
    Expression55 = ""
    for field in ListOfFields.split(';'):
        # Set local variables
        Expression1 = '"' + str(field) + '"' + "<=" + str1
        Expression2 = '"' + field + '"' + ">=" + str2

        if count == s:
            Expression3 = Expression1 + " OR " + Expression2
            Expression4 = Expression4 + Expression3

        else:
            Expression3 = Expression1 + " OR " + Expression2 + " OR "
            Expression4 = Expression4 + Expression3

        count = count + 1

    # Execute MakeFeatureLayer
    arcpy.MakeFeatureLayer_management(feature, tempLayer)

    # Execute SelectLayerByAttribute to determine which features to delete
    arcpy.SelectLayerByAttribute_management(tempLayer, "NEW_SELECTION",
                                            Expression4)
    # Execute GetCount and if some features have been selected, then
    #  execute DeleteFeatures to remove the selected features.
    arcpy.DeleteFeatures_management(tempLayer)