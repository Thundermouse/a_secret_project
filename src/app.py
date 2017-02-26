from gui.iframe import MainWin
import wx
class MApp(wx.App):
    def __init__(self,parent):
        super(MApp,self).__init__(parent)
        self.Mframe = MainWin(None)
        self.Bind(wx.EVT_BUTTON, self.ButtonDetector)
        self.SetTopWindow(self.Mframe)
    def ButtonDetector(self,event):
        print "MainApp Event Button:"+event.GetEventObject().GetLabel()
        if event.GetEventObject().GetLabel() == "Search":
            print "MainApp Event Search for:"+self.Mframe.tc.GetValue() #Search Operation
        elif event.GetEventObject().GetLabel() == "Close":
            exit()
if __name__ == '__main__':
    app = MApp(None)
    app.MainLoop()