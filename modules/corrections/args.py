# -*- coding: utf-8 -*-

from __future__ import print_function

import copy

from rendering import commas, truncate_str, truncate_value

####################
class ArgsKeywords(object):
    """
    The most general form of a function argument list is made
    of a tuple and a dictionary
    
    Example:
    my_input = ArgsKeywords( (1,2), {'a': []})
    my_input.call (foo)
    would then return the result of
    foo (1, 2, a=[])
    """
    def __init__(self, args=None, keywords=None, format=None):
        # expecting a tuple or a list
        self.args = args if args is not None else tuple()
        # expecting a dictionary
        self.keywords = keywords if keywords is not None else {}
        # used when rendering - in exemple or correction
        # in general this is defined in the Exercice instance
        # but can also be overridden here
        self.format=format
        # can be overridden later on using 'render_function_name'
        self.function_name = None

    def __repr__(self):
        cn = "Args" if not self.keywords else "ArgsKeywords"
        result = "<Args {} ".format(self.args)
        if self.keywords:
            result += "Keywords:" + ",".join(["{}={}".format(k, v) for (k, v) in self.keywords.items() ])
        result += ">"
        return result

    def call(self, function, debug=False):
        if debug:
            print("calling {} *{} **{}".format(function.__name__, self.args, self.keywords))
        return function(*self.args, **self.keywords)

    def init_obj(self, klass, debug=False):
        if debug:
            print("creating object in class {}, *{} **{}"
                  .format(klass.__name__, self.args, self.keywords))
        return klass(*self.args, **self.keywords)
                  
    def call_obj(self, object, methodname, debug=False):
        if debug:
            print("calling method {} on object {} *{} **{}"
                  .format(methodname, object, self.args, self.keywords))
        method = getattr(object, methodname)
        return method(*self.args, **self.keywords)
                  
    def clone(self, copy_mode):
        "clone this input for safety"
        if copy_mode == 'shallow':
            return copy.copy(self)
        elif copy_mode == 'deep':
            return copy.deepcopy(self)
        else:
            return self

    # several formats for rendering in a table
    # the default is for when this is left unspecified
    # both in the Exercice instance and in the ArgsKeywords instance
    default_format = 'truncate'
    supported_formats = ['truncate', 'multiline'] 

    def actual_format(self, exo_format):
        "the format to use"
        # the value specified in the instance wins if set
        # as it is more specific
        # second use the one provided at the exercice level
        # last resort is this default
        actual_format = self.format if self.format \
           else exo_format if exo_format \
                else self.default_format
        if actual_format not in self.supported_formats:
            print("WARNING: unsupported format {}".format(actual_format))
            actual_format = self.default_format
        return actual_format

    def render_function_name(self, function_name):
        """
        if called, arguments will be rendered like this
        function_name (arg1, ... argn)
        instead of just
        arg1, .. argn
        """
        self.function_name = function_name
        
    # tmp - glue with rendering     
    def render(self, format):
        return self.render_cell(format, 0)

    def render_cell(self, exo_format, width):
        """ 
        return html for rendering in a table cell
        multiplexes to method render_<format> depending on
        this instance's format and the one specified in the exercice
        (former hs priority if set)
        """
        actual_format = self.actual_format(exo_format)
        method = getattr(self, 'render_' + actual_format)
        # the magic of bound methods !
        return method(width)

    def render_truncate(self, width):
        """
        render a list of arguments on a single line, truncated
        remember that width <= 0 means no truncation
        """
        text = commas(self.args)
        if self.function_name:
            text = "{}({})".format(self.function_name, text)
        if self.keywords:
            text += ", " + commas(self.keywords)
        return truncate_str(text, width)
    
    def render_multiline(self, width):
        """
        render a list of arguments in multiline mode
        """
        raw_lines = list(self.args) + [ "{}={}".format(k,v) for k,v in self.keywords ]
        lines = [ truncate_value(line, width) for line in raw_lines ]
        rendered_args = ",<br/>".join(lines)
        if not self.function_name:
            return rendered_args
        else:
            return "{}(<br/>{}<br/>)".format(function_name, rendered_args)

# simplified for when no keywords are required
class Args(ArgsKeywords):
    """
    In most cases though, we do not use keywords so it is more convenient to
    just pass a list of arguments

    Example:
    my_input = Args (1, 2, 3)
    my_input.call(foo)
    would then return the result of
    foo(1, 2, 3)

    it is possible to specify format=multiline if desired,
    but it MUST be a named parameter of course
    """
    def __init__(self, *args, **kwds):
        # it is NOT *args here, this is intentional
        ArgsKeywords.__init__(self, args, **kwds)

