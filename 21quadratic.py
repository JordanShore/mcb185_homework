# 21quadratic.py by Jordan Shore
#
# This program contains a function that solves the quadratic formula.

import math
import sys

#Parameters are a, b, c for y=ax**2+bx+c
#Returns both X intercepts.
def quadratic(a, b, c):
#Checks for negative sqrt.
	if b**2 - 4*a*c<0: 
		xint1, xint2 = None, None
	else:
		xint1 = ((-1*b + math.sqrt(b**2 - 4*a*c)) / (2*a))
		xint2 = ((-1*b - math.sqrt(b**2 - 4*a*c)) / (2*a))

	return xint1, xint2

#Testing Function
print("Test 1: X Int for y=3x^2+12x+30")
print(quadratic(3, 12, 30))
print("Test 2: X Int for y=x^2+4x+4")
print(quadratic(1, 4, 4))
print("Test 3: X Int for y=10x^2+10x-10")
print(quadratic(10, 10, -10))
