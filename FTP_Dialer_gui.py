import socket
import sys
import os
from Tkinter import *

def FTP_dialer():
    counter = 0
    started_ip_dig_0 = (tk_started_ip_dig_0.get())
    started_ip_dig_1 = (tk_started_ip_dig_1.get())
    started_ip_dig_2 = (tk_started_ip_dig_2.get())
    started_ip_dig_3 = (tk_started_ip_dig_3.get())

    ended_ip_dig_0 = (tk_ended_ip_dig_0.get())
    ended_ip_dig_1 = (tk_ended_ip_dig_1.get())
    ended_ip_dig_2 = (tk_ended_ip_dig_2.get())
    ended_ip_dig_3 = (tk_ended_ip_dig_3.get())
    network_start = str(started_ip_dig_0)+'.'+str(started_ip_dig_1)+'.'+str(started_ip_dig_2)+'.'+str(started_ip_dig_3)
    network_end = str(ended_ip_dig_0)+'.'+str(ended_ip_dig_1)+'.'+str(ended_ip_dig_2)+'.'+str(ended_ip_dig_3)
    
    print "[x] Network:", network_start +"-"+network_end
    print "[x] FTP service searching..."
    print "[x] Take a RedBull and wait!\n"
    while ( counter != 1):
        if int(started_ip_dig_3) != 255 + 1:
            ip = str(started_ip_dig_0)+'.'+str(started_ip_dig_1)+'.'+str(started_ip_dig_2)+'.'+str(started_ip_dig_3)
            port = 21
            print ip
            try:
                s = socket.create_connection((ip, port), timeout=2)
                file = open("FTP_Server_list.txt","a")
                file.write(ip + "\t" + s.recv(1024) + "\n")
                file.close()
                print "\n","[x]",ip, "FTP found!"
                s.close
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
    print "\n[x] FTP service search finished!"
    print "[x] Results:\a"
    try:
        result_read = open("FTP_Server_list.txt", "r")
        print result_read.read()
    except:
        print "No Results..."
    ex = raw_input("")


abl1 =Tk()
abl1.title("FTP Dialer v1.0beta")
txt1 =Label(abl1,text = "IP range:")
txt2 =Label(abl1,text = '-')
txt3 =Label(abl1,text = '.')
txt4 =Label(abl1,text = '.')
txt5 =Label(abl1,text = '.')
txt6 =Label(abl1,text = '.')
txt7 =Label(abl1,text = '.')
txt8 =Label(abl1,text = '.')
gomb1 =Button(abl1,text="Start",command=FTP_dialer)
gomb2 =Button(abl1,text="Exit",command=abl1.quit)

tk_started_ip_dig_0 = Entry(abl1, width = 5)
tk_started_ip_dig_1 = Entry(abl1, width = 5)
tk_started_ip_dig_2 = Entry(abl1, width = 5)
tk_started_ip_dig_3 = Entry(abl1, width = 5)
tk_ended_ip_dig_0 = Entry(abl1, width = 5)
tk_ended_ip_dig_1 = Entry(abl1, width = 5)
tk_ended_ip_dig_2 = Entry(abl1, width = 5)
tk_ended_ip_dig_3 = Entry(abl1, width = 5)

txt1.pack(side =LEFT)
tk_started_ip_dig_0.pack(side =LEFT)
txt3.pack(side =LEFT)
tk_started_ip_dig_1.pack(side =LEFT)
txt4.pack(side =LEFT)
tk_started_ip_dig_2.pack(side =LEFT)
txt5.pack(side =LEFT)
tk_started_ip_dig_3.pack(side =LEFT)
txt2.pack(side =LEFT)
tk_ended_ip_dig_0.pack(side =LEFT)
txt6.pack(side =LEFT)
tk_ended_ip_dig_1.pack(side =LEFT)
txt7.pack(side =LEFT)
tk_ended_ip_dig_2.pack(side =LEFT)
txt8.pack(side =LEFT)
tk_ended_ip_dig_3.pack(side =LEFT)
gomb1.pack(side = LEFT)
gomb2.pack(side = LEFT)

abl1.mainloop()



    
    
    
    
    
