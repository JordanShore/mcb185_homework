#57birthday.py by Jordan Shore
#
#This program counts the number of duplicate birthdays,
#Then solves the birthday problem. 

import random
import sys


def check_birthday_duplicates(people, days):
#Similar to hw 56, this returns 1 if there are duplicate birthdays or 0 if not.
	calendar = []
	duplicate = 0
#Creates a calendar of empty slots representing each day.
	for i in range(days):
		calendar.append(0)
#Adds the number of people's birthdays to each day. 
	for i in range(people):
		birthday = random.randint(1, days)
		calendar[birthday-1] += 1
#Checks through the calendar for any values >=2 indicating duplicates.
	for day in calendar:
		if day >= 2:
			duplicate = 1
			return duplicate

	return duplicate

#Takes Trials, Days, and People in command line
trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

#Sums total trials where duplicates were found. 
totdups = 0
for i in range(trials):
	totdups += check_birthday_duplicates(people, days)

#Prints proportion of times a duplicate birthday was found. 
print(totdups / trials)




