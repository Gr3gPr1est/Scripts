# this is a python script! 
# bug hunting automatization tool.....
# this script collect information the target domain, subdomains, links, etc....


import os
import sys
from sys import argv

target = argv[1]

print """
=================
 EXPLORATORY_.py
=================
"""
if target == "-h":
	print "[+] Usage example:"
	print "exploratory_.py index.hu"
else:
	print "[+] Stage01: sublist3r.py" 
	os.system("python /home/bughunter/Tools/Sublist3r/sublist3r.py -d "+target+" -o sublist3r")

	print "[+] Stage02: dnscan.py"
	os.system("python /home/bughunter/Tools/dnscan/dnscan.py -d "+target+" -w /home/bughunter/Data/SecLists/Discovery/DNS/sortedcombined-knock-dnsrecon-fierce-reconng.txt -o dnscan")
	os.system("cat dnscan "+' | '+" cut -d' ' -f 3 >> dnscan01")
	os.system("rm -r dnscan") 

	print "[+] Stage03: httprobe"
	os.system("cat sublist3r | /home/bughunter/Tools/httprobe/httprobe >> "+target+"_subdomains.txt")
	os.system("cat dnscan01 | /home/bughunter/Tools/httprobe/httprobe >> "+target+"_subdomains.txt")
	os.system("cat "+target+"_subdomains.txt | cut -d'/' -f 3 >> "+target+"_domain_list.txt")
	os.system("rm -r sublist3r")
	os.system("rm -r dnscan01")

#	print "[+] Stage04: aquatone"
#	os.system("cat "+target+"_subdomains.txt | /home/bughunter/Tools/aquatone")

