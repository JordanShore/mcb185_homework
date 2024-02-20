#53genomestat.py by Jordan Shore
#
#This program reports stats for a genome using functions for lists.

import sys
import math
import gzip

#The following functions return attributes for a list.
#Count
def listcount(vals):
	count = 0
	for element in vals:
		count += 1
	return count
#Min and Max
def minmax(vals):
   mini = vals[0]
   maxi = vals[0]
   for val in vals:
       if val < mini: mini = val
       if val > maxi: maxi = val
   return mini, maxi
#Mean
def mean(vals):
   total = 0
   for val in vals: total += val
   return total / len(vals)
#Median
def median(vals):
	vals.sort()
	if len(vals) % 2 == 1:
		med = vals[len(vals) // 2]
	else:
		med = (vals[len(vals) // 2] + vals[len(vals)//2 - 1]) / 2
	return med
#StDev
def stdev(vals):
	devsum = 0
	for val in vals:
		devsum += (val - mean(vals))**2
	stdev = math.sqrt(devsum / listcount(vals))
	return stdev

#Take path and feature from command line.
path = sys.argv[1]
feature = sys.argv[2]

processlist = []
with gzip.open(path, "rt") as file:
	for line in file:
		words = line.split()
		if words[2] == feature:	
			start = int(words[3])
			end = int(words[4])
			featurelength = (end - start + 1)
			processlist.append(featurelength)

ucount = listcount(processlist)
umin,umax = minmax(processlist)
umean = mean(processlist)
ustdev = stdev(processlist)
umed = median(processlist)

featurelist=[]
featurelist.append(int(ucount // 1))
featurelist.append(int(umin // 1))
featurelist.append(int(umax // 1))
featurelist.append(int(umean // 1))
featurelist.append(int(ustdev // 1))
featurelist.append(int(umed // 1))

for attribute in featurelist:
	print(attribute," | ",sep="",end="")





