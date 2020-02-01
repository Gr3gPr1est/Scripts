import sys
import os
from sys import argv
print '''

############################
#######	   Auto_.py    #####
#######	 Greg Priest   #####
############################
'''
print "[+] in progress!" 
print "[+] Take RedBull and wait! ;]"
iplist = argv[1]
with open(iplist) as f:
	for line in f:
		for word in line.split():
			print word
			os.system("python3 /root/tools/dirsearch/dirsearch.py -u "+word+" -e php,asp,jsp -b >> index.txt")
#			os.system("nmap -sV -PN "+word+" >> att_nmap.txt")
