#74genefinder.py by Jordan Shore
#
#This program 

import mcb185
import dogma
import gzip
import sys

#Command line inputs
path = sys.argv[1]
minorf_size = int(sys.argv[2])

#Opening file and creating the sequence
with gzip.open(path, "rt") as file:
	count = 0
	seq = ""
	for line in file:
#IF statement uses count to make the first line a title
		count += 1
		if count == 1:
			title = line
		For testing with less than whole genome.
		elif len(seq)>2000:
			break
		else:
#Iterates through each nucleotide in the 81 nucleotide lines
#Appends them to the nucleotidelist
			line = line.strip()
			for nuc in line:
					seq = seq + nuc
