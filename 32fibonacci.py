# 32fibonacci.py by Jordan Shore
#
# This program prints the first 10 values of the fibonacci sequence.

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34


fib1 = 0
fib2 = -1
fib3 = 0
print(fib3)

#This FOR loop sets the lesser of the 2 starting values to the absolute value of the sum of them. 
for i in range(9):
	fib3 = abs(fib1+fib2)
	print(fib3)
	if fib2 > fib1:
		fib1 = fib3
	else:
		fib2 = fib3
		


