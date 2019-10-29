# Numpy

Data analysis: Extracting meaningful information

## Create Numpy Array

```python
>>> import numpy as np
>>> lst = [1,2,3]
>>> arr = np.array([lst, lst])
>>> arr * 10  # different than `list`
[[10, 20, 30], [10, 20, 30]]
>>> np.eye(4) * 10
array([[10.,  0.,  0.,  0.],
       [ 0., 10.,  0.,  0.],
       [ 0.,  0., 10.,  0.],
       [ 0.,  0.,  0., 10.]])
>>> np.eye(3, 6)
array([[1., 0., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0., 0.],
       [0., 0., 1., 0., 0., 0.]])
>>> np.zeros((3, 6))
array([[0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.]])
>>> np.zeros(3)
array([0., 0., 0.])
>>> np.ones(3)
array([1., 1., 1.])
>>> np.ones(3, 6)
array([[1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.]])
>>> np.arange(10, 20, 2)  # start, stop, step=1
array([10, 12, 14, 16, 18])
>>> np.linspace(0, 20, 5)  # start, stop, num=50
array([ 0.        ,  2.22222222,  4.44444444,  6.66666667,  8.88888889,
       11.11111111, 13.33333333, 15.55555556, 17.77777778, 20.        ])
>>> np.linspace(0, 20, 10, dtype=int)
array([ 0,  2,  4,  6,  8, 11, 13, 15, 17, 20])
```

### `ndarray` vs. `matrix`
Numpy matrices are strictly 2-dimensional, while numpy arrays (ndarrays) are N-dimensional. Matrix objects are a subclass of ndarray, so they inherit all the attributes and methods of ndarrays.

```python
>>> import numpy as np
>>> a=np.mat('4 3; 2 1')
>>> b=np.mat('1 2; 3 4')
>>> a
matrix([[4, 3],
        [2, 1]])
>>> b
matrix([[1, 2],
        [3, 4]])
>>> a*b
matrix([[13, 20],
        [ 5,  8]])
```

On the other hand, as of Python 3.5, NumPy supports infix matrix multiplication using the `@` operator, so you can achieve the same convenience of matrix multiplication with ndarrays in Python >= 3.5.

```python
import numpy as np

>>> a=np.array([[4, 3], [2, 1]])
>>> b=np.array([[1, 2], [3, 4]])
>>> a@b
array([[13, 20],
       [ 5,  8]])
>>> np.dot(a, b)
array([[13, 20],
       [ 5,  8]])
```

Both matrix objects and ndarrays have `.T` to return the transpose, but matrix objects also have `.H` for the conjugate transpose, and `.I` for the inverse.

In contrast, numpy arrays consistently abide by the rule that operations are applied element-wise (except for the new `@` operator). Thus, if a and b are numpy arrays, then `a*b` is the array formed by multiplying the components element-wise:

```python
>>> c=np.array([[4, 3], [2, 1]])
>>> d=np.array([[1, 2], [3, 4]])
>>> c*d
array([[4, 6],
       [6, 4]])
```
To obtain the result of matrix multiplication, you use `np.dot` (or `@` in Python >= 3.5, as shown above):

```python
>>> np.dot(c,d)
```

The main advantage of numpy arrays is that they are more general than 2-dimensional matrices. What happens when you want a 3-dimensional array? Then you have to use an ndarray, not a matrix object. Thus, learning to use matrix objects is more work -- you have to learn matrix object operations, and ndarray operations.

Writing a program that uses both matrices and arrays makes your life difficult because you have to keep track of what type of object your variables are, lest multiplication return something you don't expect.

In contrast, if you stick solely with ndarrays, then you can do everything matrix objects can do, and more, except with slightly different functions/notation.

Of course, you really don't have to choose one at the expense of the other, since np.asmatrix and np.asarray allow you to convert one to the other (as long as the array is 2-dimensional).

