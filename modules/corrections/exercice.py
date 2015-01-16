# -*- coding: utf-8 -*-

from __future__ import print_function

############################################################
# the low level interface - used to be used directly in the first exercices

from IPython.display import HTML
import traceback
import copy
from types import FunctionType, BuiltinFunctionType, BuiltinMethodType

# for logging
import os
import os.path
import time

DEBUG=False
#DEBUG=True

########## helpers for rendering / truncating
def html_escape(s):
    return s
    # xxx need to find code for < and >
    return s.replace("<", "&lt;").replace(">", "&gt;").replace("&", "&amp;")

def truncate_str(message, max_size):
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

########## styles in html output
font_style = 'font-family:monospace;font-size:small;'
header_font_style = 'font-family:monospace;font-size:medium;'

ok_style = 'background-color:#66CC66;'
ko_style = 'background-color:#CC3300;color:#e8e8e8;'

# defaults for columns widths - for FUN 
default_correction_columns =    (30, 40, 40)
default_exemple_columns =       (40, 40)

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

    def call(self, function, debug=False):
        if debug:
            print("calling", function.__name__, "*", self.args, "**", self.keywords)
        return function(*self.args, **self.keywords)

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
    supported_formats = ['truncate', 'multiline', 'plain'] 

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

    def render_cell(self, exo, width):
        """ 
        return html for rendering in a table cell
        multiplexes to mathod render_<format> depending on
        this instance's format and the one specified in the exercice
        (former hs priority if set)
        """
        exo_format = exo.format
        actual_format = self.actual_format(exo_format)
        method = getattr(self, 'render_' + actual_format)
        # the magic of bound methods !
        return method(exo.name, width)

    def render_plain(self, function_name, width):
        """
        single line - not truncated
        """
        text = commas(self.args)
        if self.keywords:
            text += ", " + commas(self.keywords)
        return text

    def render_truncate(self, function_name, width):
        """
        render a list of arguments on a single line, truncated
        """
        return truncate_str(self.render_plain(function_name, width), width)
    
    def render_multiline(self, function_name, width):
        """
        render a list of arguments in multiline mode
        """
        raw_lines = list(self.args) + [ "{}={}".format(k,v) for k,v in self.keywords ]
        lines = [ truncate_value(line, width) for line in raw_lines ]
        rendered_args = ",<br/>".join(lines)
        return "{}(<br/>{}<br/>)".format(function_name, rendered_args)

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

