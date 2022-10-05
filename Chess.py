import turtle
import ChessBoard
import ChessPiece
import time

loop = 0
x = -264
while loop < 8:
    turtle.pu()
    turtle.goto(x, -200)
    ChessPiece.pawn()
    x = x+75
    loop = loop+1

loop = 0
x = -280
while loop < 2:
    turtle.pu
    turtle.goto(x, -290)
    ChessPiece.rook()
    x = x+525
    loop = loop+1


loop = 0
x = -210
while loop < 2:
    turtle.pu()
    turtle.goto(x, -295)
    ChessPiece.knight()
    x = x+375
    loop = loop+1

loop = 0
x = -135
while loop < 2:
    turtle.pu()
    turtle.goto(x, -295)
    ChessPiece.bishop()
    x = x+225
    loop = loop+1

turtle.pu
turtle.goto(15, -295)
ChessPiece.queen()

turtle.pu()
turtle.goto(-64, -295)
ChessPiece.king()

time.sleep(10)
    
    
