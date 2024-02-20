#55colorname.py by Jordan Shore
#
#This program reports stats for a genome using functions for lists.

import sys
import gzip

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

#This FOR loop will go through the file find the closest color to the RGB values given.
mindist = 1000
with open(colorfile) as file:
	for line in file:
		words = line.split()
		vals = words[2].split(",")
		dist = abs(int(vals[0])-R)+abs(int(vals[1])-G)+abs(int(vals[2])-B)

		if dist < mindist:
			mindist = dist
			closestcolor = words[0]
	
print(closestcolor)
			