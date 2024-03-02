#65transmembrane.py by Jordan Shore
#
#This program predicts which proteins in a proteome are transmembrane.

import dogma
import gzip
import sys
import mcb185

#is_hydrophobic_region evaluates whether
#1: The average KD hydrophobicity of any window of a specified size is;
	# >= minave_kdh
#2: There are no prolines in that window
#If both then returns tmr = True, else False
def is_hydrophobic_region(region, minave_kdh, windowsize):
	start = 0
	tmr = False
	end = start + windowsize
	window = region[start:end]

	for i in range(len(region)-windowsize):
#Loops through each window
		tot_window_kdh = 0
		for aa in window:
			tot_window_kdh = tot_window_kdh + dogma.kd_hydrophobicity(aa)
		avg_window_kdh = tot_window_kdh / windowsize

		if avg_window_kdh >= minave_kdh and window.find("P") == -1:
			tmr = True
			break

#Start and End increment changes the window
		start += 1
		end += 1 
		window = signalregion[start:end]

	return tmr

#Checks if the signal and transmembrane regions are hydrophobic.
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	signal = False
	transmembrane = False
	signalregion = seq[:30]
	transmembraneregion = seq[30:]

	signal = is_hydrophobic_region(signalregion, 2.5, 8)
	transmembrane = is_hydrophobic_region(transmembraneregion, 2, 11)

	if signal == True and transmembrane == True:
		print(defline)

