import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()
stop = False
url_todo = {'/', '/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9'}
host = 'localhost'
port = 8888


class Future:
    def __init__(self):
        self.result = None
        self.callbacks = []

    def set_result(self, result):
        self.result = result
        for cb in self.callbacks:
            cb(self)

    def add_callback(self, fn):
        self.callbacks.append(fn)


class Task:
    def __init__(self, coro):
        self.coro = coro
        self.step(Future())

    def step(self, f):
        try:
            next_future = self.coro.send(f.result)
        except StopIteration:
            return
        next_future.add_callback(self.step)


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

        f = Future()

        def connected():
            f.set_result(None)

        selector.register(self.socket.fileno(), EVENT_WRITE, connected)
        yield f

        selector.unregister(self.socket.fileno())
        get = f'GET {self.url} HTTP/1.1\r\nHost: {host}\r\n\r\n'
        self.socket.send(get.encode('ascii'))

        global stop
        while True:
            f = Future()

            def on_readable():
                f.set_result(self.socket.recv(4089))

            selector.register(self.socket.fileno(), EVENT_READ, on_readable)
            chunk = yield f
            selector.unregister(self.socket.fileno())
            if chunk:
                self.response += chunk
            else:
                url_todo.remove(self.url)
                if not url_todo:
                    stop = True
                break


def loop():
    while not stop:
        events = selector.select()
        for event_key, event_mask in events:
            cb = event_key.data
            cb()


if __name__ == '__main__':
    import time
    start = time.perf_counter()
    tasks = []
    for url in url_todo:
        crawler = Crawler(url)
        tasks.append(Task(crawler.fetch()))

    loop()
    print(f'costs: {time.perf_counter() -start}')
