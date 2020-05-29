# this is a python script! 
# bug hunting automatization tool.....
# this script collect information the target domain, subdomains, links, etc....


import os
import sys
from sys import argv

target = argv[1]
domainlist = target+"_wget_list.txt"

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
	os.system("python /home/bughunter/Tools/dnscan/dnscan.py -d "+target+" -o dnscan")
	os.system("cat dnscan "+' | '+" cut -d' ' -f 3 >> dnscan01")
	os.system("rm -r dnscan") 

	print "[+] Stage03: httprobe"
	os.system("cat sublist3r | /home/bughunter/Tools/httprobe/httprobe >> "+target+"_httprobe.txt")
	os.system("cat dnscan01 | /home/bughunter/Tools/httprobe/httprobe >> "+target+"_httprobe.txt")
	os.system("cat "+target+"_httprobe.txt | cut -d'/' -f 3 >> "+target+"_wget_list.txt")
	os.system("rm -r sublist3r")
	os.system("rm -r dnscan01")
	os.system("cat "+target+"_httprobe.txt | /home/bughunter/Tools/aquatone")

	print "[+] Stage04: collecting links"
	with open(domainlist) as f:
		for line in f:
			for word in line.split():
				print word
				command = "wget -r "+word+" -o "+word+"_asdf.txt"
				#os.system("wget -r "+word+" -o "+word+"_asdf.txt")
				os.system(command)
	os.system("cat *_asdf.txt | grep http | cut -d' ' -f4 | grep // >> "+target+"_all_subdomains_links.txt")
	print "[+] Cleaning!"
	os.system("rm -r *."+target)
	os.system("rm -r *_asdf*")
