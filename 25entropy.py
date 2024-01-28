# 25entropy.py by Jordan Shore
#
# This program contains a function that calculates Shannon Entropy for DNA Nucleotides. 

import math

#Parameters are A, C, G, T counts.
#Returns Shannon Entropy.
def shannon_entropy(a, c, g, t):
	total = a + c + g + t
#These IF / ELSE statements set the statement for each variable equal to 0 if the count is 0.
#If a letter count is 0, then it would cause and error when taking a log.
#But since it still accounts for 0 of the entropy, it needs to be counted as 0. 
	if a != 0:
		shannona = a / tot * math.log2(a)
	else:
		shannona = 0

	if c != 0:
		shannonc = c / tot * math.log2(c)
	else:
		shannonc = 0

	if g != 0:
		shannong = g / tot * math.log2(g)
	else:
		shannong = 0

	if t != 0:
		shannont = t / tot * math.log2(t)
	else:
		shannont = 0

	entropy = -1*(shannona + shannonc + shannong + shannont)

	return entropy
