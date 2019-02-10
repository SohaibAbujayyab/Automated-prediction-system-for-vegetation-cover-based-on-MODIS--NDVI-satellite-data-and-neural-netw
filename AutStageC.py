# -------------------------------------------------------------------------------
# Name:           AutStageC.py
# Description:    Grid of tiles
# Purpose:        Automated prediction system for vegetation cover based on MODIS- NDVI satellite data and neural networks
# Author:         Sohaib K. M. Abujayyab
# Created:        11/02/2019
# Requirements: None
# -------------------------------------------------------------------------------

# import system module
import arcpy
from arcpy import env

arcpy.env.overwriteOutput = True
arcpy.env.addOutputsToMap = True

# Create a Describe object from the shapefile
inVector = arcpy.GetParameterAsText(0)  # border
desc = arcpy.Describe(inVector)

# Set coordinate system of the output fishnet
incoordinate = arcpy.GetParameterAsText(1)
env.outputCoordinateSystem = incoordinate

# create boundary points from envelope
minX = (desc.extent.XMin)
maxX = (desc.extent.XMax)
minY = (desc.extent.YMin)
maxY = (desc.extent.YMax)
pxy = arcpy.Point(minX, minY)
pxY = arcpy.Point(minX, maxY)
pXy = arcpy.Point(maxX, minY)
pXY = arcpy.Point(maxX, maxY)

# Set the origin of the fishnet
originCoordinate = str(pxy.X) + " " + str(pxy.Y)

# Set the orientation
yAxisCoordinate = str(pxy.X) + " " + str(pxy.Y + 1)

# Number of rows and columns together with origin and opposite corner
cellSizeWidth = arcpy.GetParameterAsText(2)
cellSizeHeight = arcpy.GetParameterAsText(3)

# Set the oppositeCoorner
oppositeCoorner = str(pXY.X) + " " + str(pXY.Y)

# Create a point label feature class
labels = 'LABELS'

# Extent is set by origin and opposite corner - no need to use a template fc
templateExtent = '#'

# Each output cell will be a polygon
geometryType = 'POLYGON'

# Create bloks
outFeatureClass=arcpy.CreateFishnet_management("in_memory/outFeatureClass", originCoordinate, yAxisCoordinate, cellSizeWidth, cellSizeHeight, '#', '#', oppositeCoorner, labels, templateExtent, geometryType)

# Selection the bloks within the mask
arcpy.MakeFeatureLayer_management(outFeatureClass, 'bloks_lyr')
Selection = arcpy.SelectLayerByLocation_management('bloks_lyr', 'intersect', inVector)
Outputfc =  arcpy.GetParameterAsText(4)
arcpy.AddMessage(str(Outputfc)+"   path must saved as Geodatabase FC not shp")
arcpy.CopyFeatures_management(Selection, Outputfc)   #path must save as Geodatabase FC not shp

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
addLayer = arcpy.mapping.Layer(Outputfc)
arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")
