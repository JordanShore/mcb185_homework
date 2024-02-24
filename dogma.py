#dogma.py by Jordan Shore
#
#This is a library for Central Dogma functions. 


def transcribe(dna):
    return dna.replace('T', 'U')

def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:           rc.append('N')
	return ''.join(rc)

def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)

def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)

#Done beautifully by ChatGPT
def translate(dna):
    aas = []
    for i in range(0, len(dna), 3):
        codon = dna[i:i + 3]
        if codon == 'TTT' or codon == 'TTC':
            aas.append('F')
        elif codon == 'TTA' or codon == 'TTG' or codon == 'CTT' or codon == 'CTC' or codon == 'CTA' or codon == 'CTG':
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
        elif codon == 'CGT' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG':
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
# This program contains a function that calculates Shannon Entropy for DNA Nucleotides. 

import math

#Parameters are A, C, G, T counts.
#Returns Shannon Entropy.
def shannon_entropy(a, c, g, t):
	tot = a + c + g + t
#These IF / ELSE statements set the statement for each variable equal to 0 if the count is 0.
#If a letter count is 0, then it would cause and error when taking a log.
#But since it still accounts for 0 of the entropy, it needs to be counted as 0. 
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