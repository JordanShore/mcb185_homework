# 36poisson.py by Jordan Shore
#
# This program contains functions that calculate factorial and Poisson probability. 

import math

def factorial(n):
	"""
	factorial(n) calculates an int n multiplied by each 0<int<n.

	Parameters
	----------
	n: Int, for which factorial will be calculated

	Returns
	----------
	ftrl: Int, factorial value of n
	"""

	ftrl = 1
	for i in range(1, n+1):
		ftrl = ftrl * i 
	return ftrl

def poisson(n, k):
	"""
	poisson(n, k) calculates the Poisson probability of k events occuring.

	Parameters
	----------
	n: Int, options possible
	k: Int, events chosen

	Returns
	----------
	pp: Float, poisson probability
	"""

	pp = n**k * math.e**(-n) / factorial(k)
	return pp 

print("Poisson probability for 5 choose 3 is", poisson(5, 3))
print("Poisson probability for 13 choose 7 is", poisson(13, 7))
print("Poisson probability for 7 choose 2 is", poisson(7, 2))
