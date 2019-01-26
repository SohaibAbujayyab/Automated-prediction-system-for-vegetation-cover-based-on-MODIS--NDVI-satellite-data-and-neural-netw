try:
    import arcpy
    import os
    from arcpy.sa import *



    arcpy.env.workspace = arcpy.GetParameterAsText(0)
    rasterList = arcpy.ListRasters()
    arcpy.AddMessage('Number of images are  '+ str(len(rasterList)))

    inMaskData = arcpy.GetParameterAsText(1)
    OutputFolder = arcpy.GetParameterAsText(2)
    arcpy.AddMessage(str(inMaskData))
    i=0
    # Mask NDVI for study area border
    for raster in rasterList:

        i+=1
        arcpy.AddMessage(str(i))
        arcpy.AddMessage(str(raster))


        OutputFolderpath = os.path.abspath(OutputFolder)
        OutputFolderpath2 = os.path.join(OutputFolderpath, '')
        OutputTif = str(OutputFolderpath2) + str(raster[8:-29])
        if arcpy.Exists(OutputTif):
            arcpy.AddError(str(OutputTif) + " file is Exists.")
        arcpy.AddMessage(str(OutputTif))

        # Execute ExtractByMask
        arcpy.gp.ExtractByMask_sa(raster, inMaskData, OutputTif)

except:
    #arcpy.GetMessages()
    #arcpy.AddMessage("Extract Subdataset example failed.")
    arcpy.AddError("Extract Subdataset failed.")
    #arcpy.AddWarning("Extract Subdataset failed.")

