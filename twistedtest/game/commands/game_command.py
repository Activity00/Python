from texas.game.commands.base_command import BaseCommand
from texas.game.commands.command_forms import CallForm, BetForm, CheckForm, RaiseForm, FoldForm, AllInForm


class CallCommand(BaseCommand):
    Form = CallForm

    def run(self):
        room_id = self.factory.player_room_dict.get(self.protocol.player_id)
        room = self.factory.room_dict.get(room_id)
        room.call(self.form, self.protocol)


class BetCommand(BaseCommand):
    Form = BetForm

    def run(self):
        room_id = self.factory.player_room_dict.get(self.protocol.player_id)
        room = self.factory.room_dict.get(room_id)
        room.bet(self.form, self.protocol)


class AllInCommand(BaseCommand):
    Form = AllInForm

    def run(self):
        room_id = self.factory.player_room_dict.get(self.protocol.player_id)
        room = self.factory.room_dict.get(room_id)
        room.all_in(self.form, self.protocol)


class CheckCommand(BaseCommand):
    Form = CheckForm

    def run(self):
        room_id = self.factory.player_room_dict.get(self.protocol.player_id)
        room = self.factory.room_dict.get(room_id)
        room.check(self.form, self.protocol)


class RaiseCommand(BaseCommand):
    Form = RaiseForm

    def run(self):
        room_id = self.factory.player_room_dict.get(self.protocol.player_id)
        room = self.factory.room_dict.get(room_id)
        room.raise_chips(self.form, self.protocol)


class FoldCommand(BaseCommand):
    Form = FoldForm

    def run(self):
        room_id = self.factory.player_room_dict.get(self.protocol.player_id)
        room = self.factory.room_dict.get(room_id)
        room.fold(self.form, self.protocol)