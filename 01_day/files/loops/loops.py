## loops.py
## demo

start = 0 # inclusive
stop = 10 # exclusive
step = 2

## TODO range with 1 arg:
# for i in range(stop):
#     print(i)

## TODO range with 2 args:

# for i in range(start, stop):
#     print(i)

## TODO range with 3 args:

# for i in range(start, stop, step):
#     print(i)

for i in range(10):
    if not i % 2:
        print(i)

## TODO loops through strings

my_string = "the average airspeed velocity of an unladen swallow."

for char in my_string:
    print(char)

## TODO loops through lists

my_list = [1,2,3,4,5]

for i in my_list:
    print(i)
## TODO loops through tuples

dog = ("Canis Familiaris", "dog", "carnivore", 12)

# for data in dog:
#     print(data)

# ## TODO loops through dictionaries

# person = {'name': 'Ed', 'age': 31}

# for k in person:
#     print(k)

# for k in person:
#     print(person[k])

# for key, value in person.items():
#     print(f"The peson's {key} is {value}.")

## TODO Loop through lists of dictionaries

data = [
    {'name': 'Ed', 'age': 31},
    {'name': 'John', 'age': 29},
    {'name': 'Tyler', 'age': 39}
]

for person in data:
    print(f"{person['name']} is {person['age']} years old.")

## TODO `while` loops

count = 0
while count < 5:
    print(count)
    count += 1

## TODO loop control



while True:
    guess = int(input("guess a number: "))
    if guess == 42:
        break
    if guess == 13:
        continue
    print("You didn't guess 13")

