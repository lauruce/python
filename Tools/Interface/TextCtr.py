import wx


        # super(Mywin, self).__init__(parent, title=title, size=(350, 250))
        #
        # panel = wx.Panel(self)
        # vbox = wx.BoxSizer(wx.VERTICAL)
        #
        # hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        # l1 = wx.StaticText(panel, -1, "text")
        #
        # hbox1.Add(l1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        # self.t1 = wx.TextCtrl(panel)
        #
        # hbox1.Add(self.t1, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        # self.t1.Bind(wx.EVT_TEXT, self.OnKeyTyped)
        # vbox.Add(hbox1)
        #
        # hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        # l2 = wx.StaticText(panel, -1, "password")
        #
        # hbox2.Add(l2, 1, wx.ALIGN_LEFT | wx.ALL, 5)
        # self.t2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        # self.t2.SetMaxLength(5)
        #
        # hbox2.Add(self.t2, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        # vbox.Add(hbox2)
        # self.t2.Bind(wx.EVT_TEXT_MAXLEN, self.OnMaxLen)
        #
        # hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        # l3 = wx.StaticText(panel, -1, "Lines")
        #
        # hbox3.Add(l3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        # self.t3 = wx.TextCtrl(panel, size=(200, 100), style=wx.TE_MULTILINE)
        #
        # hbox3.Add(self.t3, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        # vbox.Add(hbox3)
        # self.t3.Bind(wx.EVT_TEXT_ENTER, self.OnEnterPressed)
        #
        # hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        # l4 = wx.StaticText(panel, -1, "ReadOnly")

        # hbox4.Add(l4, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        # self.t4 = wx.TextCtrl(panel, value="ReadOnly test", style=wx.TE_READONLY | wx.TE_CENTER)
        #
        # hbox4.Add(self.t4, 1, wx.EXPAND | wx.ALIGN_LEFT | wx.ALL, 5)
        # vbox.Add(hbox4)
        # panel.SetSizer(vbox)

app = wx.App()

win = wx.Frame(None,title="Remote Upgrade GPC OS Tool",size=(450,350))
panel = wx.Panel(win)

vbox = wx.BoxSizer(wx.VERTICAL)

hbox1 = wx.BoxSizer(wx.HORIZONTAL)
l1 = wx.StaticText(panel,-1,"Console IP:")
hbox1.Add(l1,1,wx.EXPAND|wx.LEFT|wx.ALL,5)

t1 = wx.TextCtrl(panel)
hbox1.Add(t1,1,wx.EXPAND|wx.LEFT|wx.ALL,5)

vbox.Add(hbox1)

hbox2 = wx.BoxSizer(wx.HORIZONTAL)
l2 = wx.StaticText(panel,-1,"Gantry IP:")
hbox2.Add(l2,1,wx.EXPAND|wx.LEFT|wx.ALL,5)

t2 = wx.TextCtrl(panel)
hbox2.Add(t2,1,wx.EXPAND|wx.RIGHT|wx.ALL,5)

vbox.Add(hbox2)

hbox3 = wx.BoxSizer(wx.HORIZONTAL)
l3 = wx.StaticText(panel,-1,"Gantry Mac:")
hbox3.Add(l3,1,wx.EXPAND|wx.LEFT|wx.ALL,5)

t3 = wx.TextCtrl(panel)
hbox3.Add(t3,1,wx.EXPAND|wx.RIGHT|wx.ALL,5)

vbox.Add(hbox3)

panel.SetSizer(vbox)
win.Show()

app.MainLoop()