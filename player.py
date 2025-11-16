

class Player:

    def __init__(self, symbol, player_name):
        self.symbol = "  " + str(symbol) + "  "
        self.player_name = player_name
        self.wins = 0

    def get_symbol(self):
        return self.symbol
    
    def get_wins(self):
        return self.wins

    def get_player_name(self):
        return self.player_name

    def inc_wins(self):
        self.wins += 1
        return True