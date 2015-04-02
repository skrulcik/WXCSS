from elements import *
import elements as wx
import os

def main():
    app = wx.App('/Users/Scott/Documents/WXCSS/style.css')
    
    frm = wx.Frame(None)
    frm.Show()
    
    lbl = wx.StaticText(frm, label="This should say something")

    app.MainLoop()

if __name__ == '__main__':
    main()