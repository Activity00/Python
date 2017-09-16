class BaseChecker:
    def __init__(self, factory, room_id, player_id=None):
        self.factory = factory
        self.room = self.factory.room_dict.get(room_id)
        self.player_id = player_id

    def is_valid(self):
        return self.room is not None

    def check(self):
        raise NotImplementedError
