#70demo.py by Jordan Shore
#
#This program demos dictionaries. 
import itertools

#Dictionary Basic
d = {'dog': 'woof', 'cat': 'meow'}
print(d)

#dictionary.items returns a list of tuples with key value pairs
for k, v in d.items(): print(k, 'says', v)

#Printing keys or values
print(d.keys(), d.values(), list(d.values()))

#itertools.product gives every combo of repeat=x elements.
for nts in itertools.product('ACGT', repeat=3):
    print(nts)