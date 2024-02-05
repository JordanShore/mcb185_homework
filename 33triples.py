# 33triples.py by Jordan Shore
#
# This program finds pythagorean triples. 
# A pythogorean triple is values for which a**2 + b**2 = c**2 and all 3 are normal int.

import math


limit = 101
#i+1 avoids repeats and major diagonal since that always gives hypothenuse = side*sqrt(2).
#These nested FOR loops iterate through each int<100 and calculate the triples.
#The IF statement checks if the value of c is equal to the same value floor divided by 1,
#and prints the triple if so as this means all 3 are normal int. 
for i in range(1, limit):
	for j in range(i+1, limit):
		if math.sqrt(i**2 + j**2) == math.sqrt(i**2 + j**2) // 1:
			print("Sides:", i,",", j, "Hypotenuse:", int(math.sqrt(i**2 + j**2)))

