## dictionaries.py
## demo

# TODO creating dictionaries

## TODO How would you make a person list?
person_list = ['Tyler', 39, ['coding', 'sleeping'], True, False]

## TODO dictionaries give us ways to associate data 
person = {'name': 'Tyler', 'age': 39, 'hobbies': ['coding', 'sleeping']}


## TODO add to the hobbies list: 'gaming'

## TODO add to hobbies list in the person_list:

# print(person_list[2])
# person_list[2].append('gaming')
# print(person_list[2])

## add to hobbies list in person dictionary:

# print(person['hobbies'])
# person['hobbies'].append('gaming')
# print(person['hobbies'])

# print(person)
# person['address'] = address
# print(person)

## TODO remove values with pop('key')
# person.pop('age')
# print(person)

## TODO remove values with del
# del person['hobbies']
# print(person)

# TODO nested dictionaries
address = {'street': '123 Main', 'city': 'Santa Clarita', 'state': 'CA', 'zip': 91355 }
person['address'] = address