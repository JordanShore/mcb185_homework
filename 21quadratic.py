# 21quadratic.py by Jordan Shore
#
# This program contains a function that solves the quadratic formula.


#Parameters are a,b,c for y=ax**2+bx+c
#Returns both X intercepts.
def quadratic(a,b,c):
	import math
	import sys
#Checks if there will be a negative sqrt. 
	if ((b**2-4*a*c)<0): sys.exit("Error, no real solutions.")
#Calculate x intercepts.
	xint1 = ((-1*b + math.sqrt(b**2-4*a*c))/(2*a))
	xint2 = ((-1*b - math.sqrt(b**2-4*a*c))/(2*a))

	return xint1,xint2

#Testing Function
firstx1,firstx2 = quadratic(3,12,9)
print("Test 1, X intercepts:", firstx1,",",firstx2)
secondx1,secondx2 = quadratic(1,4,4)
print("Test 2, X intercepts:", secondx1,",",secondx2)
thirdx1,thirdx2 = quadratic(10,10,-10)
print("Test 3, X intercepts:", thirdx1,",",thirdx2)