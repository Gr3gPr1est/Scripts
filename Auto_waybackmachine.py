import sys
import os
from sys import argv


print '''

############################
#######    Auto_.py    #####
#######  Greg Priest   #####
############################
'''
iplist = argv[1]
outname = argv[2]

print "[+] Wordlist: "+iplist
print "[+] in progress!" 
print "[+] Take RedBull and wait! ;]"
with open(iplist) as f:
        for line in f:
                for word in line.split():
                        print word
                        os.system("python /root/tools/waybackMachine/waybackMachine.py "+word+" >> "+outname+".txt")
