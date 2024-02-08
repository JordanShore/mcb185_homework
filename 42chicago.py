# 42chicago.py by Jordan Shore
#
# This program plays Chicago and calculates the number of times zero is scored and the average score.

import random

zerogames = 0
totalscore = 0
gamesplayed = 100000

#Outer FOR loop resets score each game to 0 before adding each game score to a total score.
for i in range(gamesplayed):
	score=0
#Inner FOR loop plays the game by rolling 2 D6 and adding the round number to the score if you roll doubles.
	for roundnumber in range(2,13):
		d1 = random.randint(1,6)
		d2 = random.randint(1,6)
		if d1+d2 == roundnumber:
			score += roundnumber

#Calculation of average score.
	totalscore += score
	if score == 0:
		zerogames+=1

print("You will score 0 points", zerogames / gamesplayed, "proportion of the time.")
print("Average score is", totalscore / gamesplayed)