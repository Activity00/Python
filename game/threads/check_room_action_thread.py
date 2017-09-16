import threading
import time


class CheckRoomStartThread(threading.Thread):
    def __init__(self, room, form, protocol, *args, **kwargs):
        self.room = room
        self.form = form
        self.protocol = protocol
        super(CheckRoomStartThread, self).__init__(*args, **kwargs)

    def run(self):
        while len(self.room.get_ready_players()) < 2:
            time.sleep(5)
        self.room.start_room(self.form, self.protocol)


class CheckRoomDismissThread(threading.Thread):
    def __init__(self, room, *args, **kwargs):
        self.room = room
        super(CheckRoomDismissThread, self).__init__(*args, **kwargs)

    def run(self):
        while self.room.game_controller.game_state.state != 'over':
            time.sleep(5)
        self.room.dismiss_room()


class RunRoomActionThread(threading.Thread):
    def __init__(self, func, player_id=None, *args, **kwargs):
        self.func = func
        self.player_id = player_id
        super(RunRoomActionThread, self).__init__(*args, **kwargs)

    def run(self):
        if self.player_id:
            self.func(self.player_id)
        else:
            self.func()






