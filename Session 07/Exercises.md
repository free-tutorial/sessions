# Exercies #1

## Closed Laptop

1. `print` output?

```python
x, y = [1, 2, 3], ['1', '2', '3']
print(x*3, y*3)
```

> Wrong: `['1', '1', '1', '2', '2', '2', '3', '3', '3']`

> Wrong: `[3, 6, 9]`

> Solution: `[1, 2, 3, 1, 2, 3, 1, 2, 3] ['1', '2', '3', '1', '2', '3', '1', '2', '3']`

1. Type of `*args` and `**kwargs`?

```python
def func(a, b, c, ..., *args, **kwargs):
```

> Solution:
>
> `*args`: `list`
>
> `**kwargs`: `dict`

3. Define a tuple with length = 1.

```python
mytuple = # code here
```

> Wrong: `Tuple(1)`

> Solutions:
> - `(1, )`
> - `Tuple([1])`

1. Output where indicated with `# ?`.

```python
x = ['1', '2', '3']
y = ''.join(x) #1 ?
'1' in x #2 ?
'1' in y #3 ?
type(x) #4 ?
type(y) #5 ?
z = x
z *= 2
x[0] = 0
x #6 ?
z #7 ?
s1 = 'Ali'
L1 = list(s1) #8 ?
```

> Solution:
> 1. `123`
> 2. `True`
> 3. `True`
> 4. `<class 'list'>`
> 5. `<class 'str'>`
> 6. `[0, '2', '3', '1', '2', '3']`
> 7. `[0, '2', '3', '1', '2', '3']`
> 8. `['A', 'l', 'i']`

1. Write down the variable value in each line:

```python
x = [i + 1 for i in range(10)]
x = [i * 2 for i in x if i > 5]
y = [(i, i + 1) for i in range(-2, 2) if i % 2 == 0]
```

