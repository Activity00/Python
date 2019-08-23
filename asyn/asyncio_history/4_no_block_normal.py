import socket

stop = False
url_todo = {'/', '/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9'}
host = 'localhost'
port = 8888


class Crawler:
    def __init__(self, url):
        self.url = url

    def fetch(self):
        response = b''
        soct = socket.socket()
        soct.setblocking(False)
        try:
            soct.connect((host, port))
        except BlockingIOError:
            pass

        get = f'GET {self.url} HTTP/1.1\r\nHost: {host}\r\n\r\n'
        while True:
            try:
                soct.send(get.encode('ascii'))
                break
            except BlockingIOError:
                pass

        while True:
            try:
                chunk = soct.recv(4096)
                while chunk:
                    response += chunk
                    chunk = soct.recv(4089)
                break
            except BlockingIOError:
                pass
            return response


if __name__ == '__main__':
    import time
    start = time.perf_counter()
    res = []
    for url in url_todo:
        crawler = Crawler(url)
        res.append(crawler.fetch())
    print(len(res))
    print(f'costs: {time.perf_counter() -start}')

