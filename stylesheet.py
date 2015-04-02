import tinycss
import wx
import css_util

class WXStyleSheet:
    def __init__(self, source=None):
        self.source = source
        self.stylesheet = None
        self.parse_source()
        self.update = {"background-color": self.background_color,
                        "color": self.color,
                        "width": self.width,
                        "height": self.height}
    
    
    def parse_source(self):
        if self.source != None:
            parser = tinycss.make_parser('page3')
            self.stylesheet = parser.parse_stylesheet_file(self.source)

# Naive implementation here, fix with a graph of some sort
    def rule_for(self, selector):
        declarations = []
        for rule in self.stylesheet.rules:
            for sel in rule.selector:
                if sel.as_css() in selector:
                    declarations += rule.declarations
        return declarations

    def apply_rules(self, w):
        for attr in w.style.rule_for(w.token):
            self.update[attr.name](w,attr.value) #"value" is a token list

    ############################################################################
    #################   Actually implementing CSS Style   ######################
    ############################################################################

    # Color
    # --------------------------------------------------------------------------
    def background_color(self, target, value):
        for token in value:
            if token.type == "HASH":
                r,g,b = css_util.hex_to_rgb(token.value)
                target.SetBackgroundColour(wx.Colour(r,g,b))
    def color(self, target, value):
        for token in value:
            if token.type == "HASH":
                r,g,b = css_util.hex_to_rgb(token.value)
                target.SetForegroundColour(wx.Colour(r,g,b))

    # Size
    # --------------------------------------------------------------------------
    def width(self, target, value):
        pass

    def height(self, target, value):
        pass






