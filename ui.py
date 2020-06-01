# First things, first. Import the wxPython package.
import wx, wx.xrc
import os
import vlc
directory = '/home/pydev/Music/kimba'

def getTracksList():
    return [os.fsdecode(file) for file in os.listdir(directory)]

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_toolBar1 = self.CreateToolBar(wx.TB_HORIZONTAL, wx.ID_ANY)
        self.m_staticText2 = wx.StaticText(self.m_toolBar1, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText2.Wrap(-1)

        self.m_toolBar1.AddControl(self.m_staticText2)
        self.m_button12 = wx.Button(self.m_toolBar1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_toolBar1.AddControl(self.m_button12)
        self.m_dirPicker1 = wx.DirPickerCtrl(self.m_toolBar1, wx.ID_ANY, wx.EmptyString, u"/home/pydev/Music/salsa/",
                                             wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        self.m_toolBar1.AddControl(self.m_dirPicker1)
        self.m_toolBar1.Realize()

        self.m_statusBar1 = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.SetStatusText("Welcome to wxPython!")
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        m_listBox2Choices = getTracksList()
        self.m_listBox2 = wx.ListBox(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox2Choices, 0)
        bSizer5.Add(self.m_listBox2, 0, wx.ALL, 5)

        self.m_panel1.SetSizer(bSizer5)
        self.m_panel1.Layout()
        bSizer5.Fit(self.m_panel1)
        bSizer3.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


# Next, create an application object.
app = wx.App()

# Then a frame.
frm = MyFrame1(None)
frm.Maximize()

# Show it.
frm.Show()

p = vlc.MediaPlayer("file:///home/pydev/Music/salsa/salsa-the wolf-la loba.mp3")
# p.play()
# Start the event loop.
print()
app.MainLoop()
