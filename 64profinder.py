#64profinder.py by Jordan Shore
#
#This program reports proteins in a DNA sequence.

import dogma
import gzip
import sys

#Command line inputs
path = sys.argv[1]
minprotein_size = int(sys.argv[2])

#Opening file and creating the sequence
with gzip.open(path, "rt") as file:
	count = 0
	seq = ""
	for line in file:
		#IF statement uses count to skip the first line
		count += 1
		if count == 1:
			title = line
		else:
		#Iterates through each nucleotide in the 81 nucleotide lines
		#Appends them to the nucleotidelist
			line = line.strip()
			for nuc in line:
					seq = seq + nuc


#This chunk creates the starting state of window and finalseq

windowsize = 3
start = 0
end = start + windowsize
window = seq[start:end]

aaseq = dogma.translate(seq)



