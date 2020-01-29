import sys
import os

print '''

############################
#######	   Auto_.py    #####
#######	 Greg Priest   #####
############################
'''
print "[+] in progress!" 
print "[+] Take RedBull and wait! ;]"
iplist = "huffingtonpost_subdomain.txt"
with open(iplist) as f:
	for line in f:
		for word in line.split():
			print word
			os.system("python3 /root/tools/dirsearch/dirsearch.py -u https://"+word+" -e php,asp >> dirsearch_huffingtonpost_com.txt")
