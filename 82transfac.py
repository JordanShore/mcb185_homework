#82transfac.py by Jordan Shore
#
#This program 

import mcb185
import gzip
import sys
import re

def read_transfac(filename):
	count = 0
	file = gzip.open(filename, 'rt')
	for line in file:
		count += 1
		matrix_here == False
		if count > 10: 
			break
		else:
			line = line.split()
			if line[0] == "ID":
				line = line.split()
				identification = line[1]
			elif line.[0] == "PO":
				matrix_here == True
			while matrix_here == True:
				#append acgt counts
	print(identification)


read_transfac(sys.argv[1])