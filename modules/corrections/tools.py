# -*- coding: iso-8859-15 -*-
from IPython.display import HTML
import traceback
import copy
from types import FunctionType, BuiltinFunctionType, BuiltinMethodType

########## helpers
def truncate (data, max_size=10):
    message = "{}".format(repr(data))
    return message if len(message) <= max_size \
        else message [:max_size-3]+'...'

# display functions as their name
def custom_repr (x):
    if isinstance (x,(FunctionType, BuiltinFunctionType, BuiltinMethodType)):
        return x.__name__
    else:
        return repr(x)

def html_escape (s):
    # xxx need to find code for < and >
    return s.replace("<","&28;")

def _truncate_list (data_list, max_size):
    message = ", ".join([custom_repr(x) for x in data_list])
    return message if len(message) <= max_size \
        else message [:max_size-3]+'...'

def truncate_list (data, max_size=10):
    if isinstance (data,set):
        return "{"+_truncate_list(data,max_size-2)+"}"
    else:
        return _truncate_list (data, max_size)

# safer to copy inputs most of the time (always?)
def clone_dataset (dataset, copy_mode):
    if copy_mode == 'shallow':
        return copy.copy(dataset)
    elif copy_mode == 'deep':
        return copy.deepcopy(dataset)
    else:
        return dataset

########## 
# when the function only has one arg it is much easier to give a list of inputs 
# instead of a list of tuples or arguments - especially as this results in 1-arg tuple
# so the comma is required
def correction_table_1arg (student_function, correct_function, args, *l, **k):
    datasets = [ (arg,) for arg in args ]
    return correction_table (student_function, correct_function, datasets, *l, **k)


########## styles in html output
font_style='font-family:monospace;'

ok_style='background-color:#66CC66;'
ko_style='background-color:#CC3300;color:#e8e8e8;'
default_table_columns = (30, 40, 40)

def correction_table (student_function,
                      correct_function,
                      datasets,
                      columns = default_table_columns,
                      copy_mode = 'deep'):
    """
    colums should be a 3-tuple for the 3 columns widths
    copy_mode can be either None, 'shallow', or 'deep' (default)
    """
    c1,c2,c3 = columns
    html = ""
    html += u"<table style='{}'>".format(font_style)
    html += u"<tr><th>Entrée</th><th>Attendu</th><th>Obtenu</th><th></th></tr>"

    for dataset in datasets:
        student_dataset = clone_dataset (dataset, copy_mode)
        correct_dataset = clone_dataset (dataset, copy_mode)
        # compute rendering of dataset *before* running in case there are side-effects
        rendered_input = html_escape(truncate_list(student_dataset,c1))
        expected = apply (correct_function, correct_dataset)
        rendered_expected = truncate (expected, c2)
        # run both codes
        try:
            student_result = apply (student_function, student_dataset)
        except Exception as e:
            student_result = e
#        print 'expected',expected
#        print 'student_result',student_result
        # compare 
        ok = expected == student_result
        # render that run
        result_cell = '<td style="background-color:green;">'
        message = 'OK' if ok else 'KO'
        style = ok_style if ok else ko_style
        html += "<tr style='{}'>".format(style)
        html += "<td>{}</td><td>{}</td><td>{}</td><td>{}</td>".\
                format(rendered_input,rendered_expected,
                       truncate(student_result,c3),message)
    html += "</table>"
    return HTML(html)

# like with correction_table_1arg: pass a list of the arguments, not tuples
def exemple_table_1arg (function_name, correct_function, args, *l, **kwds):
    datasets = [ (arg,) for arg in args ]
    return exemple_table (function_name, correct_function, datasets, *l, **kwds)

# see how to use in exo_rendering.py
def exemple_table (function_name,
                   correct_function,
                   datasets,
                   columns = default_table_columns,
                   copy_mode = 'deep',
                   how_many=1):

    if how_many == 0:
        how_many=len(datasets)

    # can provide 3 args (convenient when it's the same as correction) or just 2
    columns = columns[:2]
    c1,c2 = columns
    html = ""
    html += u"<table style='{}'>".format(font_style)
    html += u"<tr><th>Appel</th><th>Résultat attendu</th></tr>"
    
    for dataset in datasets [:how_many]:
        sample_dataset = clone_dataset (dataset, copy_mode)
        rendered_input = "{}({})".format(function_name,truncate_list(sample_dataset,c1))
        expected = apply (correct_function, sample_dataset)
        rendered_expected = truncate (expected, c2)
        html += "<tr><td>{}</td><td>{}</td></tr>".format(rendered_input,rendered_expected)

    html += "</table>"
    return HTML(html)

# likewise but with a different layout
# see w4_comps.py for an example of use
# this is a patch...
def exemple_table_args (function_name,
                        arg_names,
                        correct_function,
                        datasets,
                        columns = default_table_columns,
                        copy_mode = 'deep',
                        dataset_index = 0):

    # can provide 3 args (convenient when it's the same as correction) or just 2
    columns = columns[:2]
    c1,c2 = columns
    html = ""
    html += u"<table style='{}'>".format(font_style)
    html += u"<tr><th>Arguments</th><th>Résultat attendu</th></tr>"
    
    sample_dataset = clone_dataset (datasets[dataset_index], copy_mode)
    nb_args = len(arg_names)
    for index,arg,name in zip(range(nb_args),sample_dataset, arg_names):
        rendered_input = "{}={}".format(name,truncate_list(arg,c1))
        if index==0:
            expected = apply (correct_function, sample_dataset)
            rendered_expected = truncate (expected, c2)
        else:
            rendered_expected = ""
        html += "<tr><td>{}</td><td>{}</td></tr>".format(rendered_input,rendered_expected)

    html += "</table>"
    return HTML(html)