####################        
class Exercice:
    """The class for an exercice where students are asked to write a
    function The teacher version of that function is provided as
    'solution' and is used against datasets - a list of Args (or
    ArgsKeywords) to generate an online correction.

    The most useful method in this class is 'correction'; for each
    input in the dataset, we call both the teacher function and the
    student function, and compare the results using '==' to produce a
    table of green or red cells.

    The class provides a few other utility methods, like 'exemple'
    that can be used in the students notebook to show the expected
    result for some or all of the inputs.

    One important aspects of this is copying. Realizing that both
    teacher and student functions can do side effects in the inputs,
    it means that these need to be copied before any call is made. By
    default the copy is a deep copy, but for some corner cases it can
    be required to use shallow copy instead; in this case just pass
    copy_mode='shallow' to the constructor here.

    Some more cosmetic settings are supported as well, for defining
    the column widths in both the correction and exemple outputs. Also
    exemple_how_many allows you to specify how many inputs should be
    considered for generating the exemple table (starting of course at
    the top of the list).
    """
    def __init__(self, solution, datasets, 
                 correction_columns=None, exemple_columns=None,
                 exemple_how_many=1,
                 copy_mode='deep',
                 format=None):
        # the 'official' solution
        self.solution = solution
        # the inputs 
        self.datasets = datasets
        # in some weird cases this won't exist
        self.name = getattr(solution, '__name__', "no_name")
        self.correction_columns = correction_columns 
        self.exemple_columns = exemple_columns 
        self.exemple_how_many = exemple_how_many
        self.copy_mode = copy_mode
        self.format = format

    # public interface
    def exemple(self):
        # the 'right' implementation
        how_many = self.exemple_how_many
        columns = self.exemple_columns if self.exemple_columns else default_exemple_columns
        exo_format = self.format

        how_many_samples = self.exemple_how_many if self.exemple_how_many \
                           else len(self.datasets)
    
        # can provide 3 args (convenient when it's the same as correction) or just 2
        columns = columns[:2]
        c1, c2 = columns

        html = ""
        html += u"<table style='{}'>".format(font_style)
        html += u"<tr style='{}'><th>Arguments</th>"\
                u"<th>Résultat attendu</th></tr>".format(header_font_style)
        
        for dataset in self.datasets[:how_many_samples]:
            sample_dataset = dataset.clone(self.copy_mode)
            rendered_input = sample_dataset.render_cell(self, width=c1)
            try:
                expected = sample_dataset.call(self.solution)
            except Exception as e:
                expected = e
            rendered_expected = truncate_value(expected, c2)
            html += "<tr><td>{}</td><td>{}</td></tr>".format(rendered_input, rendered_expected)
    
        html += "</table>"
        return HTML(html)

    def correction(self, student_function):
        """
        colums should be a 3-tuple for the 3 columns widths
        copy_mode can be either None, 'shallow', or 'deep' (default)
        """
        datasets = self.datasets
        copy_mode = self.copy_mode
        columns = self.correction_columns
        if columns is None: columns = default_correction_columns

        c1,c2,c3 = columns
        html = ""
        html += u"<table style='{}'>".format(font_style)
        html += u"<tr style='{}'><th>Arguments</th><th>Attendu</th>"\
                u"<th>Obtenu</th><th></th></tr>".format(header_font_style)
    
        overall = True
        for dataset in datasets:
            # always clone all inputs
            student_dataset = dataset.clone(copy_mode)
            correct_dataset = dataset.clone(copy_mode)
            # compute rendering of dataset *before* running
            #in case there are side-effects
            rendered_input = student_dataset.render_cell(self, width=c1)
            
            # run both codes
            try:
                expected = correct_dataset.call(self.solution, debug=DEBUG)
            except Exception as e:
                expected = e
            rendered_expected = truncate_value(expected, c2)
            try:
                student_result = student_dataset.call(student_function, debug=DEBUG)
            except Exception as e:
                student_result = e
    
            # compare results
            ok = expected == student_result
            if not ok:
                overall = False
            # render that run
            result_cell = '<td style="background-color:green;">'
            message = 'OK' if ok else 'KO'
            style = ok_style if ok else ko_style
            html += "<tr style='{}'>".format(style)
            html += "<td>{}</td><td>{}</td><td>{}</td><td>{}</td>".\
                    format(rendered_input,
                           rendered_expected,
                           truncate_value(student_result, c3),
                           message)
        html += "</table>"
        self.log_correction(overall)
        return HTML(html)

    def log_correction(self, success):
        try:
            uid = os.getuid()
            md5 = os.path.basename(os.path.normpath(os.getenv("HOME")))
            now = time.strftime("%D-%H:%M", time.localtime())
            logname = os.path.join(os.getenv("HOME"), ".correction")
            message = "OK" if success else "KO"
            function_name = self.name
            with open(logname, 'a') as log:
                line = "{now} {uid} {md5} {function_name} {message}\n".format(**locals())
                log.write(line)
        except:
            pass


##############################
# this one is about providing a slightly different layout
# it is used only for exercice 'intersect' so it is probably not
# worth worrying too much about it
class Exercice_multiline(Exercice):
    def exemple(self):
        columns = self.exemple_columns
        if columns is None: columns = default_exemple_columns
        return exemple_table_multiline(self.name, self.solution, 
                                       self.datasets, columns=columns)


##############################
import re

class ExerciceRegexp(Exercice):
    """
    With these exercices the students are asked to write a regexp
    which is transformed into a function that essentially
    takes an input string and returns a boolean
    that says if the *whole* string matches or not
    """
    @staticmethod
    def regexp_to_solution(regexp):
        def solution(string):
            match = re.match(regexp, string)
            if not match:       return False
            else:               return match.group(0) == string
        return solution

    def __init__(self, name, regexp, inputs, *args, **keywords):
        solution = ExerciceRegexp.regexp_to_solution(regexp)
        Exercice.__init__(self, solution, inputs, *args, **keywords)
        self.regexp = regexp
        self.name = name

    def correction(self, student_regexp):
        student_solution = ExerciceRegexp.regexp_to_solution(student_regexp)
        return Exercice.correction(self, student_solution)

##############################
class ExerciceRegexpGroups(Exercice):
    """
    With these exercices the students are asked to write a regexp
    with a set of specified named groups
    a list of these groups needs to be passed to construct the object

    the regexp is then transformed into a function that again
    takes an input string and either a list of tuples 
    (groupname, found_substring) 
    or None if no match occurs
    """

    @staticmethod
    def extract_group(match, group):
        try:        return group, match.group(group)
        except:     return group, "Undefined"

    @staticmethod
    def regexp_to_solution(regexp, groups):
        def solution(string):
            match = re.match(regexp, string)
            return match and [ExerciceRegexpGroups.extract_group(match,group) for group in groups]
        return solution

    def __init__(self, name, regexp, groups, inputs, *args, **keywords):
        solution = ExerciceRegexpGroups.regexp_to_solution(regexp, groups)
        Exercice.__init__(self, solution, inputs, *args, **keywords)
        self.name = name
        self.regexp = regexp
        self.groups = groups

    def correction(self, student_regexp):
        student_solution = ExerciceRegexpGroups.regexp_to_solution(student_regexp, self.groups)
        return Exercice.correction(self, student_solution)
