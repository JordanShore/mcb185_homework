#Checksum Example
#Adds characters using ASCII values

import math

def chksum(string):
	checksum = 0
	for char in string:
		checksum = checksum + ord(char)

	return checksum % 256

def maxchar(string):
	current = -1*float("inf")
	for char in string:
		if ord(char)>current:
			current = ord(char)

	return current

def minchar(string):
	current = float("inf")
	for char in string:
		if ord(char)<current:
			current = ord(char)

	return current

def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1 / math.factorial(n)
		print(e)
	return e

def is_perfect_square(n):
	root = math.sqrt(n)
	if root == root // 1: return True
	return False

print(chksum("Jordan"))
print(maxchar("Jordan"))
print(minchar("Jordan"))
print(euler(20))
print(is_perfect_square(16))
print(is_perfect_square(17))