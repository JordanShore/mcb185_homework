#74genefinder.py by Jordan Shore
#
#This program finds all protein locations on the + and - strand of DNA.

import mcb185
import dogma
import gzip
import sys

#Command line inputs
path = sys.argv[1]
minprotein_size = int(sys.argv[2]) / 3

#Opening file and creating the sequence
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	#Creates the reading frames, 3 forward 3 back and puts them in a list.
	#Separates f and reverse strands to deal with separately.
	sequencelist = dogma.frseqs(seq)
	sequencelistf = sequencelist[0:3] 
	sequencelistr = sequencelist[3:]
	title = defline[:11]

#Outer FOR loop iterates through the 3 forward reading frames.
#Create amino acid sequence from DNA and list of all proteins.
	for seq in sequencelistf:
		aaseq = dogma.translate(seq)
		orf = 0
		current_proteins = dogma.proteins_list(seq, minprotein_size)
		#Inner FOR loop formats the protein print out considering the 
		#current reading frame and how that shifts 0-2 nucleotides.
		for start, end in dogma.protein_indexes(aaseq, current_proteins):
			print(title, "CDS", "{}  {} +".format(start + orf, end + orf))	
		orf += 1
	
#The reverse sequence is much the same except we have to subtract the 
#locations of the proteins from the overall length to give the + strand locs
	for seq in sequencelistr:
		aaseq = dogma.translate(seq)
		orf = 0
		current_proteins = dogma.proteins_list(seq, minprotein_size)
		for start, end in dogma.protein_indexes(aaseq, current_proteins):
			start = len(seq) - (start + orf)
			end = len(seq) - (end + orf)
			print(title,"CDS","{}  {} -".format(start, end))	
		orf += 1
				
