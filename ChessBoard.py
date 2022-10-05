import turtle
import Square
import time


screen = turtle.Screen()
screen.setup(675, 675)


turtle.speed(0)



turtle.color("red", "red")
turtle.pu()
y = 300
turtle.goto(-300, y)


def roweven():
    repeat = 0
    while repeat<4:
        Square.empty()

        turtle.forward(75)

        turtle.pu()
        Square.fill()
        
        turtle.forward(75)
        
        repeat = (repeat)+1

def rowodd():
    repeat = 0
    while repeat<4:
        Square.fill()

        turtle.forward(75)

        turtle.pu()
        Square.empty()
        
        turtle.forward(75)
        
        repeat = (repeat)+1

        
loop = 0
while loop < 4:
    repeat = 0
    roweven()
    turtle.pu
    y = y-75
    turtle.goto(300, y)
    turtle.goto(-300, y)
    rowodd()
    turtle.pu
    y = y-75
    turtle.goto(300, y)
    turtle.goto(-300, y)
    turtle.pd
    
    loop = (loop+1)
    print(loop)
