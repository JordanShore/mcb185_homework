#64profinder.py by Jordan Shore
#
#This program reports proteins in a DNA sequence.

import dogma
import gzip
import sys
import mcb185

#Command line inputs
path = sys.argv[1]
minprotein_size = int(sys.argv[2])

#Opening file and creating the sequence
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	seq = seq[1000:4000]
	title = defline[:11]
	#Creates the reading frames, 3 forward 3 back and puts them in a list.
	defline = defline.strip()
	sequencelist = dogma.frseqs(seq)
	#The first part of title list will be used for protein titles.

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
				print(">" + title +"-prot-"+str(numprotein))
				print(temptranscript[potentialstart:potentialend])
				numprotein += 1
			
			temptranscript = temptranscript[potentialend+1:]


