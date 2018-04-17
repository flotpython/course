#!/usr/bin/env python

import turtle

def wait_input (*args):
    return raw_input ("Press Enter ...")

def interpret (func_call_as_tuple):
    print 'interpreting',func_call_as_tuple
    try:
        func_name=func_call_as_tuple[0]
        func=turtle.__dict__[func_name]
        args=func_call_as_tuple[1:]
        return func(*args)
    except Exception,e:
        print 'Could not interpret',func_call_as_tuple
        import traceback
        traceback.print_exc()
        return None
    

from list_flatten import list_flatten

nonagon = [ 
    ( 'color', 'red', 'yellow' ),
    # ATTENTION : the comma is required here
    ( 'begin_fill', ),
    [ [ ('left',40), ('forward', 100) ] for i in xrange (9) ],
    # ATTENTION : the comma is required here
    ( 'end_fill', ),
]

star = [ 
    ('color', 'blue', 'gray') ,
    [ [ ('forward', 200), ('left',150) ] for i in xrange (12) ],
]

inputs = [ nonagon, star ]

def main ():
    current=inputs
    def draw_current (x,y):
        print 'CLICK'
        if not current: exit(0)
        input=current.pop(0)
        print 20*'='
        print 'before flatten:',input
        input = list_flatten (input)
        print 'after flatten:',input
#        turtle.reset()
        turtle.speed('fastest')
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        for funcall in input:
            interpret (funcall)
    draw_current(0,0)
    turtle.onscreenclick(draw_current)
    turtle.mainloop()

if __name__ == '__main__': main()
