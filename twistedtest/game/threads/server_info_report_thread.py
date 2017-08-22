import json
import threading
import time

from django_redis import get_redis_connection


class ServerInfoReportThread(threading.Thread):
    def __init__(self, startup_args, factory, *args, **kwargs):
        self.server_info = startup_args
        self.factory = factory
        super(ServerInfoReportThread, self).__init__(*args, **kwargs)

    def run(self):
        while True:
            self.server_info['room_count'] = len(self.factory.room_dict)
            self.server_info['last_modified'] = time.time()
            conn = get_redis_connection('redis')
            conn.hset('texas-game-server-infos', self.server_info['server_name'], json.dumps(self.server_info))
            time.sleep(5)
