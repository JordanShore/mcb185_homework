#60demo.py by Jordan Shore
#
#This program uses mcb185 to read FASTA files. 


import mcb185
import sys

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline[:30], seq[:40], len(seq))