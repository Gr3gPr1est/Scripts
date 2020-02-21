import sys
import os
from sys import argv

print '''
############################
#######	   Auto_.py    #####
#######	 Greg Priest   #####
############################
'''
iplist = argv[1]
recommand = argv[2]
outname = argv[3]
print "[+] Wordlist: "+iplist
print "[+] Outname: "+outnname
print "[+] Command: "+recommand
print "[+] in progress!" 
print "[+] Take a RedBull and wait! ;]"

with open(iplist) as f:
	for line in f:
		for word in line.split():
			print word
			os.system(recommand+" "+word+" >> "+outname)
