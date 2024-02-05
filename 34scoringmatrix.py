# 34scoringmatrix.py by Jordan Shore
#
# This program prints a scoring matrix for nucleotide match/mismatch.


alphabet = 'ACGT'
match = '+1'
mismatch = '-1'

#This prints the first line of the scoring matrix.
print(" ", end = ' ')
for letter in alphabet:
	print("", letter, end = ' ')
print()

#These nested FOR loops print a +1/-1 for each letter 
#The empty print() at the end of the line skips to the next line to create the matrix shape.
for outerletter in alphabet:
	print(outerletter, end = ' ')
	for innerletter in alphabet:
		if innerletter == outerletter:
			print(match, end = ' ')
		else:
			print(mismatch, end = ' ')
	print()

