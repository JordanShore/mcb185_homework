#62skewer.py by Jordan Shore
#
#This program prints gc_comp and gc_skew for a sequence.
import dogma
import gzip

path = "GCF_000005845.2_ASM584v2_genomic.fna.gz"
with gzip.open(path, "rt") as file:
	count = 0
	seq = ""
	for line in file:
		#IF statement uses count to skip the first 1000 lines
		count += 1
		if count<1000:
			continue
		#Adds a total of 1000 nucleotides
		elif len(seq)>1000:
			break
		else:
		#Iterates through each nucleotide in the 81 nucleotide lines
		#Appends them to the nucleotidelist
			line = line.strip()
			for nuc in line:
				seq = seq + nuc
#print(seq)

start = 0
end = 3
window = seq[start:end]
windowsize = 10
start_gccomp = dogma.gc_comp(window)
start_gcskew = dogma.gc_skew(window)
print(start_gccomp)
print(start_gcskew)

ccount = window.count('C') 
gcount = window.count('G')

current_gccomp = (ccount + gcount) / len(window)
	if ccount == gcount:
		current_gcskew = 0
	else:
		current_gcskew = (g - c) / (g + c)

for i in range(1000):

	if window[0] == 'C':
		ccount -= 1
	elif window[0] == 'G':
		gcount -= 1
	




'''
#61skewer.py by Jordan Shore
#
#This program prints gc_comp and gc_skew for a sequence
import dogma

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	print(i, dogma.gc_comp(s), dogma.gc_skew(s))
'''

