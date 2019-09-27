# Object Oriented Programming

## Function Overloading

Function overloading (also method overloading) is a programming concept that allows programmers to define two or more functions with the same name and in the same scope.

Each function has a unique signature (or header), which is derived from:
1. function/procedure name
2. number of arguments
3. arguments' type
4. arguments' order
5. arguments' name
6. return type

Please note: Not all above signature options are available in all programming languages.

|Language|1|2|3|4|5|6|
|--|--|--|--|--|--|--|
|Ada	|yes|yes|yes|yes|yes|yes|
|C++	|yes|yes|yes|yes|no|no|
|Java	|yes|yes|yes|yes|no|no|
|Swift	|yes|yes|yes|yes|yes|yes|

At compile time, the compiler chooses which overload to use based on the type of arguments passed in by the caller.
Following is a simple C++ example to demonstrate function overloading.
```C
#include <iostream>
using namespace std;

void print(int i) {
  cout << " Here is int " << i << endl;
}
void print(double  f) {
  cout << " Here is float " << f << endl;
}
void print(char const *c) {
  cout << " Here is char* " << c << endl;
}

int main() {
  print(10);
  print(10.10);
  print("ten");
  return 0;
}
```

Output:
```
Here is int 10
Here is float 10.1
Here is char* ten
```

Note: Overloading functions with argument lists of the same types, based on return type alone, is an error.

When working with languages that can discriminate data types at compile-time, selecting among the alternatives can occur at compile-time. The act of creating such alternative functions for compile-time selection is usually referred to as overloading a function

Python is a dynamically typed language, so the concept of overloading simply does not apply to it. However, all is not lost, since we can create such alternative functions at run-time.

Function overloading is further divided into two types: overloading built-in functions and overloading custom functions.

### Overloading User-Defined Functions
To overload a user-defined function in Python, we need to write the function logic in such a way that depending upon the parameters passed, a different piece of code executes inside the function. Take a look at the following example:

```python
class Student:
    def hello(self, name=None):
        if name is not None:
            print('Hey ' + name)
        else:
            print('Hey ')

# Creating a class instance
std = Student()

# Call the method
std.hello()

# Call the method and pass a parameter
std.hello('Nicholas')
```

Output:
```
Hey
Hey Nicholas
```

### Overloading Built-in Functions
It is possible for us to change the default behavior of Python's built-in functions. We only have to define the corresponding special method in our class.

Let us demonstrate this using Python's len() function on our Purchase class:

```python
class Purchase:
    def __init__(self, basket, buyer):
        self.basket = list(basket)
        self.buyer = buyer

    def __len__(self):
        return len(self.basket)

purchase = Purchase(['pen', 'book', 'pencil'], 'Python')
print(len(purchase))
```
Output:
```
3
```

To change how the `len()` function behaves, we defined a special method named `__len__()` in our class. Anytime we pass an object of our class to len(), the result will be obtained by calling our custom defined function, that is, `__len__()`.

The output shows that we are able to use `len()` to get the length of the basket.

If we call len() on the object without the `__len__()` function overloaded, we will get a `TypeError`.

## Operator Overloading
Python allows us to change the default behavior of an operator depending on the operands that we use. This practice is referred to as "operator overloading".


### Operators to Overload
|Operator|Symbol|Method|
|--|--|--|
|Addition|+|`__add__(self, other)`|
|Subtraction|-|`__sub__(self, other)`|
|Multiplication|*|`__mul__(self, other)`|
|Power|**|`__pow(self, other)`|
|Division|/|`__truediv__(self, other)`|
|Floor Division|//|`__floordiv__(self, other)`|
|Remainder|%|`__mod__(self, other)`|
|Lower than|< |`__lt__(self, other)`|
|Lower equal than|<=|`__le__(self, other)`|
|equality|==|`__eq__(self, other)`|
|Not equal|!=|`__ne__(self, other)`|
|Greater than| >|`__gt__(self, other)`|
|Greater or equal than|>=|`__ge__(self, other)`|
|Bitwise left shift|>>|`__lshift__(self, other)`|
|Bitwise right shift|<<|`__rshift__(self, other)`|
|Bitwise AND|&|`__and__(self, other)`|
|Bitwise OR|\||`__or__(self, other)`|
|Bitwise XOR|^|`__xor__(self, other)`|
|Bitwise NOT|~|`__invert__(self, other)`|

## Hash

Immutable data types in Python come with a built-in method for computing their hash value, which is called `__hash__`. However, mutable objects such as lists and dictionaries do not have a hash method. What is important to note is that for immutable types, the hash value depends only on the data stored and not on the identity of the object itself. For instance, you can create two tuples with the same values, and see the differences:

```python
>>> var1 = (1, 2, 3)
>>> var2 = (1, 2, 3)
>>> id(var1)
140697473296656
>>> id(var2)
140697473295216
```

