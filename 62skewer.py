#62skewer.py by Jordan Shore
#
#This program prints gc_comp and gc_skew for a sequence.
#20s vs 36s for Hw 61
#Note that a lot of that time is printing either way.
import dogma
import gzip
import sys
import mcb185

windowsize = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
#This chunk prints the starting gc_comps and skew using dogma
	start = 0
	end = start + windowsize
	window = seq[start:end]
	start_gccomp = dogma.gc_comp(window)
	start_gcskew = dogma.gc_skew(window)
	print(0, start_gccomp, start_gcskew)

#Create a count variable for each letter that will be changed
	ccount = window.count('C') 
	gcount = window.count('G')

#Loops through each window
	for i in range(len(seq)-windowsize):

#IF/ELIF statements subtract or add 1 for C/G at ends of window
		if window[0] == 'C':
			ccount -= 1
		elif window[0] == 'G':
			gcount -= 1
		
#Start and End increment changes the window
		start += 1
		end += 1 
		window = seq[start:end]

		if window[-1] == 'C':
			ccount += 1
		elif window[-1] == 'G':
			gcount += 1 

#Calculations for gc comp and skew
		current_gccomp = (ccount + gcount) / len(window)
		if ccount == gcount:
			current_gcskew = 0
		else:
			current_gcskew = (gcount - ccount) / (gcount + ccount)

		print(i, current_gccomp, current_gcskew)



