
## tuples.py
## demo


# my_tuple = 1,
# print(type(my_tuple))

dog = ("Canis Familiaris", "dog", "carnivore", 12)
print(dog)
print(id(dog))
dog = dog + ("domestic",)
print(dog)
print(id(dog))

## TODO builtin tuple functions

print(dir(dog))


## TODO tuples as `return` values

def divide(num, den):
    quo = num // den
    remainder = num % den
    return (quo, remainder)

print(divide(17,3))