#84splicesites.py by Jordan Shore
#
#This program prints the Splice Site 
#position weight matrixes for any organisms
#given you have .gff and .fa files for each

import mcb185
import json
import gzip
import sys
import dogma
import re

#splice_loc_list is a list of lists that have
#[chromosome,strand,donor,acceptor] for each element in the outer list
def extract_splicelocs(gff_file):
	splice_loc_list = []

	with gzip.open(gff_file, 'rt') as file:
		for line in file:
			if "RNASeq_splice" in line:
				line = line.split()
				splice_loc_list.append([line[0],line[6],int(line[3]),int(line[4])])

	return splice_loc_list

#Gets the chromosome sequences from a .fa file as 
#{Chrom1 : [fseq,rseq]}
def extract_chromosomes(fa_file):
	chrom_dict = {}
	for defline, seq in mcb185.read_fasta(fa_file):
		defline = defline.split()
		chrom_dict[defline[0]] = [seq, dogma.revcomp(seq)]

	return chrom_dict

#Gets the donor and acceptor splice sequences using dict built above.
def get_splice_seqs(splice_loc_list, chrom_dict):
	donor_list = []
	acceptor_list = []

	for curr_chromosome, pos_neg, beg, end in splice_loc_list:

		if pos_neg == '+':
			lookinside = chrom_dict[curr_chromosome][0]
			donor_list.append(lookinside[beg-5:beg+5])
			acceptor_list.append(lookinside[end-5:end+5])

		elif pos_neg == '-':
			lookinside = chrom_dict[curr_chromosome][1]
			foo = beg
			beg = end
			end = foo
			beg = len(lookinside) - beg
			end = len(lookinside) - end
			donor_list.append(lookinside[beg-4:beg+6])
			acceptor_list.append(lookinside[end-4:end+6])

	return acceptor_list, donor_list


#Prints the transfacs given the lists of nucleotide strings
def print_splice_transfacs(acceptor_list, donor_list):
	#Makes a pwm for the kozac sequences.		
	acceptor_pwm = dogma.make_pwm(acceptor_list[0])

	#Iterates through the list of acceptor sequences and 
	#adds the values to the pwm.
	for acceptor_string in acceptor_list:
		acceptor_pwm = dogma.addto_pwm(acceptor_string.upper(), acceptor_pwm)
	
	#Convert to proportions
	for pos in acceptor_pwm:
		tot = 0
		for value in pos.values():
			tot += value

		for key, val in pos.items():
			pos[key] = val / tot

	acceptor_transfac = dogma.make_transfac("ACC", acceptor_pwm, gff_file)
	acceptor_transfac['DE'] = 'splice acceptor'
	dogma.print_transfac_prop(acceptor_transfac)

	#Makes a pwm for the kozac sequences.		
	donor_pwm = dogma.make_pwm(donor_list[0])

	#Iterates through the list of donor sequences and 
	#adds the values to the pwm.
	for donor_string in donor_list:
		donor_pwm = dogma.addto_pwm(donor_string.upper(), donor_pwm)

	#Convert to proportions
	for pos in donor_pwm:
		tot = 0
		for value in pos.values():
			tot += value

		for key, val in pos.items():
			pos[key] = val / tot

	#Put everything in transfac format
	donor_transfac = dogma.make_transfac("DON", donor_pwm, gff_file)
	donor_transfac['DE'] = 'splice donor'
	dogma.print_transfac_prop(donor_transfac)


#The actual code, utilizing all functions defined.
gff_file = sys.argv[1]
fa_file = sys.argv[2]

#Where are the splices?
splice_loc_list = extract_splicelocs(gff_file)

#What are the Chromosome sequences?
chrom_dict = extract_chromosomes(fa_file)

#What are the actual splice sequences?
acceptors, donors = get_splice_seqs(splice_loc_list, chrom_dict)

#Print as transfac.
print_splice_transfacs(acceptors, donors)
