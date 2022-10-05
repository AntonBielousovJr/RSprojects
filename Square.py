import turtle

def empty():
    r = 0
    while r<4:
        turtle.pd()
        turtle.forward(75)
        turtle.right(90)
        r = r+1

def fill():
    r = 0
    turtle.begin_fill()
    while r<4:
        turtle.pd()
        turtle.fillcolor
        turtle.forward(75)
        turtle.right(90)
        r = r+1
    turtle.end_fill()
