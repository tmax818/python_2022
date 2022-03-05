# Python Syntax

## Indentation and line-endings

- indentation indicates which lines go with which **code block**

## What is a **code block**?

- group of code that belongs together
- How do you signify a code block in Python?

[python_syntax.py](python_syntax.py)

## `pass`

- hanging code block:

```
class User:
```
will produce this error:

```bash
IndentationError: expected an indented block after class definition on line xx
```

- the `pass` statement is used for stubbing out code:

```py

class User:

    def __init__(self):
        pass

    def is_logged_in(self)-> bool:
        pass

```
