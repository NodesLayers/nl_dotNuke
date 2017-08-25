import nuke
import os

myVersion = "v1.0 - 18-08-2017"

def set_write():
    print ""
    print "----------- setWrite -----------"
    print "----------- "+myVersion+" -----------"

       
    
    if nuke.root().name() == "Root":
        nuke.message("You need to save your script properly before continuing!")
  


    ## Find context from scriptname
    try:
        nuke_script = os.path.basename(nuke.root().name())
        nuke_script = str.split(nuke_script,"_")

        ## Set Script Variables
        sequence = str.upper(nuke_script[0])
        shot = nuke_script[1]
        print "Context: "+sequence+"_"+shot+"_"+ident
    except:
        print "Couldn't find Sequence, Shot"


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
    p = nuke.Panel('MAELSTROM WRITER '+myVersion)    
    p.addEnumerationPulldown('Show:', "DNG02_MAE")
    p.addEnumerationPulldown('Context:', sequence+"_"+shot)
    p.addEnumerationPulldown('Render type:', 'comp precomp element')
    p.addEnumerationPulldown('Format:', 'movie exr-sequence')
    p.addSingleLineInput('(optional) Identifier:', '')


    ret = p.show()




    ## Set User Variables
    render_type = p.value("Render type:")
    format = p.value("Format:")
    ident = p.value("(optional) Identifier:")
        
   



##-------------- PATHING -----------------------

    #### Export base path
    nuke_script_path = os.path.dirname(nuke.root().name())
    render_basepath = nuke_script_path
    render_basepath = os.path.split(render_basepath)[0]
    render_basepath = os.path.join(render_basepath, "renders", render_type)
    render_basepath = os.path.normpath(render_basepath)
    print render_basepath


    #### Filepath Profiles
    filename_base = sequence+"_"+shot+"_"+render_type+"_"+ident+"_"+scriptVersion
    if ident == "":
            filename_base = sequence+"_"+shot+"_"+render_type+"_"+scriptVersion
    print filename_base
    
    if format == "movie":
        filename = filename_base+".mov"
        filepath = os.path.join(render_basepath,filename)
        print filepath
        
    if format == "exr-sequence":
        filename = filename_base+".%04d.exr"
        filepath = os.path.join(render_basepath,filename_base,filename)
        print filepath
 
    
    ## Set writeFile
    filepath = os.path.normpath(filepath)
    filepath = filepath.replace("\\", "/")
    filepath = filepath.lower()
    print "Export filename: "+filepath


	
##-------------- CREATE WRITENODE -----------------------

    #Create Writenode
    n = nuke.createNode("Write")
    n["file"].setValue(filepath)

    if format == "movie":
        n["render_order"].setValue(2)
        n["colorspace"].setValue("linear")
    if format == "exr-sequence":
        n["autocrop"].setValue(1)



#set_write()