> Solution:
> 1. `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
> 2. `[12, 14, 16, 18, 20]`
> 3. `[(-2, -1), (0, 1)]`

```python
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
```

> Solution:
> 1. `{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}`
> 2. `range(0, 10)`
> 3. `[]`
> 4. `[1, 2, 3, 4, 5]`
> 5. `[1, 2, 3, 4, 5]`
> 6. `{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}`
> 7. `[[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]`

1. Let `x = [1, 2, 3, 4]`, `y = [1, 2, 3, 4]`. How do you produce `z = [1, 4, 9, 16]` with list comprehension?

```python
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

z = # code here
```

> Solution:
> `z = [i*j for i, j in zip(x, y)]`
> `[x[i]*y[i] for i in range(len(x))]` # Sahand's approach, MUST bring sweets next session (session 8)

7. `print` output?

```python
x = ['foo', [1, 2, 3], 10.4]
y = x[:]
y[0] = 'fooooooo'
y[1][0] = 4

print(x, y, end = '*')
```

> Solution: `['foo', [4, 2, 3], 10.4] ['fooooooo', [4, 2, 3], 10.4]*`

> Note: Read shallow `copy()` and `deepcopy()` from [here](https://docs.python.org/2/library/copy.html).

1. Output where indicated with `# ?`.

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

> Solution:
>
> 1. `() {}`
> 2. `(1, 2, 3) {}`
> 3. `(1, 2, 3, 'groovy') {}`
> 4. `() {'a': 1, 'b': 2, 'c': 3}`
> 5. `() {'a': 1, 'b': 2, 'c': 3, 'zzz': 'hi'}`
> 6. `(1, 2, 3) {'a': 1, 'b': 2, 'c': 3}`
> 7. `(1, 2, 3) {'a': 7, 'b': 8, 'c': 9}`
> 8. `(4, 5, 6) {'a': 7, 'b': 8, 'c': 9}`
> 9. `(1, 2, 4, 5, 6) {}`
> 10. `() {'q': 'winning', 'a': 7, 'b': 8, 'c': 9}`
> 11. `(1, 2, 4, 5, 6) {'q': 'winning', 'a': 7, 'b': 8, 'c': 9}`


1. Output where indicated with `# ?`.

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

> Solution:
>
> 1. `1 2 (3,) {}`
> 2. `1 2 (3, 'groovy') {}`
> 3. `1 2 () {'c': 3}`
> 4. `1 2 () {'c': 3, 'zzz': 'hi'}`
> 5. `1 2 (3,) {'a': 1, 'b': 2, 'c': 3}`
> 6. `1 2 (3,) {'a': 7, 'b': 8, 'c': 9}`
> 7. `4 5 (6,) {'a': 7, 'b': 8, 'c': 9}`
> 8. `1 2 (4, 5, 6) {}`
> 9. `1 1 () {'q': 'winning', 'a': 7, 'b': 8, 'c': 9}`
> 10. `1 2 (4, 5, 6) {'q': 'winning', 'a': 7, 'b': 8, 'c': 9}`


## Open Laptop

### Python
1. German Nazis are using a system (Enigma) to encode their messages through transmission. We know that the system shifts every character with a constant number and all chracters are ASCII. For example with a `shift = 2`: "abcde" is encrypted to "cdefg"

   1. Write a function that can decode a German message provided a constant shift.

> Solution: `decode(message, shift)` function

```python
def decode(message, shift):
    decoded_message = ""

    for ch in message:
        decoded_message += chr((ord(ch) + shift) % 128)

    return decoded_message
```
   1. We also know that Germans put the phrase "Heil Hitler" in every encrypted message. Using the `decode()` function, write a code that can decode a message. Write the decoded message in a `decoded.txt` file.
> Solution:
```python
with open("message.txt") as f:
    message = f.read()

    for shift in range(128):
        decoded_message = decode(message, shift)
        if "Heil Hitler".lower() in decoded_message.lower():
            print(f"Message succussfully decoded with shift = {shift}")
            print(decoded_message)
            break
```
   1. What is the time and space complexity of decode function? what about your final code?

> Solution:
> - `decode(message, shift)` function: O(N) [N is the number of chars in message]
> - final code: O(N) [reading the file] + 128 * O(N + N) [N for shifting, N for lower casing] = O(N)


1. Read a text file and extract all unique words

```python
def read_file(path):
    """
    :type path: Text
    :rtype: List[Text]
    "
```
3. write a program that prints `0` to `100` without using any loop (`for`, `while`, ...).

- Hint: Use recursive functions!

> Solution:
```python
def no_loop_print(n):
    if n > 0:
        no_loop_print(n-1)
    print(n)
```

1. Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  `[0,1,2,4,5,6,7]` might become  `[4,5,6,7,0,1,2]`).

Find the minimum element.

You may assume no duplicate exists in the array.

```python
def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # If the list has just one element then return that element.
    if len(nums) == 1:
        return nums[0]

    # left pointer
    left = 0
    # right pointer
    right = len(nums) - 1

    # if the last element is greater than the first element then there is no rotation.
    # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
    # Hence the smallest element is first element. A[0]
    if nums[right] > nums[0]:
        return nums[0]

    # Binary search way
    while right >= left:
        # Find the mid element
        mid = (left + right) // 2
        # if the mid element is greater than its next element then mid+1 element is the smallest
        # This point would be the point of change. From higher to lower value.
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        # if the mid element is lesser than its previous element then mid element is the smallest
        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        # if the mid elements value is greater than the 0th element this means
        # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
        if nums[mid] > nums[0]:
            left = mid + 1
        # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
        else:
            right = mid - 1
```

### Linux
1. Using only linux commands:
   1. Create two files named `1.txt` and `2.txt`.
   2. Write "Hello World!" in both files.
   3. Bundle them in a file `bundle.tar`
   4. Now compress this file in `bundle.tar.gz`

> Solution:

```bash
touch 1.txt touch 2.txt
echo "Hello World" >> 1.txt # `echo` commands also creates a file if it does not exist, so the previous line is unnecessary
echo "Hello World" >> 2.txt
tar c 1.txt 2.txt -f bundle.tar
gzip bundle.tar
```
