import wx
class MainWin(wx.Frame):
    def __init__(self,parent,title="Search Engine"):
        super(MainWin,self).__init__(parent,title=title,size=(400,600))
        self.InitUI()  
        self.Centre()  
        self.Show()  
    def InitUI(self):  
        panel = wx.Panel(self)
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)  
        font.SetPointSize(9)
        #Setting Top Layout
        vbox = wx.BoxSizer(wx.VERTICAL)
        #First line layout, search button and text frame
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)  
        b1 = wx.Button(panel,label='Search')
        b1.SetFont(font)
        hbox1.Add(b1,flag=wx.RIGHT,border=8)
        self.tc = wx.TextCtrl(panel,0)
        hbox1.Add(self.tc,proportion=1,border=8)
        vbox.Add(hbox1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,border=10)
        vbox.Add((2,10))
        #second line layout, single choice frame
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        sampleList = ['Author', 'Publication', 'Conference']
        self.ch1=wx.RadioBox(panel, -1, "Select Mode", (10, 10), wx.DefaultSize,
        sampleList, 3, wx.RA_SPECIFY_COLS)
        self.ch1.SetFont(font)
        hbox2.Add(self.ch1)
        vbox.Add(hbox2, flag=wx.LEFT, border=10)
        vbox.Add((-1, 15))
        #the third line layout, view frame
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)  
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_READONLY)
        hbox3.Add(tc2, proportion=1, flag=wx.EXPAND)  
        vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,border=10)
        vbox.Add((-1, 10))
        #the last layout
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)  
        btn1 = wx.Button(panel, label='About', size=(70, 30))
        hbox5.Add(btn1)  
        btn2 = wx.Button(panel, label='Close', size=(70, 30))  
        hbox5.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)  
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
        panel.SetSizer(vbox)
        #define actions
        self.Bind(wx.EVT_BUTTON,self.ButtonClick,b1)
        self.Bind(wx.EVT_BUTTON, self.ButtonClick, btn1)
        self.Bind(wx.EVT_BUTTON, self.ButtonClick, btn2)
        self.Bind(wx.EVT_RADIOBOX,self.ModeSelect,self.ch1)

    def ModeSelect(self,event):
        radioSelected = event.GetEventObject()
        print "WinSelectEvent:"+radioSelected.GetStringSelection()+' Selected'
        event.Skip()
    def ButtonClick(self,event):
        print "WinButtonEvent:"+event.GetEventObject().GetLabel()
        if event.GetEventObject().GetLabel()=="About":
            dlg = wx.MessageDialog(None, u"Web Mining Course Project \nMember:\n    JiangLei\n    XuChenYang\n    CaoYuHai\n", u"About", wx.YES_DEFAULT)
            if dlg.ShowModal() == wx.ID_YES:
                self.Close(True)
            dlg.Destroy()
        elif event.GetEventObject().GetLabel()=="Search":
            event.Skip()
        elif event.GetEventObject().GetLabel()=="Close":
            event.Skip()
