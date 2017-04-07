my_family = [
    {
        'name': 'Preston',
        'age': 23,
        'order': 'brother'
    },
    {
        'name': 'Katherine',
        'age': 56,
        'order': 'mother'
    },
    {
    	'name': 'Manning',
    	'age': 68,
    	'order': 'father'
    },
    {
    	'name': 'Manning',
    	'age': 22,
    	'order': 'brother'
    }
]

#iterate over the dictionary and print out the family members


for value in my_family:
	print("{} is my {} and is {} years old.".format(value['name'], value['order'], value['age'])) 
	# print(value)