### Create random numbers
```python
>>> np.random.rand(1, 2, 3, 4)  # d0, d1, d2, ..., dn (uniform distribution)
array([[[[0.07852123, 0.66368148, 0.80621321, 0.60236474],
         [0.29563877, 0.46637678, 0.68775805, 0.60474973],
         [0.34775182, 0.33228831, 0.17995697, 0.63561516]],

        [[0.97476188, 0.34171181, 0.60728871, 0.51456838],
         [0.59496419, 0.92643443, 0.57630917, 0.41814431],
         [0.20848571, 0.13638616, 0.13297371, 0.37779464]]]])
>>> np.random.randn(1, 2, 3, 4)  # d0, d1, d2, ..., dn (standard normal distribution)
array([[[[ 1.28882639,  0.7993164 , -0.16204678, -1.2629709 ],
         [ 0.41491787,  0.22994999,  0.01242777, -1.70434553],
         [-1.9578782 , -1.21180483, -0.23804626, -0.10434225]],

        [[ 0.21465893, -0.9469291 , -0.58032358,  1.46851606],
         [ 1.15507806, -0.02535171,  1.00747182,  0.31535194],
         [ 1.35352042,  0.92183943, -0.27860469,  0.55476071]]]])
>>> np.random.randint(10, 50, 5)  # low, high=None, size=None (if high is None, random numbers are from 0 to high)
array([22, 39, 32, 17, 31])
```

```python
>>> mat = np.random.randn(1, 2, 3, 4)
>>> type(mat)
numpy.ndarray
>>> mat.size  # 1*2*3*4
24
>>> mat.shape
(1, 2, 3, 4)
>>> mat.shape[2]
3
>>> mat.reshape((6, 4))
array([[-0.78730565, -1.12103096, -1.25998044, -2.44655263],
       [-1.63345988,  0.39682222,  0.82140431, -0.94642159],
       [-1.01014627, -0.3592741 ,  2.1808519 ,  0.26391496],
       [-0.97590643,  0.11774126, -0.99357452,  2.25587485],
       [ 0.17806051,  0.75828643,  2.43265264, -0.17455487],
       [ 1.10789519, -1.19097715, -0.96540053, -0.01954652]])
>>> mat.reshape((6, 4)).shape
(6, 4)
>>> mat.reshape((3, 12))
ValueError: cannot reshape array of size 24 into shape (3,12)
>>> mat.dtype
dtype('float64')
```

## Slicing and Indexing
```python
>>> arr = np.arange(50, 70)
>>> arr
array([50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69])
>>> arr.shape
(20, )
>>> arr[4]
54
>>> arr[:7]
>>> arr[-2]
>>> sum(arr > 55)
14
>>> arr + 100
array([150, 151, 152, 153, 154, 155, 156, 157, 158, 159,160, 161, 162, 163, 164, 165, 166, 167, 168, 169])
>>> arr/2
array([25. , 25.5, 26. , 26.5, 27. , 27.5, 28. , 28.5, 29. , 29.5, 30. , 30.5, 31. , 31.5, 32. , 32.5, 33. , 33.5, 34. , 34.5])
>>> mat = np.random.rand(5, 5)
>>> mat[0, 0]
0.5184802159079592
>>> mat[3, 2]
0.6405912689795946
>>> mat[1, ]
array([0.36347014, 0.73641786, 0.41660211, 0.10915532, 0.84372306])
>>> mat[:, 4]
array([0.07436297, 0.84372306, 0.50454485, 0.96674053, 0.48992084])
>>> mat[1:4, :2]
array([[0.36347014, 0.73641786],
       [0.88653818, 0.07538573],
       [0.47912522, 0.96871028]])
>>> np.cos(mat)
array([[0.86857333, 0.99627561, 0.99984501, 0.66525581, 0.99723635],
       [0.93466875, 0.74087921, 0.91446919, 0.99404847, 0.66468585],
       [0.63209833, 0.99715984, 0.59453021, 0.66684402, 0.87539459],
       [0.88739854, 0.56636293, 0.80174251, 0.96364802, 0.56798521],
       [0.86399855, 0.58841642, 0.96997793, 0.93117836, 0.88237011]])
>>> np.tan(mat)
array([[0.57054557, 0.0865483 , 0.01760806, 1.12229834, 0.07450034],
       [0.38036984, 0.90654223, 0.44250318, 0.10959092, 1.12402417],
       [1.22589817, 0.07552886, 1.3524515 , 1.1174987 , 0.55221847],
       [0.51949947, 1.45517282, 0.74546326, 0.27725377, 1.44904963],
       [0.582749  , 1.37412558, 0.25072009, 0.39150818, 0.53328647]])

>>> mat = np.eye(3, 4)
>>> np.sum(mat, axis=0)  # 0: column-wise, 1: row-wise
array([0.33333333, 0.33333333, 0.33333333, 0.        ])
>>> np.sum(mat, axis=1)
array([0.25, 0.25, 0.25])
>>> np.sum(mat)
3.0
>>> np.mean(mat)
0.25
>>> # np.min(), np.max(), np.
>>> np.sum(mat, axis=-1)  # Sahand's law: last dimension
```

