#61skewer.py by Jordan Shore
#
#This program prints gc_comp and gc_skew for a sequence
#Modified to compete with hw 62. Slower by 16 seconds.
import dogma
import sys
import gzip
'''
seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	print(i, dogma.gc_comp(s), dogma.gc_skew(s))
'''

path = sys.argv[1]
windowsize = int(sys.argv[2])

with gzip.open(path, "rt") as file:
	count = 0
	seq = ""
	for line in file:
		#IF statement uses count to skip the first line
		count += 1
		if count<2:
			continue
		else:
		#Iterates through each nucleotide in the 81 nucleotide lines
		#Appends them to the nucleotidelist
			line = line.strip()
			for nuc in line:
					seq = seq + nuc


for i in range(len(seq) -windowsize +1):
	s = seq[i:i+windowsize]
	currentgc_comp = dogma.gc_comp(s)
	currentgc_skew = dogma.gc_skew(s)
	print(i, currentgc_comp, currentgc_skew)

