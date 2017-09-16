from texas.game import checkers


class CheckerParser:
    @classmethod
    def parse(cls, factory, room_info):
        room_info_list = room_info.split(':')
        checker_name = room_info_list[0]
        room_id = int(room_info_list[1])
        player_id = len(room_info_list) > 2 and int(room_info_list[2]) or None

        Checker = getattr(checkers, checker_name + 'Checker', None)
        if not Checker:
            return None

        checker = Checker(factory, room_id, player_id)

        if not checker.is_valid():
            return None

        return checker