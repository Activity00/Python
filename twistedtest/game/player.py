class Player(object):
    def __init__(self, player_id, name, stack, protocol):
        self.player_id = player_id
        self.name = name
        self.stack = stack
        self.protocol = protocol

    def bet_chips(self, bet_chips):
        self.stack -= bet_chips
