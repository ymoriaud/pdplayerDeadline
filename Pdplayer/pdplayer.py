from Deadline.Plugins import *

######################################################################
## This is the function that Deadline calls to get an instance of the
## main DeadlinePlugin class.
######################################################################
def GetDeadlinePlugin():
    return pdplayerPlugin()

######################################################################
## This is the function that Deadline calls when the plugin is no
## longer in use so that it can get cleaned up.
######################################################################
def CleanupDeadlinePlugin( deadlinePlugin ):
    deadlinePlugin.Cleanup()

######################################################################
## This is the main DeadlinePlugin class for MyPlugin.
######################################################################
class pdplayerPlugin (DeadlinePlugin):

    ## Hook up the callbacks in the constructor.
    def __init__( self ):
        self.InitializeProcessCallback += self.InitializeProcess
		self.RenderExecutableCallback += self.RenderExecutable
        self.RenderArgumentCallback += self.RenderArgument

    ## Clean up the plugin.
    def Cleanup():
        del self.InitializeProcessCallback

    ## Called by Deadline to initialize the plugin.
    def InitializeProcess( self ):
        # Set the plugin specific settings.
        self.SingleFramesOnly = False
        self.PluginType = PluginType.Simple
		
	 ## Callback to get the executable used for rendering.
    def RenderExecutable( self ):
        return self.GetConfigEntry( "PdplayerExecutable" )
		
	 ## Callback to get the arguments that will be passed to the executable.
    def RenderArgument( self ):
        arguments += " -start " + str(self.GetStartFrame()) + " -end " + str(self.GetEndFrame())
        arguments += " -scene \"" + self.GetDataFilename() + "\""
        return arguments