# we need the turtle module
import turtle


def square (length):
    "a procedure to draw a square of side length"
    for side in range (4):
        turtle.forward (length)
        turtle.left (90)


# initialize the turtle
turtle.reset()
# draw the square
square (300)
# wait for a user to click and then exit
turtle.exitonclick()
