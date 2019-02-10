# -------------------------------------------------------------------------------
# Name:           AutStageD.py
# Description:    Clip points based on tiles and extract NDVI values
# Purpose:        Automated prediction system for vegetation cover based on MODIS- NDVI satellite data and neural networks
# Author:         Sohaib K. M. Abujayyab
# Created:        11/02/2019
# Requirements: None
# -------------------------------------------------------------------------------
# Import system modules
import arcpy, os

arcpy.env.overwriteoutput = 1

Points = arcpy.GetParameterAsText(0)   # The polygon to be clipped
Grid = arcpy.GetParameterAsText(1)     # The clip features
inRasterList = arcpy.GetParameterAsText(2)
OutputFolder = arcpy.GetParameterAsText(3)
Gridrows = arcpy.SearchCursor(Grid)

RasterList1 = inRasterList.split(';')
for Raster in RasterList1:
    RasterName=os.path.basename(Raster)
    RasterShortName=RasterName[8:-29]
    arcpy.AddMessage(RasterShortName)

count = 0     # Start a counter to name output polygons
for row in Gridrows: # Loop through individual features of "poly_multi"
    out_poly = os.path.join(OutputFolder, "Points_tile" + str(count))  # Assemble the output poly name and path
    arcpy.Clip_analysis(Points, row.Shape, out_poly)
    out_poly2=out_poly+".shp"
    arcpy.sa.ExtractMultiValuesToPoints(out_poly2, RasterList1, "NONE") #NONE  BILINEAR
    arcpy.AddMessage("Tile " + str(count))
    count = count + 1
