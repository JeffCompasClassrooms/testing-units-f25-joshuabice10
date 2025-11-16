

class Board:

    def __init__(self):
        self.board = {
            '1': False,
            '2': False,
            '3': False,
            '4': False,
            '5': False,
            '6': False,
            '7': False,
            '8': False,
            '9': False,
        }

    def get_board(self):
        return self.board
    
    def set_board(self, key, value):
        self.board[key] = value
        return True