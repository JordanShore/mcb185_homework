#82transfac.py by Jordan Shore
#
#This program reads transfac files and outputs them in json format.

import mcb185
import json
import gzip
import sys

'''
mcb185.read_transfac() gives an object where:
#OuterDictionary
ID = Key : MiddleDictionary = Value
#MiddleDictionary
'ACGT' = Key : InnerList = Value
#InnerList
Float = Element


Ex. matrix['AGL3']['G'][2] gives:
The 3rd pwm value for 'G' for the ID 'AGL3'

We want an object where:
#OuterList
OuterDictionary = Element
#OuterDictionary
'id' = Key : ID = Value, 'pwm' = Key : MiddleList = Value
#MiddleList
InnerDictionary = Element
#InnerDictionary
'ACGT' = Key, Float = Value

Ex. biglist[0]['pwm'][2]['G'] gives:
The 3rd pwm value for 'G' for the ID 'AGL3'
'''
#These nested FOR loops convert the data as explained above.
biglist = []
matrix = mcb185.read_transfac(sys.argv[1])
for key in matrix.keys():
	#bigdict represents an ID and associated pwm.
	bigdict = {"id":key,"pwm":[]}
	#The inner FOR loop appends a dictionary for each pwm position.
	for i in range(len(matrix[key]['A'])):
		bigdict["pwm"].append({
			"A":matrix[key]['A'][i],
			"C":matrix[key]['C'][i],
			"G":matrix[key]['G'][i],
			"T":matrix[key]['T'][i],
			})
	biglist.append(bigdict)

print(json.dumps(biglist, indent = 4))
#print(biglist[0]['pwm'][2]['G'])
#print(matrix['AGL3']['G'][2])