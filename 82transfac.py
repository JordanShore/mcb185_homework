#82transfac.py by Jordan Shore
#
#This program reads transfac files and outputs them in json format.

import mcb185
import json
import gzip
import sys

'''
mcb185.extract_transfac() gives an object where:
#OuterDictionary
ID = Key : MiddleDictionary = Value
#MiddleDictionary
'id' = Key : ID = Value, 'pwm' = Key : InnerList = Value, 
'AC'/'DE' etc... = Key : AC/DE = Value, 'CC' = Key : InnerDictionary = 'Value'
#InnerDictionary
'tax_group'/'tf_class' etc... = Key : TAX_GROUP/TF_CLASS = Value
#InnerList
InnermostDictionary = Element
#InnermostDictionary
'ACGT' = Key : Float = Value

Ex. transfac_object['AGL3']['pwm'][2]['G'] gives:
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
#This FOR loop converts the data as explained above.
biglist = []
transfac_object = mcb185.extract_transfac(sys.argv[1])
for key in transfac_object.keys():
	biglist.append({
		'id':transfac_object[key]['ID'],
		'pwm': transfac_object[key]['pwm']
		})

print(json.dumps(biglist, indent = 4))