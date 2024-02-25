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
		#For testing with less than whole genome.
		#elif len(seq)>20000:
			#break
		else:
#Iterates through each nucleotide in the 81 nucleotide lines
#Appends them to the nucleotidelist
			line = line.strip()
			for nuc in line:
					seq = seq + nuc



rseq = dogma.revcomp(seq)

fseq1,fseq2,fseq3 = dogma.orfs(seq)
rseq1,rseq2,rseq3 = dogma.orfs(rseq)

sequencelist = [fseq1,fseq2,fseq3,rseq1,rseq2,rseq3]
titlelist = title.split()

numprotein = 1
for seq in sequencelist:
	temptranscript = dogma.translate(seq)

	potentialstart = 0
	potentialend = 0

	while (potentialstart != -1) and (potentialend != -1):
		potentialstart = temptranscript.find("M")
		rest = temptranscript[potentialstart:]
		potentialend = rest.find("*")

		if potentialend >= minprotein_size:
			print(titlelist[0]+"-prot-"+str(numprotein))
			print(temptranscript[potentialstart:potentialstart+potentialend])
			numprotein += 1
		
		temptranscript = temptranscript[potentialstart+potentialend:]