They are indeed different objects, however:

```python
>>> var1.__hash__()
2528502973977326415
>>> var2.__hash__()
2528502973977326415
```

This means that if you use them as dictionary keys, they are going to be indistinguishable from each other, for instance:

```python
>>> var3 = {var1:'var1'}
>>> var3[var2]
'var1'
```

Based on what we saw, hashing an object can be thought as converting it to an integer based on its content, but not on the identity of the object itself. Of course, this may give problems, because you are reducing a very large space of possibilities into a finite set of integers. This reduction may give rise to something known as hash collisions, i.e., two objects which are reduced to the same integer even if their values are different.

A very simple example of hash collisions is what happens between a simple string and an integer:

```python
>>> var1 = 'a'
>>> var1.__hash__()
12416037344
>>> var2 = 12416037344
>>> var1.__hash__() == var2.__hash__()
True
```

Both var1 and var2 have the same hash value. So, we may wonder, what happens if we use them in a dictionary, let's try it to find out:

```python
>>> var3 = {var1: 'var1'}
>>> var3[var2] = 'var2'
>>> var3
{'a': 'var1', 12416037344: 'var2'}
```

As you can see in the snippet above, Python is relying on more than just the hash value of an object when using it as keys for a dictionary.

### Hash Values of Custom Classes

There are differences between mutable and immutable types in Python. Built-in immutable types have always a hash method, while mutable types don't. However, this leaves outside custom defined classes. By default, all instances of custom classes will have a hash value defined at creation and it will not change over time. Two instances of the same class will have two different hash values. For example:

```python
class MyClass:
    def __init__(self, value):
        self.value = value

my_obj = MyClass(1)
print(my_obj.__hash__()) # 8757243744113
my_new_obj = MyClass(1)
print(my_new_obj.__hash__()) # -9223363279611078919
```

If you run the code above, you will see that the hash value that you get from your objects changes every time. This is because the hash is derived from the object's id. Python, as expected, allows you to define your own hash value. For example, you can alter `MyClass` like this:

```python
class MyClass:
    def __init__(self, var):
        self.var = var

    def __hash__(self):
        return int(self.var)
```

If you re-run the example, you will see that both objects have the same hash value of 1. So, let's see what happens if we use them as the keys for a dictionary:

```python
>>> my_obj = MyClass(1)
>>> my_obj_2 = MyClass(1)
>>> var = {my_obj: 'my_obj'}
>>> var[my_obj_2] = 'my_obj_2'
>>> print(var)
{My Class: 'my_obj', My Class: 'my_obj_2'}
```

What you can see is that, even if the hash value is the same, they end up as different keys in the dictionary. There is still something else missing. Even if their hash values are the same, they are different objects:

```python
>>> my_obj == my_obj_2
False
```

We can tweak the `MyClass` class in order to output True when comparing it:

```python
class MyClass:
    def __init__(self, var):
        self.var = var

    def __hash__(self):
        return int(self.var)

    def __eq__(self, other):
        return other.var == self.var
```

The method `__eq__` is used to determine whether one object is equal to another. Because `MyClass` takes only one argument when instantiating, we just compare that value. For example, we would get:

```python
>>> var1 = MyClass(1)
>>> var2 = MyClass(1)
>>> var3 = MyClass(2)
>>> var1 == var2
True
>>> var1 == var3
False
```

It works as we would expect it to. If we try again with a dictionary:

```python
>>> var4 = {var1: 'var1'}
>>> var4[var2] = 'var2'
>>> var4
{My Class: 'var2'}
>>> var4[var3] = 'var3'
>>> var4
{My Class: 'var2', My Class: 'var3'}
```

Finally, we see what is that dictionaries in Python are using for defining their keys. They do not only look at the hash value, they also look whether the keys are the same or not. If they are not, they will be assigned to a new element instead of the same one. You can try and see what happens if two elements are equal, but have different hash values.

Now you are starting to go through risky waters. If you would compare your object to something other than the MyClass instance (or better said, any object without a var attribute), an exception would be raised. You can also force the equality to be true regardless of the object you are comparing it to. So, for example:

```python
class MyClass:
    def __init__(self, var):
        self.var = var

    def __hash__(self):
        return int(self.var)

    def __eq__(self, other):
        return True
```

And now, we would find a strange behavior:

```python
>>> my_obj = MyClass(1)
>>> var = 1
>>> my_obj == var
True
>>> var2 = {my_obj: 'my_obj'}
>>> var2[var] = 'var'
>>> print(var2)
{MyClass: 'var'}
```

So now you see that dictionaries test two things: the hash value and the equality, if one of them doesn't match, then it is going to be assigned as a new key.

#### Reference
[What are hashable objects](https://www.pythonforthelab.com/blog/what-are-hashable-objects/)