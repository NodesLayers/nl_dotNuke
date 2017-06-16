########### DEADLINE -------------------------------------------------------------------------------------
import DeadlineNukeClient
menubar = nuke.menu("Nuke")
tbmenu = menubar.addMenu("&Thinkbox")
tbmenu.addCommand("Submit Nuke To Deadline", DeadlineNukeClient.main, "F8")
try:
    if nuke.env[ 'studio' ]:
        import DeadlineNukeFrameServerClient
        tbmenu.addCommand("Reserve Frame Server Slaves", DeadlineNukeFrameServerClient.main, "")
except:
    pass
try:
    import DeadlineNukeVrayStandaloneClient
    tbmenu.addCommand("Submit VRay Standalone to Deadline", DeadlineNukeVrayStandaloneClient.main, "")
except:
    pass
	
############ ----------------------------------------------------------------------------------------------

menubar=nuke.menu("Nuke")
m=menubar.addMenu("Python")
#m.addCommand("&NewItem", "PythonCode", "Shortcut", icon="IconName", index=#)

import launchFile
m.addCommand("Launch file...", "launchFile.launchFile()", "alt+q")

import readFromWrite
m.addCommand("Read from Write", "readFromWrite.ReadFromWrite()", "alt+r")
