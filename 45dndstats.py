# 45dndstats.py by Jordan Shore
#
# This program determines the average stats for a dnd character with various rules.

import random

#r means roll, tot means total stats for this trial
#Methods of stat creation: os = oldschool, nf = nofailures, em = easymode, ld = lowdrop
#Ex. ros is a roll for old school, totnf is the total for nofailures
trials = 10000
totos = 0
totnf = 0
totem = 0
totld = 0
for i in range(trials):

	#FOR loop Rolls 3D6.
	oldschool = 0
	for n in range(3):
		ros = random.randint(1, 6)
		oldschool += ros
	totos += oldschool

	#FOR loop Rolls 3D6. 
	#WHILE loop Rerolls 1s. 
	nofailures = 0
	for n in range(3):
		rnf = random.randint(1, 6)
		if rnf == 1:
			rnf = random.randint(1, 6)
		nofailures += rnf
	totnf += nofailures

	#FOR loop Rolls 3D6x2.
	#IF/ELSE takes the higher of the two rolls.
	easymode = 0
	for n in range(3):
		em1 = random.randint(1, 6)
		em2 = random.randint(1, 6)
		if em1 >= em2:
			rem = em1
		else:
			rem = em2
		easymode += rem
	totem += easymode

	#FOR loop Rolls 4D6.
	#IF statement finds the badroll by calculating the min of 4, 
	#then subtracts it at the end from total.
	lowdrop = 0
	badroll = 7
	for n in range(4):
		rld = random.randint(1, 6)
		if rld < badroll:
			badroll = rld
		lowdrop += rld
	lowdrop -= badroll
	totld += lowdrop

print("Average for 3D6:", totos/trials)
print("Average for 3D6r1:", totnf/trials)
print("Average for 3D6x2:", totem/trials)
print("Average for 4D6d1:", totld/trials)