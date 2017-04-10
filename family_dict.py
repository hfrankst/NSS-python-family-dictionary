my_family = {
    'middle brother': {
        'name': 'Preston',
        'age': 23,
    },
    'mother': {
        'name': 'Katherine',
        'age': 56,
    },
    'father': {
    	'name': 'Manning',
    	'age': 68,
    },
    'youngest brother': {
    	'name': 'Manning',
    	'age': 22,
    }
}

#iterate over the dictionary and print out the family members

for key,value in my_family.items():
	print(value['name'] + " is my " + key + " and is " + str(value['age']) + " years old.") 
