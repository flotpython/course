# -*- coding: utf-8 -*-

from __future__ import print_function

############################################################
# the low level interface - used to be used directly in the first exercices

from IPython.display import HTML

from rendering import (
    Table, TableRow, TableCell, CellLegend,
    font_style, header_font_style,
    ok_style, ko_style,
    center_cell_style,
    truncate_value)

from log import log_correction

DEBUG=False
#DEBUG=True

########## defaults for columns widths - for FUN 
default_correction_columns =    (30, 40, 40)
default_exemple_columns =       (40, 40)

####################        
class ExerciceFunction(object):
    """The class for an exercice where students are asked to write a
    function The teacher version of that function is provided as
    'solution' and is used against datasets to generate an online
    correction or example.
    A dataset is an instance of Args (or ArgsKeywords)

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
    Finally render_name, if set to True, will cause the function name
    to appear in the first column together with arguments
    """
    def __init__(self, solution, datasets, 
                 correction_columns=None, exemple_columns=None,
                 exemple_how_many=1,
                 copy_mode='deep',
                 layout=None,
                 render_name=False):
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
        # applicable to all cells whose Args instance has not specified a layout
        self.layout = layout
        self.render_name = render_name

    # public interface
    def exemple(self):
        # the 'right' implementation
        how_many = self.exemple_how_many
        columns = self.exemple_columns if self.exemple_columns else default_exemple_columns
        exo_layout = self.layout

        how_many_samples = self.exemple_how_many if self.exemple_how_many \
                           else len(self.datasets)
    
        # can provide 3 args (convenient when it's the same as correction) or just 2
        columns = columns[:2]
        c1, c2 = columns

        table = Table(style=font_style)
        html = table.header()

        title1 = "Arguments" if not self.render_name else "Appel"
        html += TableRow(style=header_font_style,
                         cells = [ TableCell (CellLegend(x), tag='th', style=center_cell_style)
                                   for x in (title1, 'Résultat Attendu') ]).html()
        for dataset in self.datasets[:how_many_samples]:
            sample_dataset = dataset.clone(self.copy_mode)
            if self.render_name:
                sample_dataset.render_function_name(self.name)
            try:
                expected = sample_dataset.call(self.solution)
            except Exception as e:
                expected = e
            html += TableRow(cells = [ TableCell(sample_dataset, layout=self.layout, width=c1),
                                       TableCell(expected, layout=self.layout, width=c2)
                                   ]).html()
    
        html += table.footer()
        return HTML(html)

    def correction(self, student_function):
        """
        colums should be a 3-tuple for the 3 columns widths
        copy_mode can be either None, 'shallow', or 'deep' (default)
        """
        datasets = self.datasets
        copy_mode = self.copy_mode
        columns = self.correction_columns if self.correction_columns else default_correction_columns

        c1, c2, c3 = columns

        table = Table(style=font_style)
        html = table.header()
        
        title1 = "Arguments" if not self.render_name else "Appel"
        html += TableRow (
            cells = [ TableCell (CellLegend(x), tag='th', style=center_cell_style)
                      for x in ( title1, 'Attendu', 'Obtenu', '') ],
            style=header_font_style).html()
    
        overall = True
        for dataset in datasets:
            # will use original dataset for rendering to avoid any side-effects
            # during running
            if self.render_name:
                dataset.render_function_name(self.name)
            # always clone all inputs
            student_dataset = dataset.clone(copy_mode)
            ref_dataset = dataset.clone(copy_mode)
            
            # run both codes
            try:
                expected = ref_dataset.call(self.solution, debug=DEBUG)
            except Exception as e:
                expected = e

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
            html += TableRow(
                style = style,
                cells = [ TableCell(dataset, layout=self.layout, width=c1),
                          TableCell(expected, layout=self.layout, width=c2),
                          TableCell(student_result, layout=self.layout, width=c3),
                          TableCell(CellLegend(message))]
            ).html()

        log_correction(self.name, overall)
        html += table.footer()
        return HTML(html)

##############################
import re

class ExerciceRegexp(ExerciceFunction):
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
        ExerciceFunction.__init__(self, solution, inputs, *args, **keywords)
        self.regexp = regexp
        self.name = name

    def correction(self, student_regexp):
        student_solution = ExerciceRegexp.regexp_to_solution(student_regexp)
        return ExerciceFunction.correction(self, student_solution)

##############################
class ExerciceRegexpGroups(ExerciceFunction):
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
        ExerciceFunction.__init__(self, solution, inputs, *args, **keywords)
        self.name = name
        self.regexp = regexp
        self.groups = groups

    def correction(self, student_regexp):
        student_solution = ExerciceRegexpGroups.regexp_to_solution(student_regexp, self.groups)
        return ExerciceFunction.correction(self, student_solution)
