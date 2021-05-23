from turtle import Turtle
from piece import Piece
class King(Piece):
    def __init__(self,spot,iswhite):
        super().__init__(spot, iswhite)
        self.value = 1000
        self.ficha = Turtle()
        self.ficha.penup()
        if iswhite:
            self.ficha.shape('../Pieces/wK.gif')
            self.ficha.setheading(90)
        else:
            self.ficha.shape('../Pieces/bK.gif')
            self.ficha.setheading(-90)