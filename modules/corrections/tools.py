# -*- coding: iso-8859-15 -*-
from IPython.display import HTML
import traceback

def truncate (data, max_size=10):
    message = "{}".format(data)
    return message if len(message) <= max_size \
        else message [:max_size-3]+'...'


ok_style='background-color:#66CC66;'
ko_style='background-color:#CC3300;color:#e8e8e8;'
default_table_columns = (20, 20, 30)

def correction_as_table (student_function,
                         correct_function,
                         datasets,
                         columns = default_table_columns):
    c1,c2,c3 = columns
    html = ""
    html += u"<table>"
    html += u"<tr><th>Entrée(s)</th><th>Attendu</th><th>Obtenu</th><th></th></tr>"

    for dataset in datasets:
        expected = apply (correct_function, dataset)
        try:
            student_result = apply (student_function, dataset)
        except Exception as e:
            student_result = e
        ok = expected == student_result
        result_cell = '<td style="background-color:green;">'
        message = 'OK' if ok else 'KO'
        style = ok_style if ok else ko_style
        html += "<tr style='{}'>".format(style)
        html += "<td>{}</td><td>{}</td><td>{}</td><td>{}</td>".\
                format(truncate(dataset,c1),truncate(expected,c2),
                       truncate(student_result,c3),message)
    html += "</table>"
    return HTML(html)

# see how to use in exo_rendering.py
