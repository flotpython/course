# -*- coding: utf-8 -*-

from __future__ import print_function

from types import FunctionType, BuiltinFunctionType, BuiltinMethodType

########## styles in html output
font_style = 'font-family:monospace;font-size:small;'
header_font_style = 'font-family:monospace;font-size:medium;'

ok_style = 'background-color:#66CC66;'
ko_style = 'background-color:#CC3300;color:#e8e8e8;'

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

def truncate_value(value, max_size):
    # this is the case where we may have a set and prefer to show it with {}
    if isinstance(value, set):
        message = "{" + commas(value)
        return truncate_str(message, max_size-1) + "}"
    else:
        return truncate_str(repr(value), max_size)

########## html tags
# create a start tag with arbitrary attributes
# tag_keywords('table', style='text-align:center') to get
# <table style='text-align:center'>
# special case for 'class' that is a python keyword
# use hclass instead
# use e.g. tag_keywords('tr', hclass='error') to get
# <table class='error'>
def tag_keywords(tag, **keywords):
    html = "<{}".format(tag)
    for k,v in keywords.items():
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
    def __init__(self, **keywords):
        self.keywords = keywords
    def header(self):
        return tag_keywords("table", **self.keywords)
    def footer(self):
        return end_tag("table")

class TableRow(object):
    def __init__(self, cells, **keywords):
        self.cells = cells
        self.keywords = keywords

    def render(self):
        html = tag_keywords("tr", **self.keywords)
        for cell in self.cells:
            html += cell.render()
        html += end_tag("tr")
        return html

class TableCell(object):
    def __init__(self, content, tag='td', format='truncate', **keywords):
        self.content = content
        self.tag = tag
        self.format = format
        self.keywords = keywords

    # if the 'content' object has a 'render' method, then use it
    # otherwise provide a few basic methods for that
    def render(self):
        if hasattr(self.content, 'render'):
            cell = self.content.render(self.format)
        else:
            ### should plug the currently available formats
            cell = str(self.content)
        html = tag_keywords(self.tag, **self.keywords)
        html += cell
        html += end_tag(self.tag)
        return html

