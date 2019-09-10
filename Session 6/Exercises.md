# Exercies #1

## Closed Laptop

1. `print` output?

```python
x, y = [1, 2, 3], ['1', '2', '3']
print(x*3, y*3)
```

2. Type of `*args` and `**kwargs`?

```python
def func(a, b, c, ..., *args, **keywords):
```

3. Define a tuple with length = 1.

```python
mytuple = # code here
```

4. Output where indicated with `# ?`.

```python
x = ['1', '2', '3']
y = ''.join(x) # ?
'1' in x # ?
'1' in y # ?
type(x) # ?
type(y) # ?
z = x
z *= 2
x[0] = 0
x # ?
z # ?
s1 = 'Ali'
L1 = list(s1) # ?
```

5. Write down the variable value in each line:

```python
x = [i + 1 for i in range(10)]
x = [i * 2 for i in x if i > 5]
y = [(i, i + 1) for i in range(-2, 2) if i % 2 == 0]
```

```python
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
```

6. Let `x = [1, 2, 3, 4]`, `y = [1, 2, 3, 4]`. How do you produce `z = [1, 4, 9, 16]`?

```python
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

z = # code here
```

7. `print` output?

```python
x = ['foo', [1, 2, 3], 10.4]
y = x[:]
y[0] = 'fooooooo'
y[1][0] = 4

print(x, y, end = '*')
```

8. Output where indicated with `# ?`.

```python
def f(*args,**kwargs):
    print(args, kwargs)

l = [1,2,3]
t = (4,5,6)
d = {'a':7,'b':8,'c':9}

f() # ?
f(1,2,3) # ?
f(1,2,3,"groovy") # ?
f(a=1,b=2,c=3) # ?

f(a=1,b=2,c=3,zzz="hi") # ?
f(1,2,3,a=1,b=2,c=3) # ?
f(*l,**d) # ?
f(*t,**d) # ?
f(1,2,*t) # ?
f(q="winning",**d)  # ?
f(1,2,*t,q="winning",**d) # ?
```

9. Output where indicated with `# ?`.

```python
def f2(arg1,arg2,*args,**kwargs):
    print(arg1,arg2, args, kwargs)

f2(1,2,3) # ?
f2(1,2,3,"groovy") # ?
f2(arg1=1,arg2=2,c=3) # ?
f2(arg1=1,arg2=2,c=3,zzz="hi") # ?
f2(1,2,3,a=1,b=2,c=3) # ?
f2(*l,**d) # ?
f2(*t,**d) # ?
f2(1,2,*t) # ?
f2(1,1,q="winning",**d) # ?
f2(1,2,*t,q="winning",**d) # ?
```

## Open Laptop

### Python
1. German Nazis are using a system (Enigma) to encode their messages through transmission. We know that the system shifts every character with a constant number and all chracters are ASCII. For example with a `shift = 2`: "abcde" is encrypted to "cdefg"

   1. Write a function that can decode a German message provided a constant shift.
   2. We also know that Germans put the phrase "Heil Hitler" in every encrypted message. Using the `decode()` function, write a code that can decode a message. Write the decoded message in a `decoded.txt` file.
   3. What is the time and space complexity of decode function? what about your final code?

2. Read a text file and extract all unique words

```python
def read_file(path):
    """
    :type path: Text
    :rtype: List[Text]
    "
```
2. write a program that prints `0` to `100` without using any loop (`for`, `while`, ...).

- Hint: Use recursive functions!
```python
# code here
```

3. Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  `[0,1,2,4,5,6,7]` might become  `[4,5,6,7,0,1,2]`).

Find the minimum element.

You may assume no duplicate exists in the array.

```python
def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
```

### Linux
1. Using only linux commands:
   1. Create two files named `1.txt` and `2.txt`.
   2. Write "Hello World!" in both files.
   3. Bundle them in a file `bundle.tar`
   4. Now compress this file in `bundle.tar.gz`

