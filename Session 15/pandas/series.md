# `pandas`

## Series

Series: one single column of tabular Data/DataFrame (one dimensional labeled array)

Note: `pandas` dataframe can hold any data type.

```python
import pandas as pd

lst = [1,2,3]
s = pd.Series(lst)
s_with_index = pd.Series(lst, index=[0,1,2])
s_with_index = pd.Series({0: 1, 1:2, 2:3})
```

### Series from `csv` file
params:
- `header`: `int`, list of `int`, default `infer`

  Row number(s) to use as the column names, and the start of the data. Default behavior is to infer the column names: if no names are passed the behavior is identical to `header=0` and column names are inferred from the first line of the file, if column names are passed explicitly then the behavior is identical to `header=None`.
- `names` : array-like, optional

  List of column names to use. If file contains no header row, then you should explicitly pass `header=None`. Duplicates in this list are not allowed.
- `squeeze` : `bool`, default `False`

  If the parsed data only contains one column then return a Series.

1. Example #1
```csv
Ali
Reza
Amir
Mojtaba
```

```python
>>> pd.read_csv("./file.csv", header=None, squeeze=True, names=["name"])  # will load a series of data named `employee_names`
0        Ali
1       Reza
2       Amir
3    Mojtaba
Name: name, dtype: object
```

2. Example #2
```csv
name,last_name
Ali,Hejazizo
Shahab,Hosseini
Amir,Jafari
```

```python
>>> pd.read_csv("./file.csv", header=0, squeeze=True, usecols=['name'])
0       Ali
1    Shahab
2      Amir
Name: name, dtype: object
```

### Series Attributes and Methods

1. 
```csv
name,last_name
Ali,Hejazizo
Shahab,Hosseini
Amir,Jafari
```

```python
>>> s = pd.read_csv('file.csv', squeeze=True, usecols=['name'])
>>> s.index
RangeIndex(start=0, stop=3, step=1)
>>> s.values
array(['Ali', 'Shahab', 'Amir'], dtype=object)
>>> s.dtype
dtype('O')
>>> s.ndim
1
>>> s.is_unique
True
```

2. 

```python
>>> s = pd.Series(np.linspace(10, 20, 30))
>>> s
0    10.000000
1    11.428571
2    12.857143
3    14.285714
4    15.714286
5    17.142857
6    18.571429
7    20.000000
dtype: float64
>>> s.sum()
120.0
>>> s.max()
20.0
>>> s.idxmax()  # the same for `min`
7
>>> s.tail()
3    14.285714
4    15.714286
5    17.142857
6    18.571429
7    20.000000
dtype: float64
>>> s.head(3)
0    10.000000
1    11.428571
2    12.857143
dtype: float64
>>> s.mean()
15.0
>>> s.std()
3.4992710611188254
>>> s.shape
(8, )
```

```python
>>> s = pd.Series(np.linspace(10, 20, 30))
>>> s.describe()
count    30.000000
mean     15.000000
std       3.035658
min      10.000000
25%      12.500000
50%      15.000000
75%      17.500000
max      20.000000
dtype: float64
```

### Label Indexing

```python
>>> temperature = [30, 31, 32, 33, 34, 32, 30, 31, 29, 33, 34, 32]
>>> months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
>>> s = pd.Series(temperature)
>>> s
0     30
1     31
2     32
3     33
4     34
5     32
6     30
7     31
8     29
9     33
10    34
11    32
dtype: int64
>>> s.index
RangeIndex(start=0, stop=12, step=1)
>>> s = pd.Series(temperature, months)  # pd.Series(data=temperature, index=months)
>>> s
Jan    30
Feb    31
Mar    32
Apr    33
May    34
Jun    32
Jul    30
Aug    31
Sep    29
Oct    33
Nov    34
Dec    32
dtype: int64
>>> s.index
Index(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
       'Nov', 'Dec'],
      dtype='object')
```

### `sort_value`, `sort_index`, in-place

```python
>>> s.sort_values()
Sep    29
Jan    30
Jul    30
Feb    31
Aug    31
Mar    32
Jun    32
Dec    32
Apr    33
Oct    33
May    34
Nov    34
dtype: int64
>>> s.sort_values(ascending=True)
Nov    34
May    34
Oct    33
Apr    33
Dec    32
Jun    32
Mar    32
Aug    31
Feb    31
Jul    30
Jan    30
Sep    29
dtype: int64
>>> s.sort_index()
Sep    29
Oct    33
Nov    34
May    34
Mar    32
Jun    32
Jul    30
Jan    30
Feb    31
Dec    32
Aug    31
Apr    33
dtype: int64
>>> s.sort_index(ascending=True)
Apr    33
Aug    31
Dec    32
Feb    31
Jan    30
Jul    30
Jun    32
Mar    32
May    34
Nov    34
Oct    33
Sep    29
dtype: int64
```

`inplace`: If `True`, perform operation in-place.
```python
>>> s1.sort_values(inplace=True)
>>> s1
Sep    29
Jan    30
Jul    30
Feb    31
Aug    31
Mar    32
Jun    32
Dec    32
Apr    33
Oct    33
May    34
Nov    34
dtype: int64
```

### Apply python built-in functions on Series

```python
>>> len(s)
12
>>> type(s)
pandas.core.series.Series
>>> list(s)
[30, 31, 32, 33, 34, 32, 30, 31, 29, 33, 34, 32]
>>> dict(s)
{'Jan': 30,
 'Feb': 31,
 'Mar': 32,
 'Apr': 33,
 'May': 34,
 'Jun': 32,
 'Jul': 30,
 'Aug': 31,
 'Sep': 29,
 'Oct': 33,
 'Nov': 34,
 'Dec': 32}
>>> sorted(s)
[29, 30, 30, 31, 31, 32, 32, 32, 33, 33, 34, 34]
>>> max(s), min(s)
(34, 29)
```

### Indexing
```python
>>> s[0]
30
>>> s[5]
32
>>> [2:8]
Mar    32
Apr    33
May    34
Jun    32
Jul    30
Aug    31
dtype: int64
>>> s[[0, 1]]
Jan    30
Feb    31
dtype: int64
>>> s[[-1, -2]]
Dec    32
Nov    34
dtype: int64
>>> s[-5:-2]
Aug    31
Sep    29
Oct    33
dtype: int64
>>> s[['May', 'Nov', 'Dec']]
May    34
Nov    34
Dec    32
dtype: int64
```

### Methods
#### `value_counts`
```python
>>> s = pd.Series(['Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Female', 'Female'])
>>> s.nunique()
2
>>> s.value_counts()
Male      5
Female    3
dtype: int64
```

#### `apply` and `map`
```python
def convertTemp(C):
      return C * 1.8 + 32
>>> temperature = [30, 31, 32, 33, 34, 32, 30, 31, 29, 33, 34, 32]
>>> months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
>>> s = pd.Series(temperature, months)
>>> s.apply(convertTemp)
Jan    86.0
Feb    87.8
Mar    89.6
Apr    91.4
May    93.2
Jun    89.6
Jul    86.0
Aug    87.8
Sep    84.2
Oct    91.4
Nov    93.2
Dec    89.6
dtype: float64
>>> s.apply(lambda c: c * 1.8 + 32)
>>> mapobj = {30: 300, 31: 310, 32: 40, 34: 100}
>>> s.map(mapobj)
Jan    300.0
Feb    310.0
Mar     40.0
Apr      NaN
May    100.0
Jun     40.0
Jul    300.0
Aug    310.0
Sep      NaN
Oct      NaN
Nov    100.0
Dec     40.0
dtype: float64
```