## More Numpy Functions
`hstack`
```python
>>> a = np.eye(3,3)
>>> b = np.eye(3, 5) * 100
>>> np.hstack((a, b))
array([[100.,   0.,   0.,   0.,   0.,   1.,   0.,   0.],
       [  0., 100.,   0.,   0.,   0.,   0.,   1.,   0.],
       [  0.,   0., 100.,   0.,   0.,   0.,   0.,   1.]])
>>> b.T
array([[100.,   0.,   0.],
       [  0., 100.,   0.],
       [  0.,   0., 100.],
       [  0.,   0.,   0.],
       [  0.,   0.,   0.]])
>>> np.vstack((a, b.T))
array([[  1.,   0.,   0.],
       [  0.,   1.,   0.],
       [  0.,   0.,   1.],
       [100.,   0.,   0.],
       [  0., 100.,   0.],
       [  0.,   0., 100.],
       [  0.,   0.,   0.],
       [  0.,   0.,   0.]])
>>> np.floor(np.random.random((3, 5)) * 10)
array([[0., 8., 9., 7., 6.],
       [1., 9., 2., 8., 5.],
       [6., 7., 7., 8., 0.]])
>>> np.ceil(np.random.random((3, 5)) * 10)
array([[ 3.,  5.,  6.,  5.,  6.],
       [ 8.,  5.,  6.,  3.,  8.],
       [ 1.,  6., 10.,  7.,  2.]])
>>> np.cumsum(np.arange(0, 10, 2))
array([ 0,  2,  6, 12, 20])
>>> np.cumproduct(np.arange(2, 10, 2))
array([  2,   8,  48, 384])
>>> np.cumproduct(np.arange(10))
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
>>> np.cumsum(np.random.rand(1, 2, 3))
array([0.42743848, 0.61290531, 1.01909076, 1.09168569, 1.7639229, 2.61748834])
>>> np.unique(np.random.randint(3, 10, 100))
array([3, 4, 5, 6, 7, 8, 9])
```

## Linear Algebra

```python
>>> mat = np.array([[1,2], [3,4]])
>>> np.linalg.det(mat)
-2.0000000000000004
>>> np.linalg.inv(mat)
array([[-2. ,  1. ],
       [ 1.5, -0.5]])
>>> mat.transpose()
array([[1, 3],
       [2, 4]])
>>> mat.T
array([[1, 3],
       [2, 4]])
```

```python
>>> mat_A = np.array([[1,2], [3,4]])
>>> mat_B = np.array([1,2,3], [4,5,6])
>>> mat_A * mat_B  # element wise product
ValueError: operands could not be broadcast together with shapes (2,2) (2,3)
>>> np.dot(mat_A, mat_B)  
array([[ 3,  6,  9],
       [ 7, 14, 21]])
>>> mat_A * mat_A  # element wise product
array([[ 1,  4],
       [ 9, 16]])
>>> np.multiply(mat_A, mat_A)
array([[ 1,  4],
       [ 9, 16]])
```

`Numpy.dot`

Dot product of two arrays. Specifically:

- If both a and b are 1-D arrays, it is inner product of vectors (without complex conjugation).
```python
>>> np.dot([1,2,3], [4,5,6])
32
```
- If both a and b are 2-D arrays, it is matrix multiplication, but using matmul or a @ b is preferred.
```python
>>> np.dot([[1,2,3]], [[4],[5],[6]])
array([[32]])
```
- If either a or b is 0-D (scalar), it is equivalent to multiply and using numpy.multiply(a, b) or a * b is preferred.
```python
>>> np.dot(3, [1,2,3])
array([3, 6, 9])
```
- If a is an N-D array and b is a 1-D array, it is a sum product over the last axis of a and b.
```python
>>> np.dot([[1,2,3], [4,5,6]], [1,2,3])
array([14, 32])
```
- If a is an N-D array and b is an M-D array (where M>=2), it is a sum product over the last axis of a and the second-to-last axis of b.


