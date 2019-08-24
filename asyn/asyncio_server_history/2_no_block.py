import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.conns = {}

    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(5)

        def readable(event_key, event_mask):
            print('read...')
            conn = list(self.conns.values())[0]
            chunk = conn.recv(4089)
            print(chunk)
            selector.unregister(conn.fileno())
            conn.close()
            # del self.conns[event_key]

        def acceptable(event_key, event_mask):
            print('accept', event_key)
            conn, _ = sock.accept()
            conn.setblocking(False)
            self.conns[event_key] = conn
            selector.register(conn.fileno(), EVENT_READ, readable)

        selector.register(sock.fileno(), EVENT_READ, acceptable)


def loop():
    while True:
        for event_key, event_mask in selector.select():
            cb = event_key.data
            cb(event_key, event_mask)


if __name__ == '__main__':
    server = Server('localhost', 8888)
    server.start()
    loop()
