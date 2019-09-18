# Object Oriented Programming

```python
class NameOfClass():
    # class object attribute
    # same for any instance of a class
    class_var = [] #

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

        flag = True

    def some_method(self):
        # perfome some action
        pass
```

3 types of variables:
1. class variables, [`class_var`] (shared among all objects)
2. object variables [`self.param1`, `self.param2`]
3. local variables [`flag`]

## Public, Protected, Private Access

### Public
```python
class employee:
    def __init__(self, name, sal):
        self.name = name
        self.salary = sal
```

### Protected
```python
class employee:
    def __init__(self, name, sal):
        self._name = name  # protected attribute
        self._salary = sal # protected attribute
```

In fact, this doesn't prevent instance variables from accessing or modifyingthe instance. You can still perform the following operations:

```python
>>> e1 = employee("Swati", 10000)
>>> e1._salary
10000
>>> e1._salary = 20000
>>> e1._salary
20000
```

### Private
a double underscore __ prefixed to a variable makes it private. It gives a strong suggestion not to touch it from outside the class. Any attempt to do so will result in an AttributeError:

```python
e1 = employee("Bill",10000)
>>> e1.__salary
AttributeError: 'employee' object has no attribute '__salary'
```

Every member with double underscore will be changed to `_object._class__variable`. If so required, it can still be accessed from outside the class, but the practice should be refrained.

```python
e1 = Employee("Bill",10000)
>>> e1._Employee__salary
10000
>>> e1._Employee__salary=20000
>>> e1._Employee__salary
20000
```

## Inheritance

```python
class Animal():
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        # super().__init__()
```

## `super()`

By using the `super()` function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

By using the `super()` function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

## `issubclass()` & `isinstance()`

Two built-in functions `isinstance()` and `issubclass()` are used to check inheritances. Function `isinstance()` returns True if the object is an instance of the class or other classes derived from it. Each and every class in Python inherits from the base class object.

```python
issubclass(derived, base)       # returns True
issubclass(base, drived)        # returns False

isinstance(object, derived)     # returns True
isinstance(object, base)        # returns True
```

