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

    def __await__(self):
        yield self  # This tells Task to wait for completion.
        return self.result

    __iter__ = __await__


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


async def connected(sock):
    f = Future()
    sock.setblocking(False)
    try:
        sock.connect((host, port))
    except BlockingIOError:
        pass

    def connect():
        f.set_result(None)

    selector.register(sock.fileno(), EVENT_WRITE, connect)
    await f
    selector.unregister(sock.fileno())


async def read(sock):
    f = Future()

    def on_readable():
        f.set_result(sock.recv(4089))

    selector.register(sock.fileno(), EVENT_READ, on_readable)
    chunk = await f
    selector.unregister(sock.fileno())
    return chunk


async def read_all(sock):
    response = b''
    chunk = await read(sock)
    while chunk:
        response += chunk
        chunk = await read(sock)
    return response


class Crawler:
    def __init__(self, url):
        self.url = url

    async def fetch(self):
        sock = socket.socket()
        await connected(sock)
        get = f'GET {self.url} HTTP/1.1\r\nHost: {host}\r\n\r\n'
        sock.send(get.encode('ascii'))
        response = await read_all(sock)
        url_todo.remove(self.url)
        global stop
        if not url_todo:
            stop = True

        return response


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
    print(f'costs: {time.perf_counter() - start}')
