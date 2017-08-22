import json
from texas.game import commands


class CommandParser:
    @classmethod
    def parse(cls, factory, protocol, line):
        try:
            if isinstance(line, bytes):
                data = json.loads(str(line, encoding='utf8'))
            else:
                data = json.loads(line)
        except:
            message = 'json解析错误'
            return None, 400, message

        if 'command' not in data:
            message = '缺少command属性'
            return None, 400, message

        Command = getattr(commands, data['command'] + 'Command', None)
        if not Command:
            message = '对应command不存在'
            return None, 400, message
        
        command = Command(factory, protocol, data)
        is_valid, errors = command.is_valid()
        if not is_valid:
            return None, 400, errors
        
        return command, 200, None
