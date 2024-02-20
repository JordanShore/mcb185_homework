# 52entropy.py by Jordan Shore
#
# This program calculates entropies for probabilities in the command line.

import sys
import math

#Shannon Entropy from hw 25.
def shannon_entropy(a, c, g, t):
	tot = a + c + g + t
'''
IF / ELSE statements set an overall value for each variable;
This value is equal to 0 if count = 0 or the normal formula.
If a letter count is 0, then it would cause and error when taking a log.
But since it still accounts for 0 of the entropy, it needs to be counted as 0. 
'''
	if a != 0:
		shannona = a / tot * math.log2(a)
	else:
		shannona = 0

	if c != 0:
		shannonc = c / tot * math.log2(c)
	else:
		shannonc = 0

	if g != 0:
		shannong = g / tot * math.log2(g)
	else:
		shannong = 0

	if t != 0:
		shannont = t / tot * math.log2(t)
	else:
		shannont = 0

	entropy = -1*(shannona + shannonc + shannong + shannont)

	return entropy

#problist is the list of probabilities given in the command line.
#Use sys.argv[1:] to exclude the first argument which is the .py file name.
problist = sys.argv[1:]

#First we are going to check if any of the probabilities are invalid.
#Probabilities must sum to 1, and cannot be negative.
probsum = 0
probcount = 0
#This FOR loop also counts the arguments entered and sums the probabilities
for i in range(len(problist)):
	problist[i] = float(problist[i])
	if not ((problist[i]>=0) and (problist[i]<=1)):
		sys.exit("Error: some probabilty is not between 0 and 1.")
	probcount += 1
	probsum += problist[i]

#For any errors we will sys.exit()
if not math.isclose(probsum, 1.0):
	sys.exit("Error: probabilties do not sum to 1.")

#This FOR loop adds 0s to problist to make sure we have 4 values,
#which will allow us to use shannon_entropy for our printout. 
for i in range(4 - probcount):
	problist.append(0)

print(shannon_entropy(problist[0],problist[1],problist[2],problist[3]))










'''


1   import sys
2   import math
3
4   probs = []
5   for arg in sys.argv[1:]:
6       f = float(arg)
7       assert(f > 0 and f < 1)
8       probs.append(float(arg))
9
10  total = 0
11  for p in probs: total += p
12  if not math.isclose(total, 1.0):
13      sys.exit('error: probs must sum to 1.0')
14
15  h = 0
16  for p in probs:
17      h -= p * math.log2(p)
18
19  print(h)
'''