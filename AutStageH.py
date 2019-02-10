# -------------------------------------------------------------------------------
# Name:           AutStageH.py
# Description:    Combined tiles of predicted points
# Purpose:        Automated prediction system for vegetation cover based on MODIS- NDVI satellite data and neural networks
# Author:         Sohaib K. M. Abujayyab
# Created:        11/02/2019
# Requirements: None
# -------------------------------------------------------------------------------

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *


# Set local variables
inPointFeaturesList = arcpy.GetParameterAsText(0)
OutputFeature = arcpy.GetParameterAsText(1)

# Execute Merge
arcpy.Merge_management(inPointFeaturesList, OutputFeature)
