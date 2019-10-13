# Python

## Data Types

### String
#### f-strings

Examples:
```python
>>> name = "Eric"
>>> age = 74
>>> f"Hello, {name}. You are {age}."
'Hello, Eric. You are 74.'
```

```python
>>> f"{2 * 37}"
'74'
```

```python
>>> def to_lowercase(input):
...     return input.lower()

>>> name = "Eric Idle"
>>> f"{to_lowercase(name)} is funny."
'eric idle is funny.'
```

```python
>>> f"{name.lower()} is funny."
'eric idle is funny.'
```

Multiline f-strings
```python
>>> name = "Eric"
>>> profession = "comedian"
>>> affiliation = "Monty Python"
>>> message = (
...     f"Hi {name}. "
...     f"You are a {profession}. "
...     f"You were in {affiliation}."
... )
>>> message
'Hi Eric. You are a comedian. You were in Monty Python.'
```

### List
```python
mylist = [1, 2, 3, 4]
mylist[0]
mylist[0:]
mylist.append("new item")
print(mylist.pop())
print(mylist.pop(0))
mylist.sort()
mylist.reverse()
```

### Dictionary
```python
mydict = {"one": 1, "two": 2, "three": 3}
mydict["one"]
mydict.keys()
mydict.values()
mydict.items()

# will raise `TypeError: unhashable type: 'list'`
mydict = {[1,2,3]: 1, [4, 5, 6]: 2, [7, 8, 9]: 3}
```
Note: **Immutable** data types in Python come with a built-in method for computing their hash value, which is called `__hash__`

### Tuple
```python
mytuple = (1, 2, 3)
len(mytuple)
mytuple.count(3)
mytuple.index(3)

mytuple = ("one", "two", "three")
mytuple[0] = "one"
```

### Set
```python
myset = set()
myset.add(1)
myset.add(1)
myset.add(2)

myset.add([1, 2, 3])

set_1 = set([1, 2, 3, 1234])
set_2 = set([4, 5, 6])

set_1.union(set_2)
set_1.intersection(set_2)

set_1.update(set_2)
set_1.update(mylist)

set_1.remove(1234)
```

## I/O
Files on most modern file systems are composed of three main parts:
- Header: metadata about the contents of the file (file name, size, type, and so on)
- Data: contents of the file as written by the creator or editor
- End of file (EOF): special character that indicates the end of the file

```
---------------------
        HEADER
---------------------


        DATA


---------------------
        EOF
---------------------
```

### Character Encodings
One problem often encountered when working with file data that you may face is the encoding of the byte data. An encoding is a translation from byte data to human readable characters. This is typically done by assigning a numerical value to represent a character. The two most common encodings are the ASCII and UNICODE Formats. ASCII can only store 128 characters, while Unicode can contain up to 1,114,112 characters.

ASCII is actually a subset of Unicode (UTF-8), meaning that ASCII and Unicode share the same numerical to character values. It’s important to note that parsing a file with the incorrect character encoding can lead to failures or misrepresentation of the character. For example, if a file was created using the UTF-8 encoding, and you try to parse it using the ASCII encoding, if there is a character that is outside of those 128 values, then an error will be thrown.


### Read
```python
myfile = open('file.txt')
myfile.read()
myfile.read()

myfile.seek(0)
myfile.read()

myfile.seek(0)
myfile.readlines()
myfile.readline()

myfile.close()
```

When you’re manipulating a file, there are two ways that you can use to ensure that a file is closed properly, even when encountering an error. The first way to close a file is to use the try-finally block:

```python
reader = open('dog_breeds.txt')
try:
    # Further file processing goes here
finally:
    reader.close()
```

```python
with open('file.txt') as f:
    f.read()
```

### `with` Statement
Error handling in python:
```python
try:
    mydict = {[1,2,3]: '1'}
except TypeError as e:
    print(e)
finally:
    mydict = {1: '1'}
```

As most other things in Python, the with statement is actually very simple, once you understand the problem it’s trying to solve. Consider this piece of code:

```python
set things up
try:
    do something
finally:
    tear things down
```

Here, “set things up” could be opening a file, or acquiring some sort of external resource, and “tear things down” would then be closing the file, or releasing or removing the resource. The try-finally construct guarantees that the “tear things down” part is always executed, even if the code that does the work doesn’t finish.

If you do this a lot, it would be quite convenient if you could put the “set things up” and “tear things down” code in a library function, to make it easy to reuse.

```python
class controlled_execution:
    def __enter__(self):
        set things up
        return thing
    def __exit__(self, type, value, traceback):
        tear things down

with controlled_execution() as thing:
        some code
```
Now, when the “with” statement is executed, Python evaluates the expression, calls the `__enter__` method on the resulting value (which is called a “context guard”), and assigns whatever `__enter__` returns to the variable given by as. Python will then execute the code body, and no matter what happens in that code, call the guard object’s `__exit__` method.

```python
f = open('file.txt')
f.read()

f.__enter__()

f.__exit__()
f.read()
```

|Method|What It Does|
|--|--|
|`.read(size=-1)`|This reads from the file based on the number of size bytes. If no argument is ||passed or None or -1 is passed, then the entire file is read.|
|`.readline(size=-1)`|This reads at most size number of characters from the line. This continues to the end of the line and then wraps back around. If no argument is passed or None or -1 is passed, then the entire line (or rest of the line) is read.|
|`.readlines()`|This reads the remaining lines from the file object and returns them as a list.|


### Write
```python
myfile = open('file.txt', 'w')
myfile.write("this is line 1\n")
myfile.writelines(["this is line 2\n", "this is line 3\n"])

myfile.seek(0)
myfile.write("this will replace line 1")
myfile.

myfile.close()
```

### Append
```python
myfile = open('file.txt', 'a')
myfile.write("this is line 1\n")
myfile.writelines(["this is line 2\n", "this is line 3\n"])

myfile.seek(0)
myfile.write("this will replace line 1")

myfile.close()
```


### Working With Bytes
Sometimes, you may need to work with files using byte strings. This is done by adding the 'b' character to the mode argument. All of the same methods for the file object apply. However, each of the methods expect and return a bytes object instead:

```python
>>> with open('png.png', 'rb') as reader:
>>>     print(reader.readline())
```

Since the .png file format is well defined, the header of the file is 8 bytes broken up like this:

```python
myfile = open("png.png", 'rb')
for i in range(8):
    print(myfile.read(1))

# b'\x89'
# b'P'
# b'N'
# b'G'
# b'\r'
# b'\n'
# b'\x1a'
# b'\n'
```