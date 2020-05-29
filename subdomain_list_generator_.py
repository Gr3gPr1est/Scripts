import sys
import os
from sys import argv

author = """
	=============
 	 Greg_Priest
	=============
   ========================
     papgergo89@gmail.com
   ========================
"""

wordlist = argv[1]
domain = argv[2]

with open(wordlist) as a:
	for line in a:
		for word in line.split():
			print word+"."+domain
