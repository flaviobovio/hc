import wx
import locale
from MainFrame import MainFrame


class Gestion(wx.App):
   
    def OnInit(self):
        #locale.setlocale(locale.LC_NUMERIC, "en_US.UTF-8")     
            
        
        self.m_frame = MainFrame(None)
        self.m_frame.Show()
        self.SetTopWindow(self.m_frame)
        return True

app = Gestion(0)
app.MainLoop()
