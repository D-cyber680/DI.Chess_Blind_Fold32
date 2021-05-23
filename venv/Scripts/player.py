class Player(object):
    def __init__(self,plays_white):
        self.plays_white = plays_white
        if self.plays_white == True:
            self.has_to_move = True
        else:
            self.has_to_move = False


