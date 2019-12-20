import socket
import subprocess
import sys
from datetime import datetime
import os

counter = 0

started_ip_dig_0 = 5
started_ip_dig_1 = 187
started_ip_dig_2 = 132
started_ip_dig_3 = 152

ended_ip_dig_0 = 5
ended_ip_dig_1 = 187
ended_ip_dig_2 = 132
ended_ip_dig_3 = 155

port = 445

network_start = str(started_ip_dig_0)+'.'+str(started_ip_dig_1)+'.'+str(started_ip_dig_2)+'.'+str(started_ip_dig_3)
network_end = str(ended_ip_dig_0)+'.'+str(ended_ip_dig_1)+'.'+str(ended_ip_dig_2)+'.'+str(ended_ip_dig_3)

print "[x] Network:", network_start +"-"+network_end
print "[x] Searched port:",port
print "[x] Network scan running!"
print "[x] Take a RedBull and wait!"

while (counter != 1):
    if started_ip_dig_3 != 255 + 1:
        ip = str(started_ip_dig_0)+'.'+str(started_ip_dig_1)+'.'+str(started_ip_dig_2)+'.'+str(started_ip_dig_3)
#	print ip
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s = socket.create_connection((ip, port), timeout=2)
            file = open("Open_port_list.txt","a")
            file.write(ip + "\t" + "Port: " + str(port) + " Open!" + "\n")
            file.close()
            print "\n",ip, "/"+str(port), "is open!"
            s.close()
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
print "\n[x] Service search finished!"
print "[x] Results:\a"

try:
    result_read = open("Open_port_list.txt", "r")
    print result_read.read()
except:
    print "No Results..."
ex = raw_input("")
    
