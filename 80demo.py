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
#person['mentors']['Gino'] = 'UCD'
