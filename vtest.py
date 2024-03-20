import mcb185
import json
import sys
import gzip

'''
count = 0
filename = sys.argv[1]
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline)
'''

filename = sys.argv[1]
with gzip.open(filename, 'rt') as file:
	for line in file:
		if "RNASeq_splice" in line:
			line = line.split()
			print(line)

