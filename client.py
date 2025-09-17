## client program

import socket

host  = 'nombre_del_servidor_o_ip'
port = 8000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host,port))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('recived', repr(data))
