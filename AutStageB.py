# -------------------------------------------------------------------------------
# Name:               AutStageB.py
# Description:        Converts a raster dataset to point features
# Purpose:            Automated prediction system for vegetation cover based on MODIS- NDVI satellite data and neural networks
# Author:             Sohaib K. M. Abujayyab
# Created:            11/02/2019
# Requirements: None
# -------------------------------------------------------------------------------


# Import system modules
import arcpy
from arcpy import env

# Set local variables
inRaster = arcpy.GetParameterAsText(0)
arcpy.env.outputCoordinateSystem = arcpy.GetParameterAsText(1)

outPoint = arcpy.GetParameterAsText(2)
field = "VALUE"

# Execute RasterToPoint
arcpy.RasterToPoint_conversion(inRaster, outPoint, field)


