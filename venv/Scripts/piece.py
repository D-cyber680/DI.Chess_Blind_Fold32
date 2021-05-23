from turtle import Turtle
class Piece(object):
    def __init__(self,spot,iswhite):
        self.spot = spot
        self.iswhite = iswhite
        self.killed = False

    def get_white(self):
        return self.iswhite

    def set_killed(self,killed):
        self.killed = killed

    def get_killed(self):
        return self.killed
