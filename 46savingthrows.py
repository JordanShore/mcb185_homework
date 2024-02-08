# 46savingthrows.py by Jordan Shore
#
# This program determines the probability of saving throw success in dnd.

import random

def roll_normal():
	return random.randint(1,20)

def roll_advantage():
	r1 = random.randint(1,20)
	r2 = random.randint(1,20)
	if r1 >= r2:
		return r1
	else:
		return r2

def roll_disadvantage():
	r1 = random.randint(1,20)
	r2 = random.randint(1,20)
	if r1 <= r2:
		return r1
	else:
		return r2

trials = 10000
print("\tNor")
for dc in range(5,16,5):
	print(dc, end='\t')
	successn = 0
	for i in range(trials):
		rn = roll_normal()
		if rn >= dc:
			successn += 1
	print(successn / trials)

print("\tAdv")
for dc in range(5,16,5):
	print(dc, end='\t')
	successa = 0
	for i in range(trials):
		ra = roll_advantage()
		if ra >= dc:
			successa += 1
	print(successa / trials)

print("\tDis")
for dc in range(5,16,5):
	print(dc, end='\t')
	successd = 0
	for i in range(trials):
		rd = roll_disadvantage()
		if rd >= dc:
			successd += 1
	print(successd / trials)
	