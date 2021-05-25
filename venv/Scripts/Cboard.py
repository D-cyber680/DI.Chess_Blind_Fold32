import turtle
from turtle import Turtle
from pawn import Pawn
class Board(Turtle):
    def __init__(self):
        super(Board).__init__()
        self.in_x =  -300
        self.in_y = 270
        self.square_size = 4
        self.square = Turtle()
        self.square.hideturtle()
        self.square.shape("square")
        self.chess_coord = {
                       "a1":[-300,-290],    "a2":[-300,-210],    "a3":[-300,-130],    "a4":[-300,-50],     "a5":[-300,30],     "a6":[-300,110],     "a7":[-300,190],    "a8":[-300,270],     # columna torre
                       "b1":[-220,-290],    "b2":[-220,-210],    "b3":[-220,-130],    "b4":[-220,-50],     "b5":[-220,30],     "b6":[-220,110],     "b7":[-220,190],    "b8":[-220,270],     # columna caballo
                       "c1": [-140,-290],   "c2": [-140,-210],   "c3": [-140,-130],   "c4": [-140,-50],    "c5": [-140,30],    "c6": [-140,110],    "c7": [-140,190],   "c8": [-140,270],    # c: alfil
                       "d1": [-60,-290],     "d2": [-60,-210],     "d3": [-60,-130],     "d4": [-60,-50],      "d5": [-60,30],      "d6": [-60,110],      "d7": [-60,190],     "d8": [-60,270],      # c: dama
                       "e1": [20,-290],      "e2": [20,-210],      "e3": [20,-130],      "e4": [20,-50],       "e5": [20,30],       "e6": [20,270],       "e7": [20,190],      "e8": [20,270],       # c: rey
                       "f1": [100,-290],    "f2": [100,-210],    "f3": [100,-130],    "f4": [100,-50],     "f5": [100,30],     "f6": [100,110],     "f7": [100,190],    "f8": [100,270],     # caballo
                       "g1": [180,-290],    "g2": [180,-210],    "g3": [180,-130],    "g4": [180,-50],     "g5": [180,30],     "g6": [180,110],     "g7": [180,190],    "g8": [180,270],     # alfil
                       "h1": [260,-290],    "h2": [260,-210],    "h3": [260,-130],    "h4": [260,-50],     "h5": [260,30],     "h6": [260,110],     "h7": [260,190],    "h8": [260,270],     # torre
                      }
        self.squares = [
                        ['a1','b1','c1','d1','e1','f1','g1','h1'],  # filas
                        ['a2','b2','c2','d2','e2','f2','g2','h2'],
                        ['a3','b3','c3','d3','e3','f3','g3','h3'],
                        ['a4','b4','c4','d4','e4','f4','g4','h4'],
                        ['a5','b5','c5','d5','e5','f5','g5','h5'],
                        ['a6','b6','c6','d6','e6','f6','g6','h6'],
                        ['a7','b7','c7','d7','e7','f7','g7','h7'],
                        ['a8','b8','c8','d8','e8','f8','g8','h8'],
                        ]

    def drawBoard(self):
        self.square.penup()
        self.square.turtlesize(self.square_size, self.square_size, 0)
        self.square.setposition(self.in_x, self.in_y)
        for i in range(8):
            self.square.setx(self.in_x)
            for j in range(8):
                self.square.setheading(0)
                if (j % 2 and not i % 2 or not j % 2 and i % 2):
                    self.square.color("saddlebrown")
                else:
                    self.square.color("burlywood")
                self.square.stamp()
                self.square.forward(80)
            self.square.setheading(270)
            self.square.backward(-80)

    def get_turtle_pos(self,sqr_str):
       pos =  self.chess_coord[sqr_str]
       for p in turtle.turtles():
            if p.position() == (pos[0],pos[1]):
                return p

    def delete_turtle(self,sqr_b):
        piece = self.get_turtle_pos(sqr_b)
        if piece != None:
            piece.hideturtle()


    def putWhitePawns(self,white_pawns_list):
        for i in range(8):
            sq = self.squares[1][i]
            new_spot = self.chess_coord[sq]
            new_pawn = Pawn(new_spot, True)
            new_pawn.ficha.setpos(new_pawn.spot)
            white_pawns_list.append(new_pawn)

    def putBlackPawns(self,black_pawns_list):
        for i in range(8):
            sq = self.squares[6][i]
            new_spot = self.chess_coord[sq]
            new_pawn = Pawn(new_spot, False)
            new_pawn.ficha.setpos(new_pawn.spot)
            black_pawns_list.append(new_pawn)

    def putwhitePieces(self,rookq,knightq,bishopq,queen,king,bishopk,knightk,rookk):
        listwp = [rookq,knightq,bishopq,queen,king,bishopk,knightk,rookk]
        for piece in listwp:
            piece.ficha.setpos(piece.spot)

    def putblackPieces(self,rookq,knightq,bishopq,queen,king,bishopk,knightk,rookk):
        listbp = [rookq,knightq,bishopq,queen,king,bishopk,knightk,rookk]
        for piece in listbp:
            piece.ficha.setpos(piece.spot)






