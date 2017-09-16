import threading
import time
from django_redis import get_redis_connection
from texas.game.checkers.checker_parser import CheckerParser


class CheckRoomInfoThread(threading.Thread):

    def __init__(self, factory, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.factory = factory

    def run(self):
        while True:
            conn = get_redis_connection('redis')

            # 检查room info
            room_infos = conn.zrangebyscore('texas-game-room-infos', 0, int(time.time()))
            for room_info in room_infos:
                room_info = str(room_info, encoding='utf-8')
                checker = CheckerParser.parse(self.factory, room_info)
                if not checker:
                    print('invalid checker')
                else:
                    checker.check()
                conn.zrem('texas-game-room-infos', room_info)
            time.sleep(1)