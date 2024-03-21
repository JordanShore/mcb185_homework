#83kozak.py by Jordan Shore
#
#This program prints the Kozak Sequence 
#position weight matrix in E.Coli in the Transfac format

import mcb185
import json
import gzip
import sys
import dogma
import re


#This adds the counts of an instance of a sequence to the 
#pwm for the overall weights of acgt
'''
pwm is a list full of dictionaries with 'acgt' keys
The index in the list for each dictionary
represents that position in the sequence
'''

#Take in gbff file to analyze and initialize variables
filename = sys.argv[1]
kozac_oglocs = []
kozac_complocs = []
kozac_list = []
kozac_pwm = []
atseq = False
startpat = '[1234567890]{1,}\.\.[1234567890]{1,}'

#This goes through the file and collects;
	#id, ac, cc, rep
#Also makes a list of all the Kozac sequences
with gzip.open(filename, 'rt') as file:
	
	for line in file:

#Collect ac, cc, rep information. de uses all 3.
		if "VERSION" in line:
			line = line.split()
			ec_ac = line[1]
		elif "ORGANISM" in line:
			line = line.split()
			ec_cc = {"ORGANISM" : " ".join(line[1:])}
		elif "DBLINK" in line:
			line = line.split()
			ec_rep = "".join(line[1:])

#Gather CDS locations
#There are normal, complement, join, and complement join
#All handled by re.search() WHILE loop
		if line[5:8] == "CDS":
			line = line.split()
			cdsloc = line[1]
			mstart = re.search(startpat, cdsloc)
			while mstart != None:
				regions = mstart.group(0).split("..")			
				if 'complement' in cdsloc:
					kozac_complocs.append(int(regions[1]))
				else:
					kozac_oglocs.append(int(regions[0]))
				gonext = cdsloc.find(mstart.group(0)) + len(mstart.group(0))
				cdsloc = cdsloc[gonext:]
				mstart = re.search(startpat, cdsloc)

#Storing the DNA sequence		
		if "ORIGIN" in line:
			atseq = True
			og_seq = ""
		elif atseq == False:
			continue
		elif atseq == True:
			og_seq += dogma.clean_line(line)

#Switch from lower to upper and back because revcomp takes uppercase
rev_seq = dogma.revcomp(og_seq.upper()).lower()

#print(kozac_oglocs)
count = 0

#FOR loops add kozac sequences based on their respective dna strand
for loc in kozac_oglocs:
	kozac_list.append(og_seq[loc-10:loc+4])

for loc in kozac_complocs:
	loc = len(rev_seq)-loc
	kozac_list.append(rev_seq[loc-9:loc+5])
	
#Makes a pwm for the kozac sequences.		
kozac_pwm = dogma.make_pwm(kozac_list[0])

#Iterates through the list of kozac sequences and 
#adds the values to the pwm.
for kozac_string in kozac_list:
	kozac_pwm = dogma.addto_pwm(kozac_string.upper(), kozac_pwm)

#Put everything in transfac format
kozac_transfac = dogma.make_transfac("ECKOZ", kozac_pwm, ec_ac, ec_cc, ec_rep)
dogma.print_transfac(kozac_transfac)

		

