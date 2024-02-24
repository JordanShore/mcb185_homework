#62skewer.py by Jordan Shore
#
#This program prints gc_comp and gc_skew for a sequence.
import dogma
import gzip
import sys

path = sys.argv[1]
windowsize = int(sys.argv[2])

with gzip.open(path, "rt") as file:
	count = 0
	seq = ""
	for line in file:
		#IF statement uses count to skip the first line
		count += 1
		if count<2:
			continue
		else:
		#Iterates through each nucleotide in the 81 nucleotide lines
		#Appends them to the nucleotidelist
			line = line.strip()
			for nuc in line:
					seq = seq + nuc

#windowsize of 10 as in HW61
#This chunk prints the starting gc_comps and skew using dogma
start = 0
end = start + windowsize
window = seq[start:end]
start_gccomp = dogma.gc_comp(window)
start_gcskew = dogma.gc_skew(window)
print(0, start_gccomp, start_gcskew)

ccount = window.count('C') 
gcount = window.count('G')

for i in range(len(seq)-windowsize):

	if window[0] == 'C':
		ccount -= 1
	elif window[0] == 'G':
		gcount -= 1
	
	start += 1
	end += 1 
	window = seq[start:end]

	if window[-1] == 'C':
		ccount += 1
	elif window[-1] == 'G':
		gcount += 1 

	current_gccomp = (ccount + gcount) / len(window)
	if ccount == gcount:
		current_gcskew = 0
	else:
		current_gcskew = (gcount - ccount) / (gcount + ccount)

	print(i, current_gccomp, current_gcskew)



