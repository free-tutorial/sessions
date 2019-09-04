# Python

## `if` Statement
```python
if condition:
    # code
elif condition:
    # code
else:
    # code
```

```python
mylist = [1, 2, 3, 4]
if 1 in mylist: # True
    # code
if 5 in mylist: # False
    # code
```

```python
mydict = {1: "1", 2: "2"}
if 1 in mydict:
    # code
if 1 in mydict.keys():
    # code
if "1" in mydict.values():
    # code
```

## For loops
The term *iterable* means you can iterate over the object.

Example: iterate over every character in a string, every item in a list, over every key in a dictionary.

```python
for item in iterable:
    # code
```

```python
for index, item in enumerate(iterable):
    # code
```

```python
iterable_1 = [1, 2, 3, 4, 5]
iterable_2 = [1, 4, 9, 16, 25]
iterable_3 = [1, 8, 27, 64, 125]
for item_1, item_2, item_3 in zip(iterable_1, iterable_2, iterable_3):
    # code
```

```python
iterable = [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
for num_1, num_2 in iterable:
    print(f"{num_1}**2 = {num_2}")
```

```python
dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
for key, value in dict.items():
    print(f"{key}**2 = {value}")
```

## While loops
```python
while condition:
    # code
```

## List Comprehension
```python
mylist = ["Ali Hejazizo", "Reza Khalkhali", "Sahand Parniani", "Yashar Kor"]
first_names = [item.split()[0] for item in mylist]
```

```python
mylist = [1, 2, 3, 4, 5]
[x**2 for x in mylist if x < 3]
```

```python
celcius = [0, 10, -40, 30, 50]
f = [(9/5) * temp + 32 for temp in celcius]
```


Nested for loop! **Not recommended** to use!
```python
[x*y for x in [1, 2, 3] for y in [4, 5, 6]]
```
