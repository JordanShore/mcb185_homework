#38quiz.py by Jordan Shore
#Co-Authors: George M., Kaled S., Ethan D.

# This program estimates pi using the Gregory-Leibenz series.


def gregory_leibenz(depth):
	"""
	Gregory-Leibenz series estimates pi by multiplying 4 by a sum of x terms, where x is the chosen depth.
	Each term in the series is either added or subtracted.
	Numerator of each term is 1.
	Denominator is 1,3,5, etc...

	Parameters
	----------
	depth: Int, Number of fractional terms in the series.

	Returns
	----------
	pi: Float, estimated value of Pi at this depth.
	"""

	#Initialize i to 0.
	#i is the number of terms deep in the WHILE loop.
	glsum = 0
	i=0

	#WHILE loop does all the calculation.
	while i<(depth):
	#The IF/ELIF statement create a +/- based on whether the term is even or odd.
	#This allows the term to flip addition subtraction each iteration.
		if i % 2 == 0:
			posneg = 1
		elif i % 2 == 1:
			posneg = -1

	#denominator increases by 2 each iteration.
		denom = 1+2*i

	#Calculation of sum to be multiplied by 4 at the end and iteration steps.
		glsum = glsum + posneg / denom
		i = i+1

	pi = glsum*4
	return pi

print(gregory_leibenz(3))
print(gregory_leibenz(6))
print(gregory_leibenz(20))
print(gregory_leibenz(300))


