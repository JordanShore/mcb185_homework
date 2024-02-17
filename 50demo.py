# 50demo.py by Jordan Shore
#
# This program tests some functions of containers.

import math

#quadratic from 21quadratic.py
def quadratic(a, b, c):
	if b**2 - 4*a*c<0: 
		xint1, xint2 = None, None
	else:
		xint1 = ((-1*b + math.sqrt(b**2 - 4*a*c)) / (2*a))
		xint2 = ((-1*b - math.sqrt(b**2 - 4*a*c)) / (2*a))

	return xint1, xint2

#Unpacking a tuple
x1,x2 = quadratic(1,5,6)
print(x1,x2)

print()

#Slicing Strings and Converting iterables to lists
s = "Jaguar"
print(s, s[::], s[::1], s[::-1])
s_list = list(s)
print(s_list)
s_remade = "".join(s_list) 
print(s_remade)
print()

#enumerate()
for i,letter in enumerate(s):
	print(i,letter)

print()

#zip()
lets = ['a','b','c','d']
nums = [1,2,3,4]
for l,n in zip(lets,nums):
	print(l,n)
