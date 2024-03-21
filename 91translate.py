#!/usr/bin/env python3

#91translate.py by Jordan Shore
#
#Translates transcripts from anywhere

import argparse
import dogma
import mcb185

parser = argparse.ArgumentParser(description='mRNA translator.')
parser.add_argument('file', type=str, help='fasta file of mRNAs')
parser.add_argument('-m','--min', type=int, default=100,
	help='minimum protein length')
parser.add_argument('-a','--anti', action='store_true', 
	help='also examine the anti-parallel strand')
arg = parser.parse_args()

print('translating with', arg.file, arg.min, arg.anti)

for defline, seq in mcb185.read_fasta(arg.file):
	if arg.anti == True:
		revseq = dogma.revcomp(seq)
		aaseq = dogma.translate(revseq)
	elif arg.anti == False:
		aaseq = dogma.translate(seq)

	if len(aaseq) > arg.min:
		dogma.print_asfasta(defline, aaseq)