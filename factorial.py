# factorial.py by Jordan Shore
#
# This program contains a function to calculate the factorial of a number.


def factorial(n):
	"""
	Calculate the factorial of a number.

	Parameters
	----------
	n: Int 
	n will be multiplied by each 0>int<i to get its factorial.

	Returns
	----------
	ftrl: Int 
	The factorial value of n.

	Ex. factorial(4) = 4*3*2*1 -> 24
	"""
	ftrl = 1
	for i in range(1, n+1):
		ftrl = ftrl * i

	return ftrl

print(factorial(4))
print(factorial(9))