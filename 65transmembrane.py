#65transmembrane.py by Jordan Shore
#
#This program predicts which proteins in a proteome are transmembrane.

import dogma
import gzip
import sys
import mcb185

'''
The big FOR loop will go through and evaluate;
The signal and transmembrane regions.
If both are valid, it will set signal and transmembrane to True.
Then and only then will it print the defline for the protein.

There are two similar Inner FOR loops.
Both evaluate all windows of a various length within their regions for;
1. High enough average KD hydrophobicity
2. No Prolines

Innermost FOR loops are just calculating window averages.
'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	signal = False
	transmembrane = False
	signalregion = seq[:30]
	transmembraneregion = seq[30:]

#Inner FOR loop sp.
	spwindowsize = 8
	spstart = 0
	spend = spstart + spwindowsize
	spwindow = signalregion[spstart:spend]

	#Loops through each window
	for i in range(len(signalregion)-spwindowsize):

		#Calculate average KD hydrophobicity within window.
		spwindowkd = 0
		for aa in spwindow:
			spwindowkd = spwindowkd + dogma.kd_hydrophobicity(aa)
		avgspwindowkd = spwindowkd / 8

		#Is this window valid? If so, we are done, break.
		if avgspwindowkd >= 2.5 and spwindow.find("P") == -1:
			signal = True
			break

#Start and End increment changes the window
		spstart += 1
		spend += 1 
		spwindow = signalregion[spstart:spend]

#Inner FOR loop tr.
	trwindowsize = 11
	trstart = 0
	trend = trstart + trwindowsize
	trwindow = transmembraneregion[trstart:trend]

	#Loops through each window
	for i in range(len(signalregion)-trwindowsize):

		#Calculate average KD hydrophobicity within window.
		trwindowkd = 0
		for aa in trwindow:
			trwindowkd = trwindowkd + dogma.kd_hydrophobicity(aa)
		avgtrwindowkd = trwindowkd / 11

		#Is this window valid? If so, we are done, break.
		if avgtrwindowkd >= 2 and trwindow.find("P") == -1:
			transmembrane = True
			break

#Start and End increment changes the window
		trstart += 1
		trend += 1 
		trwindow = transmembraneregion[trstart:trend]


	if signal == True and transmembrane == True:
		print(defline)

