class GameEvent(object):
    def __init__(self, event, data):
        self.event = event
        self.data = data


class GameHand(object):
    def __init__(self):
        self.events = []
        
    def add_event(self, event):
        self.events.append(event)
        
    def reset(self):
        self.events = []


class GameRound(object):
    def __init__(self, stage):
        self.stage = stage  # 0:pre-flop, 1:flop, 2:turn, 3:river
        self.player_actions = []
        self.next_player = {}
        self.to_call = 0
        self.to_raise = 0
        self.player_in_pot = {}
 
    def allow_next_player_actions(self, position, big_blind_position):
        self.next_player.clear()
        to_call = self.to_call
        if position in self.player_in_pot:
            to_call = self.to_call - self.player_in_pot[position]
        action_choices = {'call': to_call, 'fold': 0}
        if self.stage == 0:
            action_choices['raise'] = self.to_raise
            if position == big_blind_position:
                if to_call == 0:
                    action_choices['check'] = 0
        else:
            if not self.player_in_pot:
                action_choices['check'] = 0
            else:
                action_choices['raise'] = self.to_raise
 
    def add_player_action(self, action):
        self.player_actions.append(action)
 
    def add_player_in_pot(self, position, stake):
        if position not in self.player_in_pot:
            self.player_in_pot[position] = stake
        else:
            self.player_in_pot[position] += stake
 
    def remove_player_in_pot(self, position):
        self.player_in_pot.pop(position)
 
    def has_matched_in_pot(self, active_player_positions):
        for position in active_player_positions:
            if position not in list(self.player_in_pot.keys()):
                return False
        amount_in_pot_list = list(self.player_in_pot.values())
        if amount_in_pot_list.count(amount_in_pot_list[0]) != len(amount_in_pot_list):
                return False
        return True
