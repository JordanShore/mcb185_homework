#dogma.py by Jordan Shore
#
#This is a library for Central Dogma functions. 

import gzip
import sys
import re
import mcb185

def transcribe(dna):
	return dna.replace('T', 'U')

def orfs(seq):
	seq1 = seq[:]
	seq2 = seq[1:]
	seq3 = seq[2:]
	return seq1, seq2, seq3

def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:           rc.append('N')
	return ''.join(rc)

def frseqs(seq):
	rseq = revcomp(seq)
	fseq1, fseq2, fseq3 = orfs(seq)
	rseq1, rseq2, rseq3 = orfs(rseq)
	return [fseq1, fseq2, fseq3, rseq1, rseq2, rseq3]

def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)

def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)

def hydropathy(seq):
	kdh = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5,
	'M':  1.9, 'A':  1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
	'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
	'Q': -3.5, 'D': -3.5, 'K': -3.9, 'N': -3.5, 'R': -4.5,
	}
	s = 0
	for aa in seq:
		s += kdh[aa]
	return s / len(seq)

#Done beautifully by ChatGPT
def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i + 3]
		if codon == 'TTT' or codon == 'TTC':
			aas.append('F')
		elif codon == 'TTA' or codon == 'TTG' or codon == 'CTT' or codon == 'CTC':
			aas.append('L')
		elif codon == 'CTA' or codon == 'CTG':
			aas.append('L')
		elif codon == 'ATT' or codon == 'ATC' or codon == 'ATA':
			aas.append('I')
		elif codon == 'ATG':
			aas.append('M')
		elif codon == 'GTT' or codon == 'GTC' or codon == 'GTA' or codon == 'GTG':
			aas.append('V')
		elif codon == 'TCT' or codon == 'TCC' or codon == 'TCA' or codon == 'TCG':
			aas.append('S')
		elif codon == 'CCT' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
			aas.append('P')
		elif codon == 'ACT' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
			aas.append('T')
		elif codon == 'GCT' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
			aas.append('A')
		elif codon == 'TAT' or codon == 'TAC':
			aas.append('Y')
		elif codon == 'TAA' or codon == 'TAG':
			aas.append('*')
		elif codon == 'CAT' or codon == 'CAC':
			aas.append('H')
		elif codon == 'CAA' or codon == 'CAG':
			aas.append('Q')
		elif codon == 'AAT' or codon == 'AAC':
			aas.append('N')
		elif codon == 'AAA' or codon == 'AAG':
			aas.append('K')
		elif codon == 'GAT' or codon == 'GAC':
			aas.append('D')
		elif codon == 'GAA' or codon == 'GAG':
			aas.append('E')
		elif codon == 'TGT' or codon == 'TGC':
			aas.append('C')
		elif codon == 'TGA':
			aas.append('*')
		elif codon == 'TGG':
			aas.append('W')
		elif codon == 'CGT' or codon == 'CGC' or codon == 'CGA':
			aas.append('R')
		elif codon == 'CGG':
			aas.append('R')
		elif codon == 'AGT' or codon == 'AGC':
			aas.append('S')
		elif codon == 'AGA' or codon == 'AGG':
			aas.append('R')
		elif codon == 'GGT' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
			aas.append('G')
		else:
			aas.append('X')

	return ''.join(aas)


#From HW 25.
# 25entropy.py by Jordan Shore
#
# This program contains a function that calculates Shannon Entropy,
# for DNA Nucleotides. 

import math

#Parameters are A, C, G, T counts.
#Returns Shannon Entropy.
def shannon_entropy(a, c, g, t):
	tot = a + c + g + t
#These IF / ELSE statements set the statement for each variable equal to 0;
# if the count is 0.
#If a letter count is 0, then it would cause and error when taking a log.
#But since it still accounts for 0 of the entropy, 
# it needs to be counted as 0. 
	if a != 0:
		shannona = (a / tot) * math.log2(a / tot)
	else:
		shannona = 0

	if c != 0:
		shannonc = (c / tot) * math.log2(c / tot)
	else:
		shannonc = 0

	if g != 0:
		shannong = (g / tot) * math.log2(g / tot)
	else:
		shannong = 0

	if t != 0:
		shannont = (t / tot) * math.log2(t / tot)
	else:
		shannont = 0

	entropy = -1*(shannona + shannonc + shannong + shannont)

	return entropy



