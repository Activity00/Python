import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()
stop = False
url_todo = {'/', '/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9'}
host = 'localhost'
port = 8888


class Crawler:
    def __init__(self, url):
        self.url = url
        self.socket = None
        self.response = b''

    def fetch(self):
        self.socket = socket.socket()
        self.socket.setblocking(False)
        try:
            self.socket.connect((host, port))
        except BlockingIOError:
            pass

        selector.register(self.socket.fileno(), EVENT_WRITE, self.connected)

    def connected(self, key, mask):
        selector.unregister(key.fd)
        get = f'GET {self.url} HTTP/1.1\r\nHost: {host}\r\n\r\n'
        self.socket.send(get.encode('ascii'))
        selector.register(key.fd, EVENT_READ, self.read_response)

    def read_response(self, key, mask):
        global stop
        chunk = self.socket.recv(4096)
        if chunk:
            self.response += chunk
        else:
            selector.unregister(key.fd)
            url_todo.remove(self.url)
            if not url_todo:
                stop = True


def loop():
    while not stop:
        events = selector.select()
        for event_key, event_mask in events:
            cb = event_key.data
            cb(event_key, event_mask)


if __name__ == '__main__':
    import time
    start = time.perf_counter()
    for url in url_todo:
        crawler = Crawler(url)
        crawler.fetch()
    loop()
    print(f'costs: {time.perf_counter() -start}')
