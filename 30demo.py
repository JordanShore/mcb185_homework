# 30demo.py by Jordan Shore
#
# This program demos a some uses of loops.

#While Loop Example
i = 0
while True:
    i = i + 1
    print('hey', i)
    if i == 3: break


#Half Matrix - Major Diagonal
#How do you only compare A to TCG and T to CG and C to G?
#Pairwise comparisons without repetition. Start inner loop 1 above outer loop. 
limit = 4
for i in range(0, limit):
    for j in range(i + 1, limit):
        print(i+1, j+1)