#From HW 24
def kd_hydrophobicity(aa):
	if   aa == "A" : hpb = 1.8
	elif aa == "C" : hpb = 2.5
	elif aa == "D" : hpb = -3.5
	elif aa == "E" : hpb = -3.5
	elif aa == "F" : hpb = 2.8
	elif aa == "G" : hpb = -0.4
	elif aa == "H" : hpb = -3.2
	elif aa == "I" : hpb = 4.5
	elif aa == "K" : hpb = -3.9
	elif aa == "L" : hpb = 3.8
	elif aa == "M" : hpb = 1.9
	elif aa == "N" : hpb = -3.5
	elif aa == "P" : hpb = -1.6
	elif aa == "Q" : hpb = -3.5
	elif aa == "R" : hpb = -4.5
	elif aa == "S" : hpb = -0.8
	elif aa == "T" : hpb = -0.7
	elif aa == "V" : hpb = 4.2
	elif aa == "V" : hpb = 4.2
	elif aa == "W" : hpb = -0.9
	elif aa == "Y" : hpb = -1.3
	else:
		hpb = "na"
		print("Error Invalid Amino Acid. Use a capitalized single character.")

	return hpb


def print_asfasta(defline, seq):
	print('>' + defline)
	for i in range(0, len(seq), 60):
		print(seq[i:i+60])

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
def proteins_list(seq, minprotein_size):
	potentialstart = 0
	potentialend = 0
	proteins = []
	aaseq = translate(seq)
	while (potentialstart != -1) and (potentialend != -1):
		potentialstart = aaseq.find("M")
		potentialend = aaseq.find("*")

		if potentialend - potentialstart >= minprotein_size:
			proteins.append(aaseq[potentialstart:potentialend])
		
		aaseq = aaseq[potentialend+1:]

	return proteins

#Protein_indexes returns lists of the start and ends of all proteins,
#within the DNA sequence.
def protein_indexes(aaseq, proteins_list):
	protein_locs = []
#This FOR loop iterates through a list of proteins.
#Then will find their locations within the amino acid sequence.
	for i in range(len(proteins_list)):
		start = 0 
		end = 0
#Duplicate_count accounts for the same protein appearing in multiple counts.
#It says, in the list so far, how many of this protein are there?
#That way aaseq.find() searches for the nth place where this duplicate appears.
		duplicate_count = proteins_list[:i+1].count(proteins_list[i])
		start = aaseq.find(proteins_list[i], duplicate_count) * 3
		end = start + (len(proteins_list[i]) * 3)
		protein_locs.append([start, end])

	return protein_locs


#Cleans a line of the sequence of a gbff file
#returns only string of nucleotides.
def clean_line(line):
	cleaned = ""
	line = line.split()
	cleaned = "".join(line[1:])
	return cleaned

#Makes a pwm list of length equal to the number of 
#nucleotides in your example sequence with all weights = 0
def make_pwm(example):
	pwm = []
	for nucleotide in example:
		pwm.append({'A': 0, 'C': 0, 'G': 0,'T': 0})

	return pwm


'''
#OuterDictionary
ID = Key : MiddleDictionary = Value
#MiddleDictionary
'id' = Key : ID = Value, 'pwm' = Key : InnerList = Value, 
'AC'/'DE' etc... = Key : AC/DE = Value, 'CC' = Key : InnerDictionary = 'Value'
#InnerDictionary
'tax_group'/'tf_class' etc... = Key : TAX_GROUP/TF_CLASS = Value
#InnerList
InnermostDictionary = Element
#InnermostDictionary
'ACGT' = Key : Float = Value
'''
#extract_transfac extracts all the relevant information from a transfac file.
#Extras is a dictionary that holds AC/DE etc... until the end of round,
#denoted by '//', because ID is not the first piece of information given.
def extract_transfac(filename):
	count = 0
	transfac_object = {}
	matrix_here = False
	extras = {}
	with gzip.open(filename, 'rt') as file:
		for line in file:
			count += 1
			line = line.split()
			if line[0] == "//":
				for key in extras:
					transfac_object[identification][key] = extras[key]
				extras = {}
			elif line[0] == "ID":
				identification = line[1]
				transfac_object[identification] = {}
				transfac_object[identification]['CC'] = {}
				transfac_object[identification]['ID'] = identification
				transfac_object[identification]['pwm'] = []
			elif line[0] == "PO":
				matrix_here = True
			elif line[0] == "XX":
				matrix_here = False
			elif matrix_here == True:
				transfac_object[identification]['pwm'].append({
				"A":line[1],
				"C":line[2],
				"G":line[3],
				"T":line[4],
				})
			elif line[0] == "CC":
				info = line[1].split(":")
				infokey = info[0]
				infovalue = info[1] 
				transfac_object[identification]['CC'][infokey] = infovalue
			else:
				extras[line[0]] = "".join(line[1:])
			#print(count)
			#if count > 100:
				#break
	#print(json.dumps(id_matrix_dictionary, indent = 4))
	return transfac_object		

#Makes a transfac instance assuming;
	#cc contains a dictionary
	#pwm contains a list of dictionaries
