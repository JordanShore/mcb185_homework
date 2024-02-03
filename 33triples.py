# 33triples.py by Jordan Shore
#
# This program finds pythagorean triples. 

import math


limit = 10
#i+1 avoids repeats and major diagonal since that always gives hypothenuse = side*sqrt(2).
for i in range(1, limit):
	for j in range(i+1, limit):
		print(i, j, 'c')

