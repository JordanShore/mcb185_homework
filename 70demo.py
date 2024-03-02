#70demo.py by Jordan Shore
#
#This program demos dictionaries. 
import itertools

d = {'dog': 'woof', 'cat': 'meow'}
print(d)

for k, v in d.items(): print(k, 'says', v)

print(d.keys(), d.values(), list(d.values()))

for nts in itertools.product('ACGT', repeat=3):
    print(nts)