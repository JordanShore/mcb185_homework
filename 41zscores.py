# 41zscores.py by Jordan Shore
#
# This program calculates the percent of numbers drawn from a normal distribution 1-3 z scores above the mean.

import random

z1 = 0
z2 = 0
z3 = 0

#Runs 100,000 trials and counts how many are 1,2,3 z scores above the mean.
trials = 100000
for i in range(trials):
	r = random.gauss(0, 1)
	if r > 1: z1 += 1
	if r > 2: z2 += 1
	if r > 3: z3 += 3

#Prints the proportion of trials 1,2,3 z scores above the mean. 
print(z1/trials, "of the values are > 1 z score above the mean.")
print(z2/trials, "of the values are > 2 z score above the mean.")
print(z3/trials, "of the values are > 3 z score above the mean.")