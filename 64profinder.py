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
#IF statement uses count to make the first line a title
		count += 1
		if count == 1:
			title = line
		#For testing with less than whole genome.
		#elif len(seq)>2000:
			#break
		else:
#Iterates through each nucleotide in the 81 nucleotide lines
#Appends them to the nucleotidelist
			line = line.strip()
			for nuc in line:
					seq = seq + nuc


#Creates reverse complement.
rseq = dogma.revcomp(seq)

#Creates the reading frames, 3 forward 3 back and puts them in a list.
fseq1, fseq2, fseq3 = dogma.orfs(seq)
rseq1, rseq2, rseq3 = dogma.orfs(rseq)
sequencelist = [fseq1, fseq2, fseq3, rseq1, rseq2, rseq3]

#The first part of title list will be used for protein titles.
titlelist = title.split()

#Start at protein 1 when printing proteins found later.
numprotein = 1

#FOR loop iterates through the 3 forward and reverse reading frames.
for seq in sequencelist:
#Translates the DNA sequence to amino acids
	temptranscript = dogma.translate(seq)
#Initialize where the start and ends of proteins may be.
	potentialstart = 0
	potentialend = 0

	'''
WHILE loop evaluates all the potential proteins in an aa transcript.
Each iteration evaluates a single possible protein.

potentialstart/end are found by .find("M") or .find("*")
These represent Methionine and the STOP codon.

If .find() doesn't find a start or stop it will return -1, ending the loop.

potentialend - potentialstart signifies protein length.
IF statement prints protein information and increases numprotein by 1.
numprotein is just signifying how many proteins you've found.

temptranscript if lastly changed to only be everything after the latest "*",
this way we move forward through the transcript to the next possible protein.
	'''
	while (potentialstart != -1) and (potentialend != -1):
		potentialstart = temptranscript.find("M")
		potentialend = temptranscript.find("*")

		if potentialend - potentialstart >= minprotein_size:
			print(titlelist[0]+"-prot-"+str(numprotein))
			print(temptranscript[potentialstart:potentialend])
			numprotein += 1
		
		temptranscript = temptranscript[potentialend+1:]


