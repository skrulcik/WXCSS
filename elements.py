import wx
import stylesheet

class App(wx.App):
    def __init__(self, css_file, redirect=False, filename=None, useBestVisual=False, clearSigInt = True):
        super(App, self).__init__(redirect, filename, useBestVisual, clearSigInt)
        self.stylesheet = stylesheet.WXStyleSheet(css_file)


class Frame(wx.Frame):
    def __init__(self, parent, id=-1, title="WXCSS Frame", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name="Frame"):
        super(Frame, self).__init__(parent, id, title, pos, size, style, name)
        self.token = 'body'
        self.style = wx.GetApp().stylesheet
        self.configure_style()
    
    def configure_style(self):
        self.style.apply_rules(self)

class StaticText(wx.StaticText):
    def __init__(self, parent, id=-1, label="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=0, name=wx.StaticTextNameStr):
        super(StaticText, self).__init__(parent, id, label, pos, size, style, name)
        self.token = 'p'
        if parent:
            self.token = parent.token + self.token
        self.style = wx.GetApp().stylesheet
        self.configure_style()

    def configure_style(self):
        self.style.apply_rules(self)

class Panel(wx.Panel):
    def __init__(self, parent, id=-1, pos=wx.DefaultPosition, size=wx.DefaultSize, style= wx.TAB_TRAVERSAL | wx.NO_BORDER, name= wx.PanelNameStr):
        super(Panel, self).__init__(parent, id, pos, size, style, name)
        self.token = 'div'
        if parent:
            self.token = parent.token + self.token
        self.style = wx.GetApp().stylesheet
        self.configure_style()
    def configure_style(self):
        self.style.apply_rules(self)




