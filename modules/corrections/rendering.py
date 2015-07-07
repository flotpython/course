# -*- coding: utf-8 -*-

from __future__ import print_function

import pprint

from types import StringTypes, FunctionType, BuiltinFunctionType, BuiltinMethodType

########## styles in html output
font_style = 'font-family:monospace;font-size:small;'
header_font_style = 'font-family:monospace;font-size:medium;'

# iteration 1 was using this
#ok_style = 'background-color:#66CC66;'
#ko_style = 'background-color:#CC3300;color:#e8e8e8;'
ok_style = 'background-color:#d6e9ce;'
ko_style = 'background-color:#efd6d6;'

center_cell_style = 'text-align: center;'
left_cell_style = 'text-align: left;'
right_cell_style = 'text-align: right;'
########## helpers for rendering / truncating
def html_escape(s):
    return s
    # xxx need to find code for < and >
    return s.replace("<", "&lt;").replace(">", "&gt;").replace("&", "&amp;")

def truncate_str(message, max_size):
    # width = 0 or less means do not truncate
    if max_size <= 0:
        return message
    truncated = message if len(message) <= max_size \
        else message[:max_size-3]+'...'
    return html_escape(truncated)

# display functions as their name
def custom_repr(x):
    if isinstance(x, (FunctionType, BuiltinFunctionType, BuiltinMethodType)):
        return x.__name__
    elif isinstance(x, set):
        return "{" + commas(x) + "}"
    else:
        return repr(x)

def commas(iterable):
    if isinstance(iterable, dict):
        return ", ".join(["{}={}".format(k,custom_repr(v)) for k,v in iterable.items()])
    elif isinstance(iterable, str): 
        return str
    else:
        return ", ".join([custom_repr(x) for x in iterable])

def truncate_value(value, width):
    # this is the case where we may have a set and prefer to show it with {}
    if isinstance(value, set):
        message = "{" + commas(value)
        return truncate_str(message, width-1) + "}"
    else:
        return truncate_str(repr(value), width)

########## rendering usual objects (not Args or ArgsKeywords)
class CellObj(object):
    def __init__(self, torender):
        self.torender = torender
    def layout_truncate(self, width):
        return truncate_value(self.torender, width)
    def layout_multiline(self, width):
        torender = self.torender
        if isinstance(torender, StringTypes):
            html = "<pre>"
            for line in torender.split("\n"):
                html += truncate_value(line, width) + "\n"
            html += "</pre>"
            return html
        else:    
            #print("multiline on CellObj -> truncate")
            return self.layout_truncate(width)
    def layout_pprint(self, width):
        indent = 2
        html = "<pre>\n"
        width = width if width >0 else 80
        html += pprint.pformat(self.torender, indent=indent, width=width)
        html += "</pre>"
        return html

    def layout_text(self, width, show_backslash_n=False):
        """
        torender is expected to be a plain string on multiple lines
        WARNING: with this layout, width is expected to be a font size
        """
        style = "font-size:{};".format(width)
        html = "<pre 'style={}'>".format(style)
        contents = str(self.torender)
        if not show_backslash_n:
            html += contenst.torender
        else:
            html += contents.replace("\n", "\\n\n")
        html += "</pre>"
        return html

    def layout_text_backslash_n(self, width):
        """
        Same as layout_text but with \n at the end of lines
        """
        return self.layout_text(width, show_backslash_n=True)
    
class CellLegend(object):
    def __init__(self, legend):
        self.legend = legend
    def __repr__(self):
        return "<CellLegend {}>".format(self.legend)
    def layout_truncate(self, width):
        return truncate_str(self.legend, width)
    layout_multiline = layout_truncate
    layout_pprint = layout_truncate

########## html tags
# create a start tag with arbitrary attributes
# tag_keywords('table', style='text-align:center') to get
# <table style='text-align:center'>
# special case for 'class' that is a python keyword
# use hclass instead
# use e.g. tag_keywords('tr', hclass='error') to get
# <table class='error'>
def tag_keywords(tag, **html_tags):
    html = "<{}".format(tag)
    for k,v in html_tags.items():
        # ignore stuff that is defined by default as None
        if v is None:
            continue
        html += " {}='{}'".format(k if k != 'hclass' else 'class', v)
    html += ">"
    return html

# end_tag('table') -> </table>
def end_tag(tag):
    return "</{}>".format(tag)

##############################
class Table(object):
    def __init__(self, **html_tags):
        self.html_tags = html_tags
    def header(self):
        return tag_keywords("table", **self.html_tags)
    def footer(self):
        return end_tag("table")

class TableRow(object):
    def __init__(self, cells, **html_tags):
        self.cells = cells
        self.html_tags = html_tags

    def html(self):
        html = tag_keywords("tr", **self.html_tags)
        for cell in self.cells:
            html += cell.html()
        html += end_tag("tr")
        return html

class TableCell(object):
    """
    Something that will produce a table cell, based on 
    (*) a content, that is expected to have the right 
        layout method, like e.g. layout_truncate 
        since truncate is our default layout
        this typically applies to Args-like objects
        otherwise, a CellObj object is created instead
    (*) a width, 0 meaning no truncation/formatting occurs
    (*) a layout
    (*) a tag, default is 'td' but can be 'th'
    (*) additional html tags can be set using **html_tags
    """
    def __init__(self, content, width=0, tag='td', layout='truncate', **html_tags):
        self.content = content
        self.width = width
        self.tag = tag
        self.layout = layout
        self.html_tags = html_tags

    # if the 'content' object has a 'render' method, then use it
    # otherwise provide a few basic methods for that
    def html(self):
        html = tag_keywords(self.tag, **self.html_tags)
        layout = self.computed_layout()
        symbol = 'layout_{}'.format(layout)
        try:
            if hasattr(self.content, symbol):
                method = getattr(self.content, symbol)
                cell_html = method(self.width)
                html += cell_html
            else:
                proxy = CellObj(self.content)
                method = getattr(proxy, symbol)
                html += method(self.width)
        except:
            import traceback
            traceback.print_exc()
            html += "TableCell.html({})".format(self.content)
        html += end_tag(self.tag)
        return html


    # several layouts for rendering in a table
    # the default is for when this is left unspecified
    # or means something we cannot do
    default_layout = 'truncate'
    supported_layouts = [
        'truncate', 'multiline', 'pprint',
        'void', 'text', 'text_backslash_n',
    ] 

    def computed_layout(self):
        """
        the layout to use
        the one specified in self.content.layout, if it exists
        takes precedence over self.layout
        """
        # the value specified in the instance wins if set
        # as it is more specific
        # second use the one provided at the exercice level
        # last resort is this default
        computed_layout = None
        if hasattr(self.content, 'layout'):
            computed_layout = self.content.layout
        if computed_layout is None and self.layout:
            computed_layout = self.layout
        if computed_layout is None:
            computed_layout = self.default_layout
        if computed_layout not in self.supported_layouts:
            print("WARNING: unsupported layout {}".format(computed_layout))
            computed_layout = self.default_layout
        return computed_layout


if __name__ == '__main__':
    size = 'small'
    inputs = [ "abc\ndef" ]
    for input in inputs:
        cell = CellObj(input)
        print("----------input [[{}]]".format(input))
        print("----------text [[{}]]".format(cell.layout_text(size)))
        print("text_backslash_n [[{}]]".format(cell.layout_text_backslash_n(size)))
            
