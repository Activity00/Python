from texas.game.commands.base_command import BaseCommand
from texas.game.commands.command_forms import SitDownForm, StartForm, GetRoomForm, \
    EnterRoomForm


class EnterRoomCommand(BaseCommand):
    Form = EnterRoomForm

    def run(self):
        # self.factory.room.enter_room(self.form, self.protocol)
        room = self.factory.room_dict.get(self.form.cleaned_data['room_id'], 1)
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
        room.start()
        # room.start(self.form, self.protocol)


