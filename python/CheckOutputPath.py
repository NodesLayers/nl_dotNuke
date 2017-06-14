#		       Check output path Script 
#	Created by: Sander Jansen - www.Sander-Art.com
#		   for info: sander@sander-art.com
#		        	31-10-2010

import nuke, os

#This part of the scripts checks the output path and if it doesn't exist it creates it for you
def CheckOutputPath():
	file = nuke.filename(nuke.thisNode())
	dir = os.path.dirname(file)
	osdir = nuke.callbacks.filenameFilter(dir)
	try:
		os.makedirs (osdir)
	except OSError:
		pass
		
		

#This script  adds the 'CheckOutputPath()' script to a selected write node (this can be added as a button in the GUI of Nuke)
def AddCheckOutputPath():
	for node in nuke.selectedNodes():
		if node.Class() == 'Write':
			node.knob('beforeRender').setValue('CheckOutputPath.CheckOutputPath()')
		else:
			nuke.message('This script can only be added to a write node')