# 35nchoosek.py by Jordan Shore
#
# This program contains a function that calculates factorial and n choose k.
# Used in the statistical probability of a sequence of events without consideration of order.
# Ex. How many different combinations of 3 marbles could you take from a jar of 5 marbles? 5 choose 3.

def factorial(n):
	"""
	Factorial calculates an int n multiplied by each 0<int<n.

	Parameters
	----------
	n: Int, for which factorial will be calculated

	Returns
	----------
	ftrl: Int, Factorial value of n
	"""

	ftrl = 1
	for i in range(1, n+1):
		ftrl = ftrl * i 
	return ftrl

def nck(n, k):
	"""
	n choose k is the number of possible combinations of choices of k, for n options.

	Parameters
	----------
	n: Int, Number of possible options.
	k: Int, Number of options chosen.

	Returns
	----------
	nchoosek: Int, value of n choose k.
	"""

	nchoosek = factorial(n) / factorial(k) * factorial(n-k)
	return nchoosek

print("5 choose 3 is", nck(5, 3))
print("13 choose 6 is", nck(13, 6))
print("7 choose 2 is", nck(7, 2))