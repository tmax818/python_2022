

# integers

my_int = 39
print(type(my_int))

# floats
my_float = 3.14
print(type(my_float))

# conversion

int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

# Random Nummber

import random
from pprint import pprint

pprint(dir(random))

import random
print(random.randint(2,5)) # provides a random number between 2 and 5
