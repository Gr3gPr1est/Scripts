import socket

port = 14956
s = socket.socket()
ip = '10.15.67.184'            
s.bind((ip, port))            
s.listen(5)                    

print "Listening on port:", port

while True:
    conn, addr = s.accept()     
    conn.send("A" * 10000+'\r\n')
    conn.close()
