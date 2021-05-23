from turtle import Turtle
from piece import Piece
class Rook(Piece):
    def __init__(self,spot,iswhite):
        super().__init__(spot, iswhite)
        self.value = 5
        self.ficha = Turtle()
        self.ficha.penup()
        if iswhite:
            self.ficha.shape('../Pieces/wR.gif')
            self.ficha.setheading(90)
        else:
            self.ficha.shape('../Pieces/bR.gif')
            self.ficha.setheading(-90)