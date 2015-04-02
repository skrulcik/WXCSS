from elements import *
import elements as wx
import os

def main():
    app = wx.App('/Users/Scott/Documents/WXCSS/style.css')
    
    frm = wx.Frame(None)
    frm.Show()
    
    div = wx.Panel(frm)
    lbl = wx.StaticText(div, label="This should say something")

    app.MainLoop()

if __name__ == '__main__':
    main()