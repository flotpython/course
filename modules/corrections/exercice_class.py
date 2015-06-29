# -*- coding: utf-8 -*-

from __future__ import print_function

from IPython.display import HTML

from rendering import (Table, TableRow, TableCell,
                       font_style, header_font_style,
                       ok_style, ko_style)

from exercice import log_correction

default_correction_columns = 40, 30, 30

class ScenarioClass(list):
    """
    Describes a scenario that can be applied to a class

    Typically we want to create an instance (using some args),
    and then run some methods (still with some args)

    So a class scenario in its simpler form is defined as a list
    of couples of the form 
    ( method_name, Args_object )
    """

    def __init__(self):
        list.__init__(self)

    def set_init_args(self, args):
        if self and self[0][0] == '__init__':
            print("Only one __init__ step is allowed")
            return
        self.insert(0, ('__init__', args))

    def add_step (self, methodname, args):
        self.append( (methodname, args,) )

class ExerciceClass(object):
    """
    Much like the Exercice class, this allows to define
    an exercice as
    (*) a solution which is the correct implementation of a class
    (*) a list of scenarios that will be executed on that class
    """
    
    def __init__(self, solution, scenarios, format=None):
        self.solution = solution
        self.scenarios = scenarios
        # in some weird cases this won't exist
        self.name = getattr(solution, '__name__', "no_name")
        # applicable to all cells whose Args instance has not specified a format
        self.format = format

    def correction (self, student_class):

        overall = True

        # should be customizable
        columns = default_correction_columns
        c1, c2, c3 = columns
        
        table = Table(style=font_style)

        html = table.header()
        
        #html = ""
        #html += u"<table style='{}'>".format(font_style)
    
        ref_class = self.solution
        #print("Solution = {}".format(self.solution))
        #print("Student class = {}".format(student_class))
        for i, scenario in enumerate(self.scenarios):
            # skip empty scenarios
            if not scenario: continue
            
            # first step has to be a constructor
            methodname, args = scenario[0]
            args.render_function_name(ref_class.__name__)
            if methodname != '__init__':
                cells = [ TableCell("Error in scenario - first step must be a constructor",
                                    tag='th',
                                    colspan=4,
                                    hclass='error') ]
                html += TableRow(cells=cells).render()
                continue

            # start of scenario
            line_text = "Scenario {}".format(i+1)
            html += TableRow(cells=[TableCell(line_text, colspan=4, tag='th',
                                              style='text-align:center')],
                             style=header_font_style).render()
            cells = [ TableCell(x, tag='th') for x in ('Appel', 'Attendu', 'Obtenu','')]
            html += TableRow(cells = cells).render()

            # initialize both objects
            #constructor = args.render_cell(ref_class.__name__, self.format, c1+c2+c3 )
            try:
                objects = [ args.init_obj(klass) for klass in (ref_class, student_class) ]
                cells = [ TableCell(x) for x in (args, '-', '-','OK')]
                html += TableRow(cells=cells, style=ok_style).render()
            except Exception as e:
                cell1 = TableCell(args, colspan=2)
                error = "Exception {}".format(e)
                cell2 = TableCell(error)
                cell3 = TableCell('KO')
                html += TableRow(cells=(cell1, cell2), style=ko_style).render()
                overall = False
                continue
            
            # other steps of that scenario
            for methodname, args in scenario[1:]:
                # so that we display the function name
                args.render_function_name(methodname)
                #print("dealing with step {} - {}".format(methodname, args))
                # xxx TODO : what if student's code raises an exception
                result = [ args.call_obj(o, methodname) for o in objects ]
                if result[0] == result[1]:
                    style = ok_style
                    msg = 'OK'
                else:
                    style = ko_style
                    msg = 'KO'
                    overall = False
                cells = (TableCell(args), TableCell(result[0]),
                         TableCell(result[1]), TableCell(msg))
                html += TableRow (cells=cells, style=style).render()

        log_correction(self.name, overall)

        html += "</table>"

        return HTML(html)
