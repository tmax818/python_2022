- variable declaration
```py
```
- log statement
```py
```
- type check
```py
print(type(fruit))
```
- length check
```py
```
## comment
- single line
```py
# I didn't see any
```
- multiline
```py
"""
Bonus section
"""
```
## Data Types - Primitive

- Boolean
```py
boolean = True
```
- Numbers
```py
num1 = 42
num2 = 2.3
```
- Strings
```py
string = 'Hello World'
```
## Data Types - Composite
- List 
```py
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
```
- initialize
```py
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
```
- access value
```py
print(pizza_toppings[1])
```
- change value
```py
```
- add value
```py
pizza_toppings.append('Mushrooms')
```
- delete value
```py
```
## Tuples
- initialize
```py
fruit = ('blueberry', 'strawberry', 'banana')
```
- access value
```py
print(fruit[2])
```
- change value
```py
```
- add value
```py
```
- delete value
```py
```
## Dictionary
- initialize
```py
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
```

- access value

```py
print(person['name'])
```
- change value
```py
person['name'] = 'George'
```
- add value
```py
person['eye_color'] = 'blue'
```
- delete value


## conditional
- if
```py
if num1 > 45:
    print("It's greater")
```
- else if
```py
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
```
- else
```py
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
```
## for loop
- start
```py
for x in range(2,5):
    print(x)
```
- stop
```py
for x in range(5):
    print(x)
```
- increment
```py
for x in range(2,10,3):
    print(x)
```
- break
```py
```
- continue
```py
```
- sequence
```py
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
```
## while loop

```py
x = 0 # start
while(x < 5): # stop
    print(x)
    x += 1 # increment
```
## function
- parameter
```py
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
```
- argument
```py
print_hello_x_times(4)
```
- return

## * Bonus: Errors

- NameError: name <variable name> is not defined
- TypeError: 'tuple' object does not support item assignment
- KeyError: 'favorite_team'
- IndexError: list index out of range
- IndentationError: unexpected indent
- AttributeError: 'tuple' object has no attribute 'pop'
- AttributeError: 'tuple' object has no attribute 'append'
- Tuples
    - change value
    - add value
    - delete value