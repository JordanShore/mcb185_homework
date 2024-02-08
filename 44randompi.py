# 44randompi.py by Jordan Shore
#
# This program estimates pi using random number generation.

import random
import math

#inside is the number of points inside a circle with radius 1.
inside = 0
#total is the number of iterations.
total = 0

#WHILE loop generates infinite x and y coordinates.
#Distance to the origin can be imagined as the hypotenuse of a right triangle.
#Calculated as c of a**2 + b**2 = c**2
while True:
	x = random.random()
	y = random.random()
	distance = math.sqrt(x**2 + y**2)
	if distance < 1:
		inside += 1
	total += 1
	print(4 * inside / total)