from texas.apps.room.models import Room
from texas.game.room import Room
import json
from twisted.web.resource import Resource


class CreateRoom(Resource):
    isLeaf = True

    def __init__(self, factory):
        self.factory = factory
        super(CreateRoom, self).__init__()

    def render_POST(self, request):
        room = Room(request.args[b'name'][0].decode(), eval(request.args[b'size'][0].decode()), eval(request.args[b'id'][0].decode()))
        self.factory.room_dict[room.room_id] = room
        data = {
            'room_id': room.room_id,
            'name': room.name,
            'size': room.size,
        }
        return json.dumps(data).encode()


class Api(Resource):
    def __init__(self, factory):
        self.factory = factory
        super(Api, self).__init__()

    def getChild(self, path, request):
        if path == b'create-room':
            return CreateRoom(self.factory)