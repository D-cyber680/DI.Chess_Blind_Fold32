from turtle import Turtle
from piece import Piece
class Knight(Piece):
    def __init__(self,spot,iswhite):
        super().__init__(spot, iswhite)
        self.value = 3
        self.ficha = Turtle()
        self.ficha.penup()
        if iswhite:
            self.ficha.shape('../Pieces/wN.gif')
            self.ficha.setheading(90)
        else:
            self.ficha.shape('../Pieces/bN.gif')
            self.ficha.setheading(-90)