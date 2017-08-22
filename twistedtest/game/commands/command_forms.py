from django import forms


class BaseForm(forms.Form):
    command = forms.CharField()
    seq = forms.CharField()
    
    
class EnterRoomForm(BaseForm):
    room_id = forms.IntegerField()
    player_id = forms.IntegerField()


class GetRoomForm(BaseForm):
    pass


class SitDownForm(BaseForm):
    name = forms.CharField()
    chips = forms.IntegerField()
    position = forms.IntegerField()


class StartForm(BaseForm):
    pass


class CallForm(BaseForm):
    pass


class BetForm(BaseForm):
    chips = forms.IntegerField()


class CheckForm(BaseForm):
    pass


class RaiseForm(BaseForm):
    chips = forms.IntegerField()


class FoldForm(BaseForm):
    pass


class AllInForm(BaseForm):
    pass
