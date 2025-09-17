## server program

import socket

host = ''
port = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen(3)

    conn, addr = s.accept()

    with conn:
        print("conecteed by", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)