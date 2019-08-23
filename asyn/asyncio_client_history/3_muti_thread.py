import socket
from concurrent.futures import ThreadPoolExecutor

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
        soct.connect((host, port))
        get = f'GET {self.url} HTTP/1.1\r\nHost: {host}\r\n\r\n'
        soct.send(get.encode('ascii'))

        chunk = soct.recv(4096)
        while chunk:
            response += chunk
            chunk = soct.recv(4089)
        return response


if __name__ == '__main__':

    import time
    start = time.perf_counter()
    todo_crawlers = [Crawler(url) for url in url_todo]

    with ThreadPoolExecutor() as executor:
        fnt = {executor.submit(crawler.fetch) for crawler in todo_crawlers}

    print(len([r.result() for r in fnt]))
    print(f'costs: {time.perf_counter() -start}')

