# 43randomdna.py by Jordan Shore
#
# This program generates random DNA sequences in FASTA format.

import random

sequences = 3

#Outer FOR loop prints formatted identifier for the sequence. 
#Inner FOR loop prints 50-60 random nucleotides.
for i in range(0,sequences):
	print(f">seq-{i+1}")
	for n in range(random.randint(50,60)):
		print(random.choice('ACGT'), end = '')
	print()
