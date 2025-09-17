#server ipv4 and ipv6

import socket
import sys


host = None
port = 8000
s =None

for res in socket.getaddrinfo(host,port,socket.AF_UNSPEC, socket.SOCK_STREAM,0,socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af,socktype,proto)
    except OSError as msg:
        s=None
        continue
 # stop code continue ....