def make_transfac(tid, pwm, ac = 'NA', cc = 'NA', rep = 'NA'):
	transfac_singular = {}
	transfac_singular['ID'] = tid
	transfac_singular['AC'] = ac
	transfac_singular['CC'] = cc
	transfac_singular['DE'] = ac + ' ' + tid + ' ; ' + 'From ' + rep
	transfac_singular['pwm'] = pwm
	return transfac_singular

def addto_pwm(instance,pwm):
	finalpwm = pwm
#instance[i] returns where we are in the sequence string
#[instance[i]] uses this as the key for the pwm dictionary
	for i in range(len(instance)):
		finalpwm[i][instance[i]] += 1

	return finalpwm

'''
#Outerdictionary
'id' = Key : ID = Value, 'pwm' = Key : InnerList = Value, 
'AC'/'DE' etc... = Key : AC/DE = Value, 'CC' = Key : MiddleDictionary = 'Value'
#MiddleDictionary
'tax_group'/'tf_class' etc... = Key : TAX_GROUP/TF_CLASS = Value
#InnerList
InnerDictionary = Element
#InnerDictionary
'ACGT' = Key : Float = Value
'''
#Takes in a transfac_singular and prints in transfac format.
def print_transfac(transfac_singular):
	print('AC', transfac_singular['AC'])
	print('XX')
	print('ID', transfac_singular['ID'])
	print('XX')
	print('DE', transfac_singular['DE'])
	for head in ['PO','A','C','G','T']:
		print(f'{head:<8}', end = "")
	print()
	for i in range(len(transfac_singular['pwm'])):
		val_a = transfac_singular['pwm'][i]['A']
		val_c = transfac_singular['pwm'][i]['C']
		val_g = transfac_singular['pwm'][i]['G']
		val_t = transfac_singular['pwm'][i]['T']
		for head in [i+1,val_a,val_c,val_g, val_t]:
			head = float(head)
			print(f'{head:<8.0f}', end = "")
		print()
	print('XX')
	if (transfac_singular['CC'] != 'NA'):
		for cc_key,cc_value in transfac_singular['CC'].items():
			print('CC',cc_key + ":" + cc_value)
	else: 
		print('CC NA')
	print('XX')
	print('//')

#Same function, but prints pwm as proportions
def print_transfac_prop(transfac_singular):
	print('AC', transfac_singular['AC'])
	print('XX')
	print('ID', transfac_singular['ID'])
	print('XX')
	print('DE', transfac_singular['DE'])
	for head in ['PO','A','C','G','T']:
		print(f'{head:<8}', end = "")
	print()
	for i in range(len(transfac_singular['pwm'])):
		val_a = transfac_singular['pwm'][i]['A']
		val_c = transfac_singular['pwm'][i]['C']
		val_g = transfac_singular['pwm'][i]['G']
		val_t = transfac_singular['pwm'][i]['T']
		for head in [i+1,val_a,val_c,val_g, val_t]:
			if head == i+1:
				print(f'{head:<8.0f}', end = "")
			else:
				head = float(head)
				print(f'{head:<8.3f}', end = "")
		print()
	print('XX')
	if (transfac_singular['CC'] != 'NA'):
		for cc_key,cc_value in transfac_singular['CC'].items():
			print('CC',cc_key + ":" + cc_value)
	else: 
		print('CC NA')
	print('XX')
	print('//')

#Prints a fasta file using soft or hardmasking based on entropy
def print_enmask(path, windowsize, enthreshold, soft):
	if soft == 'True':
		soft = True
	elif soft == 'False':
		soft = False

	for defline, seq in mcb185.read_fasta(path):
		start = 0
		end = start + windowsize
		window = seq[start:end]
		finalseq = window


	#The following does the first check for a low entropy window
	#On only the first window

		acount = window.count('A')
		ccount = window.count('C') 
		gcount = window.count('G')
		tcount = window.count('T')
		entropy = shannon_entropy(acount, ccount, gcount, tcount)


	#For loop just building a string of Ns the size of the window

		nstring = ""
		for i in range(windowsize):
			nstring += "N"


	#Make the first window into Ns 

		if (entropy < enthreshold) and (soft == False):
			finalseq = nstring
		elif (entropy < enthreshold) and (soft == True):
			finalseq = window.lower()

	#Loops through each window
		for i in range(len(seq)-windowsize):
			acount = window.count('A')
			ccount = window.count('C') 
			gcount = window.count('G')
			tcount = window.count('T')

			entropy = shannon_entropy(acount, ccount, gcount, tcount)

	#Start and End increment changes the window
			start += 1
			end += 1 
			window = seq[start:end]


	#Now we append one at a time, either N or the nucleotide

			if (entropy < enthreshold) and (soft == False):
				finalseq += "N"
			elif (entropy < enthreshold) and (soft == True):
				finalseq += window[-1].lower()
			else:
				finalseq += window[-1]


		print_asfasta(defline, finalseq)
