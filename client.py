## client program

import socket

host  = 'nombresito'
port = 8000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host,port))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('recived', repr(data))
