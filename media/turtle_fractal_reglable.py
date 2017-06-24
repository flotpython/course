#!/usr/bin/env python
import turtle

def left_triangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)

def fractal_side(length, fractal, proportions):
    if fractal == 0:
        turtle.forward(length)
    else:
        [l1, l2, l3]= [p*length for p in proportions]
        fractal_side(l1, fractal-1, proportions)
        turtle.right(60)
        fractal_side(l2, fractal-1, proportions)
        turtle.left(120)
        fractal_side(l2,fractal-1, proportions)
        turtle.right(60)
        fractal_side(l3, fractal-1, proportions)

def fractal_triangle(length, fractal, proportions):
    for i in range(3):
        fractal_side(length,fractal, proportions)
        turtle.left(120)

turtle.reset()
turtle.speed('fastest')
fractal_triangle(300, 4, (.1, .5, .4,))
left_triangle(300)
turtle.exitonclick()
