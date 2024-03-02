#71countgff.py by Jordan Shore
#
#This program counts the various types of sequences in a GFF file. 

import gzip
import sys

#Taken from Unit 7. 
#Equivalent to:
#'gunzip -c ecoli.gff.gz | grep -v "^#" | cut -f 3 | sort | uniq -c | sort -nr'
count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
			f = line.split()
			feature = f[2]
		if feature not in count: count[feature] = 0
			count[feature] += 1

'''
Sorted:
Sorted is a function that takes something and sorts it. A list, etc...
But how do you sort it? Well by default there is alphabetical or number order.
But what if I want it sorted by something else?
This is where key= comes in.
key= says, give me a function to apply to each item,
then I will sort those returns.
In this case key=lambda item:item [1] says;
Take the lamba function(item) that returns item[1],
apply it to each tuple in count.items() and sort by item[1]. 
That means lowest to highest numbers.
However reverse=True makes it sort highest to lowest, and therefore:
sorted() returns the dicitionary sorted by values,
which can then be iterated through.
'''
for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True):
	print(k, v)