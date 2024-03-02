#73missingkmers.py by Jordan Shore
#
#This program counts the various types of sequences in a GFF file. 

import mcb185
import sys
import gzip
import itertools
import dogma

#Initialize variables for the while loop.
#Count is just for testing. 
k = 1
count = 0
kmer_present = True
print("Missing kmers:")

'''
This WHILE loop finds the smallest nonexistent kmer,
then prints all kmers with 0 appearances in the dictionary.
k is the current size of kmer we are checking.

The first FOR loop finds all kmers and reverse kmers and 
adds their counts to the kcount dictionary.

The second FOR loop checks if the every iteration of kmers length k 
is in kcount. Once it has found a kmer combo not in kcount,
kmer_present is set to false and the WHILE loop ends.
The second FOR loop prints all kmers of that length not in kcount.
'''
while kmer_present == True:
	kcount = {}

	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		rseq = dogma.revcomp(seq)
		for i in range(len(seq) -k +1):
			kmer = seq[i:i+k]
			rkmer = rseq[i:i+k]
			if kmer not in kcount: 
				kcount[kmer] = 0
			if rkmer not in kcount: 
				kcount[rkmer] = 0
			kcount[kmer] += 1
			kcount[rkmer] += 1

	for nts in itertools.product('ACGT', repeat=k):
		curr_kmer = ''.join(nts)
		if curr_kmer in kcount: 
			continue
		else:             
			kmer_present = False
			print(curr_kmer)
			#count += 1
	k += 1
#print(count)