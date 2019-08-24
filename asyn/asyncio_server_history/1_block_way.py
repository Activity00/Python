import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8888))
sock.listen(5)
while True:
    s, attr = sock.accept()
    print(attr)
    chunk = s.recv(4089)
    print(chunk)
    s.close()
