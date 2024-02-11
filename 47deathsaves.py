# 47deathsaves.py by Jordan Shore
#
# This program determines the probability of death save success in dnd.

import random


def deathsave():
	success = 0
	failure = 0
	health = 0
	status = "Unconcious"

	while status == "Unconcious":
		turn = random.randint(1, 20)
		if turn == 20:
			health += 1
			status = "Revived"
			break
		elif(turn < 20)and(turn >= 10):
			success += 1
		elif turn == 1: 
			failure += 2
		else:
			failure += 1

	if success >= 3:
		status = "Stable"
	elif failure >= 3:
		status = "Dead"
	return status

trials = 100000
revived = 0
stable = 0
dead = 0
for i in range(trials):
	status = deathsave()
	if status == "Revived":
		revived += 1
	elif status == "Stable":
		stable += 1
	elif status == "Dead":
		dead += 1

print("Probability of revival:", revived / trials)
print("Probability of stabilizing:", stable / trials)
print("Probability of death:", dead / trials)
