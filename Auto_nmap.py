  GNU nano 4.5                                                      Auto_put.py                                                       Modified  

print '''
############################
#######    Auto_.py    #####
#######  Greg Priest   #####
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
                        os.system("nmap -sV -PN "+word+" >> grab_nmap.txt")
