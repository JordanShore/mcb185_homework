#72kmercount.py by Jordan Shore
#
#This program counts the various types of sequences in a GFF file. 

import mcb185
import sys
import gzip
import itertools

k = int(sys.argv[2])
kcount = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1
#for kmer, n in kcount.items(): print(kmer, n)

for nts in itertools.product('ACGT', repeat=k):
	akmer = ''.join(nts)
	if akmer in kcount: 
		print(akmer, kcount[akmer])
	else:
		print(akmer, 0)