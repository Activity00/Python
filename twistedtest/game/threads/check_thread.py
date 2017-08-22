import threading
import time
from texas.game.commands.command_forms import FoldForm
from django_redis import get_redis_connection


class CheckThread(threading.Thread):

    def __init__(self, room_dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_dict = room_dict

    def run(self):
        #TODO get score, check start version
        while True:
            conn = get_redis_connection('redis')
            room_id_list = list(self.room_dict.keys())
            for room_id in room_id_list:
                room = self.room_dict.get(room_id)
                if not room.has_started():
                    start_list = conn.zrangebyscore('start:' + str(room_id), 0, int(time.time()))
                    for start in start_list:
                        start = str(start, encoding='utf-8')
                        if start == str(room.check['start']):
                            room.start()
                            conn.zremrangebyrank('start:' + str(room_id), 0, -1)
                else:
                    # TODO If player does not action in 30s, then fold!
                    player_id = room.check['next_player']
                    protocol = room.get_player_by_id(player_id).protocol
                    score = conn.zscore('fold:' + str(room_id), room.check['next_player'])
                    if score:
                        if int(score) <= int(time.time()):
                            form = FoldForm({"command": "Fold", "seq": "seq"})
                            form.is_valid()
                            room.fold(form, protocol)
                            conn.zrem('fold:' + str(room_id), room.check['next_player'])
            time.sleep(2)