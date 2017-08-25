def plateWrite():

    import os
    import nuke


    for s in nuke.selectedNodes("Read"):

        # Platename
        fn = s["file"].getValue()
        fn = os.path.basename(fn)
        fn = fn.split(".")[0]


        #File Root for MOV
        fp = s["file"].getValue()
        fp = os.path.dirname(fp)
        fp = os.path.split(fp)[0]


        #New Filepath
        np = os.path.join(fp,fn+".mov")
        np = os.path.normpath(np)
        np = np.replace("\\", "/")
        print np

        
        #Create Writenode
        n = nuke.createNode("Write")
        n["file"].setValue(np)
        n["meta_codec"].setValue("mjpb")