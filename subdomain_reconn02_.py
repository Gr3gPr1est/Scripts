import os
import sys
from sys import argv

target = argv[1]

print """
=========================
 SUBDOMAIN_RECONN_02_.py
=========================
"""

os.system("python /home/bughunter/Tools/Sublist3r/sublist3r.py -d "+target+" -o sublist3r.txt")
os.system("cat sublist3r.txt | /home/bughunter/Tools/httprobe/httprobe >> sublist3r_httprobe.txt")
os.system("rm -r sublist3r.txt")
os.system("cat sublist3r_httprobe.txt | cut -d'/' -f3 | sort -u  >> sublist3r_subd.txt")
os.system("rm -r sublist3r_httprobe.txt")

os.system("python /home/bughunter/Dev/hunter_b/subdomain_list_generator_.py /home/bughunter/Data/subdomain_brute_wordlists/sublazer_world_top_1000.txt "+target+" >> generated_subd.txt")
os.system("cat generated_subd.txt | /home/bughunter/Tools/httprobe/httprobe >> asdf.txt")
os.system("rm -r generated_subd.txt")
os.system("cat asdf.txt | cut -d'/' -f3 | sort -u  >> generated_subd.txt")
os.system("rm -r asdf.txt")

os.system("cat generated_subd.txt >> sorted_subd_list_.txt")
os.system("cat sublist3r_subd.txt >> sorted_subd_list_.txt")
os.system("sort -u sorted_subd_list_.txt >> subd_list.txt")

os.system("rm -r sorted_subd_list_.txt")
os.system("rm -r generated_subd.txt")
os.system("rm -r sublist3r_subd.txt")

print """
================
|    ALTDNS    |
================
"""
os.system("altdns -t 5000 -i subd_list.txt -o altdns_data_output -w /home/bughunter/Data/subdomain_brute_wordlists/sublazer_world_top_500.txt -r -s altdns_result_output.txt")
os.system("cat altdns_result_output.txt | cut -d':' -f1 >> altdns_result_output2.txt" )

os.system("rm -r altdns_data_output")

os.system("cat altdns_result_output2.txt >> subdomains.txt")
os.system("cat subd_list.txt >> subdomains.txt")
os.system("sort -u subdomains.txt >> subdomains00.txt")

os.system("rm -r subdomains.txt")
os.system("rm -r subd_list.txt")
os.system("rm -r altdns_result_output.txt")
os.system("cat subdomains00.txt | /home/bughunter/Tools/httprobe/httprobe >> subdomains_httprobe.txt")

print "=================="
print "|     AQUATONE   |"
print "=================="
#os.system("cat subdomains_httprobe.txt | /home/bughunter/Tools/aquatone")
