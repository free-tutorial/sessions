# Python

## Basic Data Types

|Name|Type|Description|
|--|--|--|
|integers|int|whole numbers: `300`|
|floating point|float|numbers with a decimal point: `3.4`, `5.80989`, `100.0`|
|strings|str|ordered sequence of characters: `"hello"`, `"summer", "سلام"`|
|lists|list|ordered sequence of objects: `[10, "hello", 200.3]`|
|dictionaries|dict|unordered key, value pairs: `{"key_1": "value_1", "key_2": "value_2"}`|
|tuples|tup|ordered immutable sequence of objects: `(10, "hello", 200.3)`|
|sets|set|unordered collection of unique objects: `{"a", "b"}`|
|booleans|bool|logical value indicating `True` or `False`|

Question: Why doesn't 0.1+0.2-0.3 equal 0.0?
```python
from decimal import Decimal
Decimal(0.3)
```

Variable names rules:
- names cannot start with a number
- there can be no space in name, use `_` instead.
- can't use any of these symbols: `:'",<>/?|\()!@#$%^&*~-+`
- it is considered best practice (pep8) that names are lowercase
- avoid using words that have special meaning in python like `"list"` and `"str"`
  - `str = "string"; x = "123"; str(x)` raises `TypeError: 'str' object is not callable` error. `del str` to remove the variable.
- python uses **Dynamic Typing** which means you can reassign variables to different data types. This is different than other languages that are **"Statically-Typed"**

|Dynamic Typing|Statically-Typed|
|--|--|
|very easy to work wity|may result in bugs for unexpected data types|
|faster development time|you need to be aware or `type()`|
|slow runtime performance|fast runtime performance|

```python
x = 2
x = [1, 2, 3]
# Dynamic Typing: This is OK.
```

```c
int x = 3;
x = "summary"
// Statically-Typed: results in ERROR
```

## Jupyter Notebook
The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.


## Data Types

### Strings
- Strings are ordered sequences: indexing and slicing
- string[start:stop:step]
- Note: strings are immutable!

examples:
```python
my_str = "abcdefghijklmnopqrstuvwxyz"
my_str[0]
my_str[3:]
my_str[:]
my_str[:5]
my_str[::2]
my_str[-1]

my_str[:-1]
my_str[:]

my_str[::-1]

my_str[-4:]
my_str[-4::-1]
```

```python
x = "string"
x = "my " + x
x*10

x.title()
x.capitalize()
```

Formatting:
```python
number = 5
loc = "parking"

my_str = "there are {} car in {}"
my_str.format(number, loc)

car_name = "Ferrari"
my_str = "there are {0:5} {1} car in {2}"
my_str.format(number, car_name, loc)

my_str = "there are {num_people} {location}"
my_str.format(num_poeple=num, location=loc)

num = 2324.92374923749237
"your number is {num:100.3}".format(num=num)

# f-strings
f"there are {number} {car_name} car in {loc}"
```