### Solve Equation
```python
# 2x + y = 1
# x + y = 2
>>> M0 = np.array([[2,1], [1,1]])
>>> M1 = np.array([1,2])
>>> np.linalg.solve(M0, M1)
array([-1, 3.])
```

### Eigenvector, Eigenvalue
```python
>>> mat = np.array([[1,2], [3,4]])
>>> eigvalues, eigvectors = np.linalg.eig(mat)
>>> eigvalues
array([-0.37228132,  5.37228132])
>>> eigvectors
array([[-0.82456484, -0.41597356],
       [ 0.56576746, -0.90937671]])
```

### SVD
```python
>>> C0 = np.array([[1,3,5], [3,-1,6]])
>>> U, sigma, V = np.linalg.svd(C0)
>>> U
array([[-0.6401844 , -0.76822128],
       [-0.76822128,  0.6401844 ]])
>>> sigma
array([8.42614977, 3.16227766])
>>> V
array([[-3.49489188e-01, -1.36756639e-01, -9.26906106e-01],
       [ 3.64399349e-01, -9.31242780e-01,  7.35637502e-17],
       [-8.63174619e-01, -3.37763981e-01,  3.75293313e-01]])
```

## List vs. Numpy Array

- Size - Numpy data structures take up less space
- Performance - they have a need for speed and are faster than lists
- Functionality - `SciPy` and `NumPy` have optimized functions such as linear algebra operations built in.

### Memory
The main benefits of using NumPy arrays should be smaller memory consumption and better runtime behavior.

For Python Lists -  We can conclude from this that for every new element, we need another eight bytes for the reference to the new object. The new integer object itself consumes 28 bytes. The size of a list "lst" without the size of the elements can be calculated with:

`64 + 8 * len(lst) + len(lst) * 28` Bytes

![list](lst.png =300x)

NumPy takes up less space. This means that an arbitrary integer array of length "n" in numpy needs

`96 + n * 8` Bytes

whereas a list of integer

![list](numpy.png =300x)

So the more numbers you need to store - the better you do.

- `numpy` fixed in size, can grow but create complete new array, whereas `list` can grow dynamically.
- `list` - overhead to store all memory location. `numpy` array - only similar data type stored.

```python
import numpy as np
x1 = range(1000)
y1 = range(1000)

x2 = np.arange(1000)
y2 = np.arange(1000)

%%timeit      # works in jupyter notebook cell
[x1[i] * y1[i] for i in range(1000)]

%%timeit      # works in jupyter notebook cell
x2 * y2
```

### Speed
See [`numpy-list.py`](./numpy-list.py).

## Insert, Append, Delete numpy array

### Append
```python
>>> a = np.arange(10, 19)
>>> np.append(a, [20])
array([10, 11, 12, 13, 14, 15, 16, 17, 18, 20])
>>> np.append(a, [20, 21])
array([10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21])
>>> b = a.reshape(3, 3)
>>> b
array([[10, 11, 12],
       [13, 14, 15],
       [16, 17, 18]])
>>> np.append(b, [50, 51, 52])
array([10, 11, 12, 13, 14, 15, 16, 17, 18, 50, 51, 52])
>>> np.append(b, [[50, 51, 52]], axis=0)
array([[10, 11, 12],
       [13, 14, 15],
       [16, 17, 18],
       [50, 51, 52]])
>>> np.append(b, [[50], [51], [52]], axis=1)
array([[10, 11, 12, 50],
       [13, 14, 15, 51],
       [16, 17, 18, 52]])
```

### Insert

```python
>>> np.insert(b, 1, -100)
array([  10, -100,   11,   12,   13,   14,   15,   16,   17,   18])
>>> np.insert(b, 1, -100, axis=0)
array([[  10,   11,   12],
       [-100, -100, -100],
       [  13,   14,   15],
       [  16,   17,   18]])
>>>np.insert(b, 1, -100, axis=1)
array([[  10, -100,   11,   12],
       [  13, -100,   14,   15],
       [  16, -100,   17,   18]])
>>> np.insert(b, 1, [-100, -99, -98], axis=0)
array([[  10,   11,   12],
       [-100,  -99,  -98],
       [  13,   14,   15],
       [  16,   17,   18]])
```

