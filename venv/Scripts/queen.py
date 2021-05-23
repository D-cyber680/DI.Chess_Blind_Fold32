from turtle import Turtle
from piece import Piece
class Queen(Piece):
    def __init__(self,spot,iswhite):
        super().__init__(spot, iswhite)
        self.value = 9
        self.ficha = Turtle()
        self.ficha.penup()
        if iswhite:
            self.ficha.shape('../Pieces/wQ.gif')
            self.ficha.setheading(90)
        else:
            self.ficha.shape('../Pieces/bQ.gif')
            self.ficha.setheading(-90)