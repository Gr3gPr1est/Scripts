import socket
import sys
import os


counter = 0

started_ip_dig_0 = 1
started_ip_dig_1 = 1
started_ip_dig_2 = 1
started_ip_dig_3 = 1

ended_ip_dig_0 = 1
ended_ip_dig_1 = 1
ended_ip_dig_2 = 1
ended_ip_dig_3 = 2

network_start = str(started_ip_dig_0)+'.'+str(started_ip_dig_1)+'.'+str(started_ip_dig_2)+'.'+str(started_ip_dig_3)
network_end = str(ended_ip_dig_0)+'.'+str(ended_ip_dig_1)+'.'+str(ended_ip_dig_2)+'.'+str(ended_ip_dig_3)

print "[x] Network:", network_start +"-"+network_end
print "[x] FTP service searching..."
print "[x] Take a RedBull and wait!\n"

while ( counter != 1):
	if started_ip_dig_3 != 255 + 1:
		ip = str(started_ip_dig_0)+'.'+str(started_ip_dig_1)+'.'+str(started_ip_dig_2)+'.'+str(started_ip_dig_3)
		port = 21
		print ip
		try:
			s = socket.create_connection((ip, port), timeout=2)
#			print s.recv(1024)
			file = open("FTP_Server_list.txt","a")
			file.write(ip + "\t" + s.recv(1024) + "\n")
			file.close()
			print "\n","[x]",ip, "FTP found!"
			s.close
		except socket.error,e:
			sys.stdout.write('.')
		except socket.timeout as message:
			sys.stdout.write('.')
		started_ip_dig_3 = started_ip_dig_3+1
		
	if started_ip_dig_3 == 255 + 1:
		started_ip_dig_2 = started_ip_dig_2 + 1
		started_ip_dig_3 = 0
		
	if started_ip_dig_2 == 255  + 1:
                started_ip_dig_1 = started_ip_dig_1 + 1
                started_ip_dig_2 = 0
                started_ip_dig_3 = 0
                
	if started_ip_dig_1 == 255 + 1:
                started_ip_dig_0 = started_ip_dig_0 + 1
                started_ip_dig_1 = 0
                started_ip_dig_2 = 0
                started_ip_dig_3 = 0
                
        if ip == network_end:
            counter = 1
print "\n[x] FTP service search finished!"
print "[x] Results:\a"

try:
        result_read = open("FTP_Server_list.txt", "r")
        print result_read.read()

except:
        print "No Results..."

ex = raw_input("")


