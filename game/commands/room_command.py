from texas.game.commands.base_command import BaseCommand
from texas.game.commands.command_forms import SitDownForm, StartForm, GetRoomForm, \
    EnterRoomForm, CancelJoinRoomForm, JoinRoomForm, HostAgreeForm, DismissRoomForm
from texas.game.twisted.response import TexasCommandResponseError


class EnterRoomCommand(BaseCommand):
    Form = EnterRoomForm

    def run(self):
        # self.factory.room.enter_room(self.form, self.protocol)
        room = self.factory.room_dict.get(self.form.cleaned_data['room_id'])
        if not room:
            response = TexasCommandResponseError('', '', '', 400, '请求参数错误', errors='该房间不存在')
            self.protocol.sendLine(response)
        else:
            room.enter_room(self.form, self.protocol)


class GetRoomStateCommand(BaseCommand):
    Form = GetRoomForm

    def run(self):
        room_id = self.factory.player_room_dict.get(self.protocol.player_id)
        room = self.factory.room_dict.get(room_id)
        room.get_room_state(self.form, self.protocol)


class SitDownCommand(BaseCommand):
    Form = SitDownForm

    def run(self):
        # self.factory.room.sit_down(self.form, self.protocol)
        room_id = self.factory.player_room_dict.get(self.protocol.player_id)
        room = self.factory.room_dict.get(room_id)
        room.sit_down(self.form, self.protocol)


class StartCommand(BaseCommand):
    Form = StartForm

    def run(self):
        room_id = self.factory.player_room_dict.get(self.protocol.player_id)
        room = self.factory.room_dict.get(room_id)
        room.start(self.form, self.protocol)


class CancelJoinRoomCommand(BaseCommand):
    Form = CancelJoinRoomForm

    def run(self):
        # self.factory.room.sit_down(self.form, self.protocol)
        room_id = self.factory.player_room_dict.get(self.protocol.player_id)
        room = self.factory.room_dict.get(room_id)
        room.cancel_join_room(self.form, self.protocol)


class JoinRoomCommand(BaseCommand):
    Form = JoinRoomForm

    def run(self):
        # self.factory.room.sit_down(self.form, self.protocol)
        room_id = self.factory.player_room_dict.get(self.protocol.player_id)
        room = self.factory.room_dict.get(room_id)
        room.join_room(self.form, self.protocol)


class HostAgreeCommand(BaseCommand):
    Form = HostAgreeForm

    def run(self):
        # self.factory.room.sit_down(self.form, self.protocol)
        room_id = self.factory.player_room_dict.get(self.protocol.player_id)
        room = self.factory.room_dict.get(room_id)
        room.host_agree(self.form, self.protocol)


class DismissRoomCommand(BaseCommand):
    Form = DismissRoomForm

    def run(self):
        # self.factory.room.sit_down(self.form, self.protocol)
        room_id = self.factory.player_room_dict.get(self.protocol.player_id)
        room = self.factory.room_dict.get(room_id)
        room.host_dismiss_room(self.form, self.protocol)



