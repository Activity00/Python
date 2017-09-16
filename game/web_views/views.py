from texas.game.room2 import Room
import json
from twisted.web.resource import Resource


class CreateRoom(Resource):
    isLeaf = True

    def __init__(self, factory):
        self.factory = factory
        super(CreateRoom, self).__init__()

    def render_POST(self, request):
        kwargs = {}
        for key, value in request.args.items():
            value = value[0]
            try:
                value = eval(value)
            except:
                value = value.decode()
            kwargs[key.decode()] = value

        room = Room(**kwargs)

        self.factory.room_dict[room.room_id] = room
        self.factory.player_room_dict[kwargs['player']] = room.room_id

        data = {
            'id': room.room_id,
        }
        return json.dumps(data).encode()


class EnterRoom(Resource):
    isLeaf = True

    def __init__(self, factory):
        self.factory = factory
        super(EnterRoom, self).__init__()

    def render_POST(self, request):
        player_id = eval(request.args[b'player_id'][0].decode())
        room_id = eval(request.args[b'room_id'][0].decode())

        if not self.factory.room_dict.get(room_id):
            data = {
                'error': '该牌局不存在'
            }
        else:
            self.factory.player_room_dict[player_id] = room_id
            data = {
                'id': room_id,
            }

        return json.dumps(data).encode()


class Api(Resource):
    def __init__(self, factory):
        self.factory = factory
        super(Api, self).__init__()

    def getChild(self, path, request):
        if path == b'create-room':
            return CreateRoom(self.factory)
        elif path == b'enter-room':
            return EnterRoom(self.factory)