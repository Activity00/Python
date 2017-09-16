import json


def broadcast(protocol_objs, message):
    for o in protocol_objs:
        o.protocol.sendLine(message)


def notify(protocol_obj, message):
    protocol_obj.protocol.sendLine(message)


class TexasCommandResponse(object):
    def __init__(self, command, commander, seq, status, _type, message, result, errors):
        self.data = {
            'command': command,
            'commander': commander,
            'seq': seq, # 广播时，seq=''
            'status': status,
            'type': _type, # command_result, broadcast, notice
            'message': message
        }
        if not result:
            if errors:
                self.data['errors'] = errors

        else:
            self.data['result'] = result

    def __str__(self):
        return json.dumps(self.data)


class TexasCommandResponseSuccess(TexasCommandResponse):
    def __init__(self, command, commander, seq, result):
        super(TexasCommandResponseSuccess, self).__init__(command, commander, seq, 0, 'command_result', 'OK', result, None)


class TexasCommandResponseError(TexasCommandResponse):
    def __init__(self, command, commander, seq, status, message, result=None, errors=None):
        super(TexasCommandResponseError, self).__init__(command, commander, seq, status, 'command_result', message, result, errors)


class TexasCommandResponseBroadcast(TexasCommandResponse):
    def __init__(self, command, commander, result):
        super(TexasCommandResponseBroadcast, self).__init__(command, commander, '', 0, 'broadcast', '', result, None)


class TexasCommandResponseNotice(TexasCommandResponse):
    def __init__(self, command, commander, result):
        super(TexasCommandResponseNotice, self).__init__(command, commander, '', 0, 'notice', '', result, None)
