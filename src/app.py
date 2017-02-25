from gui.iframe import MainWin
import wx
class MApp(wx.App):
    def __init__(self,parent):
        super(MApp,self).__init__(parent)
        self.Mframe = MainWin(None)
        self.Bind(wx.EVT_BUTTON, self.ButtonDetector)
        self.SetTopWindow(self.Mframe)
    def ButtonDetector(self,event):
        print "MainApp Class Search"
if __name__ == '__main__':
    app = MApp(None)
    #MainWin(None,title="Search Engine")
    app.MainLoop()