### Delete
```python
>>> np.delete(b, 2)
array([10, 11, 13, 14, 15, 16, 17, 18])
>>> np.delete(b, 1, axis=0)
array([[10, 11, 12],
       [16, 17, 18]])
>>> np.delete(b, 1, axis=1)
array([[10, 12],
       [13, 15],
       [16, 18]])
```

## Split, Concatenate, Tile, and Repeat

### Split
```python
>>> a = np.arange(24).reshape(4, 6)
>>> a
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23]])
>>> np.split(a, 2)
[array([[ 0,  1,  2,  3,  4,  5],
        [ 6,  7,  8,  9, 10, 11]]), array([[12, 13, 14, 15, 16, 17],
        [18, 19, 20, 21, 22, 23]])]
>>> np.split(a, 2)[0]
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11]])
>>> np.split(a, 2, axis=1)
[array([[ 0,  1,  2],
        [ 6,  7,  8],
        [12, 13, 14],
        [18, 19, 20]]), array([[ 3,  4,  5],
        [ 9, 10, 11],
        [15, 16, 17],
        [21, 22, 23]])]
>>> np.split(a, 2, axis=1)[0]
array([[ 0,  1,  2],
       [ 6,  7,  8],
       [12, 13, 14],
       [18, 19, 20]])
>>> np.split(a, 3)  # 4/3!
ValueError: array split does not result in an equal division
```

### Concatenate
```python
>>> b = np.arange(100, 124).reshape(4, 6)

>>> np.concatenate((a, b))
array([[  0,   1,   2,   3,   4,   5],
       [  6,   7,   8,   9,  10,  11],
       [ 12,  13,  14,  15,  16,  17],
       [ 18,  19,  20,  21,  22,  23],
       [100, 101, 102, 103, 104, 105],
       [106, 107, 108, 109, 110, 111],
       [112, 113, 114, 115, 116, 117],
       [118, 119, 120, 121, 122, 123]])
>>> np.concatenate((a, b), axis=1)
array([[  0,   1,   2,   3,   4,   5, 100, 101, 102, 103, 104, 105],
       [  6,   7,   8,   9,  10,  11, 106, 107, 108, 109, 110, 111],
       [ 12,  13,  14,  15,  16,  17, 112, 113, 114, 115, 116, 117],
       [ 18,  19,  20,  21,  22,  23, 118, 119, 120, 121, 122, 123]])
```

### Tile
```python
>>> a = np.arange(8).reshape(2, 4)
>>> a
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])
>>> np.tile(a, 2)
array([[0, 1, 2, 3, 0, 1, 2, 3],
       [4, 5, 6, 7, 4, 5, 6, 7]])
>>> np.tile(a, (2,1))
array([[0, 1, 2, 3],
       [4, 5, 6, 7],
       [0, 1, 2, 3],
       [4, 5, 6, 7]])
>>> np.tile(a, (5, 3))
array([[0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
       [4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7],
       [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
       [4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7],
       [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
       [4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7],
       [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
       [4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7],
       [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
       [4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7]])
```

### Repeat
```python
>>> a = np.arange(8).reshape(2, 4)
>>> a
array([[0, 1, 2, 3],
       [4, 5, 6, 7]])
>>> np.repeat(a, 2)
array([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7])
>>> np.repeat(a, 2, axis=0)
array([[0, 1, 2, 3],
       [0, 1, 2, 3],
       [4, 5, 6, 7],
       [4, 5, 6, 7]])
>>> np.repeat(a, 3, axis=1)
array([[0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3],
       [4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]])
```

## Save `numpy` Array

```python
>>> x = np.arange(10)
>>> np.save("./array.npy", x)
>>> y = np.load("./array.npy")
>>> np.equal(x, y).all()
True
```

## References
- https://webcourses.ucf.edu/courses/1249560/pages/python-lists-vs-numpy-arrays-what-is-the-difference
- https://stackoverflow.com/questions/993984/what-are-the-advantages-of-numpy-over-regular-python-lists