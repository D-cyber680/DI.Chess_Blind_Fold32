from turtle import Turtle
from piece import Piece
class Pawn(Piece):
    def __init__(self,spot,iswhite):
        super().__init__(spot, iswhite)
        self.value = 1
        self.ficha = Turtle()
        self.ficha.penup()
        if iswhite:
            self.ficha.shape('../Pieces/wP.gif')
            self.ficha.setheading(90)
        else:
            self.ficha.shape('../Pieces/bP.gif')
            self.ficha.setheading(-90)

    def able_move_two_sq(self):
        if iswhite and spot[1] == -210:
            z = True
        elif not(iswhite) and spot[1] == 190:
            z = True
        else:
            z = False
        return z

    def check_legal(self,movimiento):
        pass
