# Exam

## Linux
1. Using only linux commands:
   1. Create two files named `1.txt` and `2.txt`.
   2. Write "Hello World!" in both files.
   3. Bundle them in a file `bundle.tar`
   4. Now compress this file in `bundle.tar.gz`

2. What type of compression does `gzip` do?
   1. lossless
   2. lossy

## Git
1. Create a [github](github.com) account.
2. Create a repo named: `git-practice`
3. Create a folder and initialize git.
4. Add the created repo as a remote and name it `origin`
5. Create a branch with your name.
6. Create two text files and write some text.
7. Add and commit the files as one commit.
8. Push the files.
9. Add me as a collaborator.
10. Create a pull request and add me as a reviewer.

## Object Oriented Programming
1. what is the output where indicted with `# ?`?

```python
class MyClass:
    def __init__(self, var):
        self.var = var

    def __hash__(self):
        return int(self.var)

    def __eq__(self, other):
        return True
```

```python
my_obj = MyClass(1)
var = 1
my_obj == var # ?
var2 = {my_obj: 'my_obj'}
var2[var] = 'var'
print(var2) # ?
```

1. Write these classes with OOP and inheritance.

```
                --------------
                    Shape
                --------------
                /           \
        -----------     -------------
            Poly            Circle
        -----------     -------------
          |
    -----------
        Rect
    -----------

```

1. Shape
   - circ()
2. Poly
   1. sides: list
3. Circle
   1. r: float
4. Rect

```python
# constructor call
poly = Poly([2, 3, 8, 9])
poly.sides[0] = 2

circle = Circle(2)

rect = Rect([1, 2])

# function call
print(poly.circ())
print(rect.circ())
print(circle.circ())

# operator overloading
print(poly < circle)
```

1. Complete subtract method:

```python
class Point:

    def __init__(self, x = 0, y = 0):
      self.x = x
      self.y = y

    def __sub__(self, other):
        # code here

p1 = Point(3, 4)
p2 = Point(1, 2)
result = p1 - p2
print(result.x, result.y)
```

3. The correct way to instantiate the above Dog class is:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Check all that apply:
- [ ] `Dog("Rufus", 3)`
- [ ] `Dog()`
- [ ] `Dog.__init__("Rufus", 3)`
- [ ] `Dog.create("Rufus", 3)`


3. In Python, a function within a class definition is called a:
- [ ] an operation
- [ ] a class function
- [ ] a method
- [ ] a callable


4. What’s the output of the following code snippet?

```python
class Dog:
    def walk(self):
        return "*walking*"

    def speak(self):
        return "Woof!"

class JackRussellTerrier(Dog):
    def speak(self):
        return "Arff!"

bobo = JackRussellTerrier()
bobo.walk()
```


5. What’s the output of the following code snippet?

```python
class Dog:
    def walk(self):
        return "*walking*"
    def speak(self):
        return "Woof!"

class JackRussellTerrier(Dog):
    def speak(self):
        return "Arff!"

bobo = JackRussellTerrier()
bobo.speak()
```


6. What’s the output of the following code snippet?
```python
class Dog:
    def walk(self):
        return "*walking*"
    def speak(self):
        return "Woof!"

class JackRussellTerrier(Dog):
    def talk(self):
        return super().speak()

bobo = JackRussellTerrier()
bobo.talk()
```

1. Given the below code snippet, which of the following outputs are correct? (Select all that apply.)

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRusselTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
```

```python
>>> isinstance(miles, Dog)
False
```

```python
>>> isinstance(buddy, Bulldog)
True
```

```python
>>> isinstance(miles, Dog)
True
```

```python
>>> isinstance(jack, Dachshund)
False
```

```python
>>> isinstance(jack, Dog)
False
```

```python
>>> isinstance(miles, Bulldog)
False
```