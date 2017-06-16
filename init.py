



nuke.pluginAddPath('./python')
nuke.pluginAddPath('./plugins')
nuke.pluginAddPath('./luts')
nuke.pluginAddPath('./icons')
nuke.pluginAddPath('./Gizmos')

nuke.pluginAddPath('./Plugins/KeenTools_10.5')
nuke.pluginAddPath('./Plugins/cryptoMatte')
nuke.pluginAddPath('./Plugins/animatedSnap3D')


######## Import Python Scripts
import CheckOutputPath



####### Import Shotgun Toolkit for Renderodes
#import initiateShotgun


########KNOBDEFAULTS

nuke.knobDefault("EXPTool.mode", "0")
nuke.knobDefault("EXPTool.label", "[value mode]")
nuke.knobDefault("Grain2.seed", "[frame]")                                      # removes horrible pattern
nuke.knobDefault("Grain2.maskgrain", "0")                                      
nuke.knobDefault("Text.message", "frame [python '%04d' % nuke.frame()]")   # 4 padded frame number
nuke.knobDefault("Blur.channels","rgba")
nuke.knobDefault("Blur.crop","0")
nuke.knobDefault("Defocus.channels","rgba")
nuke.knobDefault("ZBlur.channels","rgba")
nuke.knobDefault("Read.before", "hold")
nuke.knobDefault("Read.after", "hold")
nuke.knobDefault("Roto.toolbar_autokey", "1")
nuke.knobDefault("Roto.output","rgba")
nuke.knobDefault("Roto.cliptype","no clip")
nuke.knobDefault("RotoPaint.toolbar_autokey", "1")
nuke.knobDefault("RotoPaint.crop","0")
nuke.knobDefault("RotoPaint.cliptype","no clip")
nuke.knobDefault("Write.beforeRender","CheckOutputPath.CheckOutputPath()")
nuke.knobDefault("Write.channels","rgba")
nuke.knobDefault("Write.autocrop","1")
nuke.knobDefault("Viewer.hide_input","1")
nuke.knobDefault("Retime.label","start frame = [value output.first]\nlast frame = [value output.last]\n\nfrom\n\noriginal start = [value input.first]\noriginal end = [value input.last]\n\n")




####FORMATS

#nuke.addFormat("2104 1136 1.0 GITS_cropped_DELVERY_FORMAT_2K")
#nuke.addFormat("2104 1184 1.0 GITS_CG_format_2K")
#nuke.knobDefault("root.format", "GITS_CG_format_2K")






###### LUTS


#nuke.ViewerProcess.register("AlexaV3Rec709_standard", nuke.createNode,("Vectorfield", "vfield_file Y:/_nuke_global_setup/Luts/AlexaV3_EI0800_LogC2Video_Rec709_EE_nuke3d.cube colorspaceIn AlexaV3LogC"))
#nuke.ViewerProcess.register("ACEScc_RRT_Rec709", nuke.createNode,("Vectorfield", "vfield_file Y:\_nuke_global_setup\Luts\rpo\ACEScc_RRT_Rec709.cube colorspaceIn AlexaV3LogC"))





#nuke.ViewerProcess.register("AlexaV3Rec709_GITS", nuke.createNode,("Vectorfield", "vfield_file Y:/_nuke_global_setup/Luts/GHOST_SHED_DAILIES_OT_V1_Rec709_EE.cube colorspaceIn AlexaV3LogC"))





