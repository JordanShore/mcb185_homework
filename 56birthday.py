#56birthday.py by Jordan Shore
#
#This program simulates the birthday problem.

import random
import sys


def check_duplicates(people, days):
#Checks if any birthdays are duplicates while being generated.
#Returns 1 if True, 0 if False.
	birthdays = []
	duplicate = 0

'''
This FOR loop:
1: Randomly generates a new birthday.
2: Uses an inner FOR loop to check the new birthday against all past birthdays.
3: Returns duplicate = 1 if a match is found. 
4: Adds the new birthday to the overall list.
'''
	for i in range(people):
		new_bday = random.randint(1,days)
		for past_bdays in birthdays:
			if new_bday == past_bdays:
				duplicate = 1
				return duplicate 
		birthdays.append(new_bday)

	return duplicate

#Takes Trials, Days, and People in command line
trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

#totdups will count how many total duplicates found.
totdups = 0
for n in range(trials):
	totdups += check_duplicates(people, days)

#Prints proportion of times a duplicate birthday was found. 
print(totdups / trials)




