# 31fizzbuzz.py by Jordan Shore
#
# This program writes the numbers from 1-100 with caviats.
# If the number is a multiple of 3, it prints Fizz, for a multiple of 5 print Buzz. FizzBuzz for both.


for i in range(1, 101):
	if (i % 3 == 0) and (i % 5 == 0):
		print("FizzBuzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
	else: 
		print(i)