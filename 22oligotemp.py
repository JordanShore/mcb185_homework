# 22oligotemp.py by Jordan Shore
#
# This program contains a function that calculates oligo melting temperatures.

#Parameters are A, C, G, T counts.
#Returns oligo melt point.
def oligomp(a, c, g, t):
	length = (a + c + g + t)

	if length <= 13:
		mp = (a + t) * 2 + (g + c) * 4
	else:
		mp = 64.9 + 41 * ((g + c - 16.4) / length)

	return mp

#Testing
print("Test 1: a=2 , c=3 , g=4 , t=1")
print("Oligo Melting Temperature:", oligomp(2, 3, 4, 1))
print("Test 2: a=3 , c=12 , g=12 , t=3")
print("Oligo Melting Temperature:", oligomp(3, 12, 12, 3))
print("Test 3: a=10 , c=100 , g=1000 , t=1")
print("Oligo Melting Temperature:", oligomp(10, 100, 1000, 1))