import nuke
import os

myVersion = "v1.0"

def ilmExporter():
    print ""
    print "----------- setWrite -----------"
    print "----------- "+myVersion+" -----------"

    n = nuke.selectedNode()
    
    
    if nuke.root().name() == "Root":
        nuke.message("You need to save your script properly before continuing!")
        
#    if (n.Class() != "Write") or (n.Class() != "DeepWrite"):
#        nuke.message("This only works on Write nodes... duh...!")
        
        


    ## Find sequence, shot & assetName from Nuke scriptName
    try:
        scriptInfo = os.path.basename(nuke.root().name()) #Nuke filename
        #scriptInfo = os.path.normcase(scriptInfo) #Lowercase + forward slash
        scriptInfo = str.split(scriptInfo,"_")
        # Set Script Variables
        sequence = str.upper(scriptInfo[0])
        print "Sequence is: "+sequence
        shot = scriptInfo[1]
        print "Shot is: "+shot
        assetName = scriptInfo[2]
        print "Asset name is: "+assetName
        taskName = scriptInfo[3]
        print "Task name is: "+taskName
    except:
        print "Couldn't find Sequence, Shot, Assetname and Taskname"


    #Set Basepath
    if os.name == "nt":
        basepath = "//192.168.50.10/FilmShare/"
    elif os.name == "posix":
        basepath = "/Volumes/FilmShare/"
    print "Basepath for this OS: "+basepath


    #Find scriptVersion
    scriptVersion = nuke.root().name()
    scriptVersion = str.split(scriptVersion,"_")
    scriptVersion = scriptVersion[-1]
    scriptVersion = str.split(scriptVersion,".")
    scriptVersion = scriptVersion[0]
    print "Scriptversion: "+scriptVersion


    ## PANEL
    p = nuke.Panel('ILM EXPORTER '+myVersion)    
    p.addEnumerationPulldown('Show:', "RPO_01")
    p.addEnumerationPulldown('Vendor:', 'ILM')
    p.addEnumerationPulldown('Context:', 'shot')
    p.addEnumerationPulldown('Layer Type:', 'GFX slapcomp_EXR slapcomp_MOV GFX_EXR GFX_MOV')
    p.addSingleLineInput('assetname.taskname:', '')
    p.addSingleLineInput('Take number:', '')
    p.addSingleLineInput('Pass (layer):', '')
    p.addSingleLineInput('Extra (optional):', '')
    p.addSingleLineInput('Version override (optional):', '')
#    p.addEnumerationPulldown('mergeOp:', 'over plus screen atop average color-burn color-dodge conjoint-over copy difference disjoint-over divide exclusion from geometric hard-light hypot in mask matte max min minus multiply out overlay soft-light stencil under xor')



    ret = p.show()




    ## Set User Variables
    show = p.value("Show:")
    vendor = p.value("Vendor:")
    context = p.value("Context:")
    layerType = p.value("Layer Type:")
    assetname_taskname = p.value("assetname.taskname:")
    if not assetname_taskname:
        assetname_taskname = assetName+"."+taskName
    assetname_taskname = assetname_taskname.replace("_" , ".")
    take = p.value("Take number:")
    layer = p.value("Pass (layer):")
    extra = p.value("Extra (optional):")
    versionOverride = p.value("Version override (optional):")



    #### Export base path
    fp = os.path.join(basepath, show, "sequences",sequence, sequence+"_"+shot, "nuke", "__nk", "__OUTPUT")
    fp = os.path.join(fp, sequence+"."+shot)
    if assetname_taskname:
        fp = os.path.join(fp+"."+assetname_taskname)
    fp = os.path.join(fp+".export."+scriptVersion)
    fp = os.path.normpath(fp)
    fp = fp.replace("\\" , '/')
    #print fp


    #### File basename
    fn = sequence+"."+shot
    if assetname_taskname:
        fn = fn+"."+assetname_taskname
    if take:
        fn = fn+".t"+take
    if layer:
        fn = fn+"."+layer
    if extra:
        fn = fn+"."+extra
    if versionOverride:
        fn = fn+".v"+versionOverride
    else:
        fn = fn+"."+scriptVersion
    #print "Export filename: "+fn


    #### Export filePaths
    if layerType == "GFX":
        fp = os.path.join(fp, fn, fn+".%04d.exr")


    if layerType == "slapcomp_EXR":
        fp = os.path.join(fp, "_exr", "slapcomp", fn+".%04d.exr")

    if layerType == "GFX_EXR":
        fp = os.path.join(fp, "_exr", "gfx", fn+".%04d.exr")

    if layerType == "slapcomp_MOV":
        fp = os.path.join(fp, "_mov", fn+".slapcomp.mov")

    if layerType == "GFX_MOV":
        fp = os.path.join(fp, "_mov", fn+".GFX.mov")

    
                    
    ## Set WriteNode
    n = nuke.selectedNode()
    n = nuke.toNode(n.name())
    
    
    ## Set writeFile
    fp = os.path.normpath(fp)
    fp = fp.replace("\\" , '/')
    fp = fp.lower()
    print "Export filename: "+fp
    n["file"].setValue(fp)


    ## Codec/Data Profiles
    if (layerType == "GFX") or (layerType == "slapcomp_EXR"):
        n["file_type"].setValue("exr")
        n["channels"].setValue("all")
        n["datatype"].setValue("16 bit half")
        n["compression"].setValue("Zip (1 scanline)")
        try:
            n["autocrop"].setValue(1)
        except:
            pass


    if (layerType == "slapcomp_MOV") or (layerType == "GFX_MOV") or (context == "plate"):
        n["file_type"].setValue("mov")
        n["meta_encoder"].setValue("mov32")
        n["meta_codec"].setValue("mjpa")




#ilmExporter()








