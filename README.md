# WXCSS
Style a WXPython application with CSS files

### Usage

1. Replace `import wx` with `import elements as wx` at the top of your file.
2. Replace `wx.App()` with `wx.App(<path/to/file.css>)`

Now you're ready! Currently, the following attributes are currently supported:
- [x] `color`
- [x] `background-color`
- [x] `width`
- [x] `height`

... more to come! Please contribute. If you want to add attributes, edit the Stylesheet class. Add functions to the dictiionary `update`. Each function you write should expect a target and a token list.
