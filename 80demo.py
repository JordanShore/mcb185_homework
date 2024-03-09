#80demo.py by Jordan Shore
#
#This program demos complex data types.

import json

person = {
	'name': 'Jordan',
	'age': 23,
	'sports': ['Triathlon','Climbing'],
	'mentors': {
		'Mario':'Buck',
		'Alexey':'UCD'
	}
}

person['mentors']['Gino'] = 'UCD'
print(json.dumps(person, indent= 4))

oligo = {
    'Name': 'SO116',
    'Length': 18,
    'Sequence': 'ATTTAGGTGACACTATAG',
    'Description': 'SP6 promoter sequencing primer'
}