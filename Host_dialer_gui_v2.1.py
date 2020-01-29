import socket
import subprocess
import sys
from datetime import datetime
import os
from Tkinter import *

def Host_dialer():
    counter = 0

    started_ip_dig_0 = (tk_started_ip_dig_0.get())
    started_ip_dig_1 = (tk_started_ip_dig_1.get())
    started_ip_dig_2 = (tk_started_ip_dig_2.get())
    started_ip_dig_3 = (tk_started_ip_dig_3.get())

    ended_ip_dig_0 = (tk_ended_ip_dig_0.get())
    ended_ip_dig_1 = (tk_ended_ip_dig_1.get())
    ended_ip_dig_2 = (tk_ended_ip_dig_2.get())
    ended_ip_dig_3 = (tk_ended_ip_dig_3.get())

    port = (tk_port.get())

    network_start = str(started_ip_dig_0)+'.'+str(started_ip_dig_1)+'.'+str(started_ip_dig_2)+'.'+str(started_ip_dig_3)
    network_end = str(ended_ip_dig_0)+'.'+str(ended_ip_dig_1)+'.'+str(ended_ip_dig_2)+'.'+str(ended_ip_dig_3)

    print "[x] Network:", network_start +"-"+network_end
    print "[x] Searched port:",port
    print "[x] Network scan running!"
    print "[x] Take a RedBull and wait!"

    while (counter != 1):
        if started_ip_dig_3 != 255 + 1:
            ip = str(started_ip_dig_0)+'.'+str(started_ip_dig_1)+'.'+str(started_ip_dig_2)+'.'+str(started_ip_dig_3)
            print ip
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s = socket.create_connection((ip, port), timeout=2)
                file = open("Open_port_list_"+str(network_start)+".txt","a")
                file.write(ip + "\t" + "Port: " + str(port) + " Open!" + "\n")
                file.close()
                file = open("ip_list.txt","a")
                file.write(ip+"\n")
                file.close()
                print "\n",ip, "/"+str(port), "is open!"
                s.close()
            except socket.error,e:
                sys.stdout.write('.')
            except socket.timeout as message:
                sys.stdout.write('.')
            started_ip_dig_3 = int(started_ip_dig_3)
            started_ip_dig_3 = started_ip_dig_3+1
        
        if int(started_ip_dig_3) == 255 + 1:
                started_ip_dig_2 = int(started_ip_dig_2)
                started_ip_dig_2 = started_ip_dig_2 + 1
                started_ip_dig_3 = 0
	    
        if int(started_ip_dig_2) == 255  + 1:
                started_ip_dig_1 = int(started_ip_dig_1)
                started_ip_dig_1 = started_ip_dig_1 + 1
                started_ip_dig_2 = 0
                started_ip_dig_3 = 0
            
        if int(started_ip_dig_1) == 255 + 1:
                started_ip_dig_0 = int(started_ip_dig_0)
                started_ip_dig_0 = started_ip_dig_0 + 1
                started_ip_dig_1 = 0
                started_ip_dig_2 = 0
                started_ip_dig_3 = 0
                
        if ip == network_end:
                counter = 1
    print "\n[x] Service search finished!"
    print "[x] Results:\a"

    try:
        result_read = open("Open_port_list_"+network_start+".txt", "r")
        print result_read.read()
    except:
        print "No Results..."
        file = open("Open_port_list_"+str(network_start)+".txt","a")
        file.write("Network:" + network_start +"-"+network_end + "\n Port:" + str(port) + "\n No Result!" + "\n")
        file.close()
#    ex = raw_input("")

def nmap_scanner():
    print "[x] Scanning in progress!"
    iplist = "ip_list.txt"
    with open(iplist) as f:
        for line in f:
            for word in line.split():
                print "[X] Scanning: "+word
                os.system("nmap -sV -PN "+word+" >> "+word+".txt")
                
    print "[X] Scanning finished!"


abl1 =Tk()
abl1.title("Host Dialer v1.0beta")
txt1 =Label(abl1,text = "IP range:")
txt2 =Label(abl1,text = '-')
txt3 =Label(abl1,text = '.')
txt4 =Label(abl1,text = '.')
txt5 =Label(abl1,text = '.')
txt6 =Label(abl1,text = '.')
txt7 =Label(abl1,text = '.')
txt8 =Label(abl1,text = '.')
txt9 =Label(abl1,text = "Searched port:")
txt10 =Label(abl1,text = "Powered by nmap!")
gomb1 =Button(abl1,text="Start",command=Host_dialer)
gomb2 =Button(abl1,text="Exit",command=abl1.quit)
gomb3 =Button(abl1,text="Result Scanning",command=nmap_scanner)

tk_started_ip_dig_0 = Entry(abl1, width = 5)
tk_started_ip_dig_1 = Entry(abl1, width = 5)
tk_started_ip_dig_2 = Entry(abl1, width = 5)
tk_started_ip_dig_3 = Entry(abl1, width = 5)
tk_ended_ip_dig_0 = Entry(abl1, width = 5)
tk_ended_ip_dig_1 = Entry(abl1, width = 5)
tk_ended_ip_dig_2 = Entry(abl1, width = 5)
tk_ended_ip_dig_3 = Entry(abl1, width = 5)
tk_port = Entry(abl1, width = 5)

txt1.grid(row = 0)
tk_started_ip_dig_0.grid(row = 0, column = 1)
txt3.grid(row = 0, column = 2)
tk_started_ip_dig_1.grid(row = 0, column = 3)
txt4.grid(row = 0, column = 4)
tk_started_ip_dig_2.grid(row = 0, column = 5)
txt5.grid(row = 0, column = 6)
tk_started_ip_dig_3.grid(row = 0, column = 7)
txt2.grid(row = 0, column = 8)
tk_ended_ip_dig_0.grid(row = 0, column = 9)
txt6.grid(row = 0, column = 10)
tk_ended_ip_dig_1.grid(row = 0, column = 11)
txt7.grid(row = 0, column = 12)
tk_ended_ip_dig_2.grid(row = 0, column = 13)
txt8.grid(row = 0, column = 14)
tk_ended_ip_dig_3.grid(row = 0, column = 15)
txt9.grid(row = 0, column = 16)
txt10.grid(row = 2,column = 0 )
tk_port.grid(row = 0, column = 17)
gomb1.grid(row = 0, column =18)
gomb2.grid(row = 0, column =19)
gomb3.grid(row = 1)

abl1.mainloop()

