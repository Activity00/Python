from twisted.protocols.basic import LineOnlyReceiver


class TexasProtocol(LineOnlyReceiver):

    def __init__(self, factory):
        self.factory = factory

    def sendLine(self, line):
        line = str(line)
        line_bytes = line.encode(encoding='utf_8', errors='strict')
        return super(TexasProtocol, self).sendLine(line_bytes)

    def lineReceived(self, line):
        self.sendLine('hello world')


