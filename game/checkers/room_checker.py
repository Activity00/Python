from texas.game.checkers.base_checker import BaseChecker


class BringStackChecker(BaseChecker):

    def check(self):
        result = self.room.check_player_status(self.player_id, 'sit')
        if result:
            self.room.remove_player_join_fail(self.player_id)


class WaitingAuthChecker(BaseChecker):

    def check(self):
        result = self.room.check_player_status(self.player_id, 'bring_stack')
        if result:
            self.room.remove_player_join_fail(self.player_id)


class DismissRoomChecker(BaseChecker):

    def check(self):
        self.room.dismiss()
        self.factory.room_dict.pop(self.room.room_id)
        for player_id in self.room.players.keys():
            self.factory.player_room_dict.pop(player_id)
        self.room.clear_room()

