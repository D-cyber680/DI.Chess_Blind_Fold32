from turtle import Turtle
from piece import Piece
class Bishop(Piece):
    def __init__(self,spot,iswhite):
        super().__init__(spot, iswhite)
        self.value = 3
        self.ficha = Turtle()
        self.ficha.penup()
        if iswhite:
            self.ficha.shape('../Pieces/wB.gif')
            self.ficha.setheading(90)
        else:
            self.ficha.shape('../Pieces/bB.gif')
            self.ficha.setheading(-90)