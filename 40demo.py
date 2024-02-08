# 40demo.py by Jordan Shore
#
# This program tests random.

import random

for i in range(100):
	rn = random.random()
	if rn < 0.7: print(random.choice('AT'), end='')
	else:        print(random.choice('CG'), end='')
print() 