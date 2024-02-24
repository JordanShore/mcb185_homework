#63dust.py by Jordan Shore
#
#This program changes a FASTA file to have N for low complexity regions.

import dogma
import gzip
import sys

#Command line inputs
path = sys.argv[1]
windowsize = int(sys.argv[2])
enthreshold = float(sys.argv[3])


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
entropy = dogma.shannon_entropy(acount,ccount,gcount,tcount)


#For loop just building a string of Ns the size of the window

nstring = ""
for i in range(windowsize):
	nstring += "N"


#Make the first window into Ns 

if entropy < enthreshold:
	finalseq = nstring

#Loops through each window
for i in range(len(seq)-windowsize):
	acount = window.count('A')
	ccount = window.count('C') 
	gcount = window.count('G')
	tcount = window.count('T')

	entropy = dogma.shannon_entropy(acount,ccount,gcount,tcount)

#Start and End increment changes the window
	start += 1
	end += 1 
	window = seq[start:end]


#Now we append one at a time, either N or the nucleotide

	if entropy < enthreshold:
		finalseq += "N"
	else:
		finalseq += window[-1]


#Print like a FASTA file
print(title, end = "")
for i in range(0,len(finalseq),60):
	print(finalseq[i:i+60])



