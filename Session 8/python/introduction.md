# Python

## Functions
```python
def func(input):
    # code
    return output
```

```python
def func(a=2, b=3):
    return a*b

func(b=4, a=8)
```

### `*args` and `**kwargs`
Unlimited input to functions!
```python
def func(*args):
    for item in args:
	print(item)
```
```python
def func(**kwargs):
    for key, value in kwargs.items():
	print(key, value)

    print(kwargs["key"])
```

```python
def func(*args, **kwargs):
    for item in args:
	# code

    for key, value in kwargs.items():
	# code
```

## Map
```python
def func(num):
    if num % 2:
	return "ODD"
    else:
	return "EVEN"

mylist = [1, 2, 3, 4, 5]
map(func, mylist)
```

## Underscore

### In Interpreter

The python interpreter stores the last expression value to the special variable called ‘_’. This feature has been used in standard CPython interpreter first and you could use it in other Python interpreters too.

```python
>>> 10
10
>>> _
10
>>> _ * 3
30
>>> _ * 20
600
```

### For Ignoring the values

The underscore is also used for ignoring the specific values. If you don’t need the specific values or the values are not used, just assign the values to underscore.

```python
for x, _, z in l:
    # code
```

### Give special meanings to name of variables and functions

#### Single Leading Underscore

This convention is used for declaring private variables, functions, methods and classes in a module. Anything with this convention are ignored in `from module import *`.

#### Double Leading Underscore

This is about syntax rather than a convention. double underscore will mangle the attribute names of a class to avoid conflicts of attribute names between classes. (so-called "mangling" that means that the compiler or interpreter modify the variables or function names with some rules, not use as it is)
The mangling rule of Python is adding the `_ClassName` to front of attribute names are declared with double underscore.
That is, if you write method named `__method` in a class, the name will be mangled in `_ClassName__method` form.

```python
class A:
    def _single_method(self):
	pass    def __double_method(self): # for mangling
	passclass B(A):
    def __double_method(self): # for mangling
	pass
```

Because of the attributes named with double underscore will be mangled like above, we can not access it with `ClassName.__method`. Sometimes, some people use it as like real private ones using these features, but it is not for private and not recommended for that. For more details, read Python Naming.

#### Double Leading and Trailing Underscore

This convention is used for special variables or methods (so-called “magic method”) such as `__init__`, `__len__`. These methods provides special syntactic features or does special things. For example, `__file__` indicates the location of Python file, `__eq__` is executed when a == b expression is excuted.