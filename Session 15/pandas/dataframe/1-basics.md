# `pandas`

## DataFrame

Nothing but a 2 dimensional data structure.

```python
>>> data = np.random.rand(5, 3)
>>> df = pd.DataFrame(arr, columns=['A', 'B', 'C'])
```

`read_csv` params:
- `header`
- `usecols`
- `delimiter`
- `squeeze`
- `names`
```python
>>> data = pd.read_csv("iris.csv")
>>> type(df)
pandas.core.frame.DataFrame
>>> df.head()
>>> df.head(2)
>>> df.tail()
>>> df.index
RangeIndex(start=0, stop=150, step=1)
>>> df.values
array([[5.1, 3.5, 1.4, 0.2, 'setosa'],
       [4.9, 3.0, 1.4, 0.2, 'setosa'],
       [4.7, 3.2, 1.3, 0.2, 'setosa'],
       [4.6, 3.1, 1.5, 0.2, 'setosa'],
                    ...
       [6.7, 3.3, 5.7, 2.5, 'virginica'],
       [6.7, 3.0, 5.2, 2.3, 'virginica'],
       [6.3, 2.5, 5.0, 1.9, 'virginica'],
       [6.5, 3.0, 5.2, 2.0, 'virginica'],
       [6.2, 3.4, 5.4, 2.3, 'virginica'],
       [5.9, 3.0, 5.1, 1.8, 'virginica']], dtype=object)
>>> df.shape
(150, 5)
>>> df.size
750
>>> df.columns
Index(['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'], dtype='object')
>>> df.dtypes
sepal_length    float64
sepal_width     float64
petal_length    float64
petal_width     float64
species          object
dtype: object
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
sepal_length    150 non-null float64
sepal_width     150 non-null float64
petal_length    150 non-null float64
petal_width     150 non-null float64
species         150 non-null object
dtypes: float64(4), object(1)
memory usage: 5.9+ KB
>>> df.get_dtype_counts()
float64    4
object     1
dtype: int64
>>> df.axes
[RangeIndex(start=0, stop=150, step=1),
 Index(['sepal_length', 'sepal_width', 'petal_length', 'petal_width',
        'species'],
       dtype='object')]
>>> df.describe()  # statistical information on numerical columns
```

### New Column
```python
>>> df['extra'] = 5
>>> df['extra'] = df['new species']
>>> df['extra'] = df['sepal_length'] * 10
```

### Select One or More Columns
```python
>>> df.sepal_width  # Pandas Series
>>> df['sepal_width']  # Pandas Series
>>> df[['sepal_width', 'sepal_length']]  # Pandas DataFrame
```

### Operations
```python
>>> df['sepal_length'] * 10
>>> df['sepal_length'] * df['sepal_width']  # element-wise operation
```

### Drop Missing Row or Column
```python
>>> df = pd.DataFrame([[np.nan, 2, np.nan, 0], [3, 4, np.nan, 1], [np.nan, np.nan, np.nan, 5], [np.nan, np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan, 8]], columns=['A', 'B', 'C', 'D'])
>>> df.dropna(axis=0, how='all')
>>> df.dropna(axis=0, how='any')
>>> df.dropna(axis=1, how='any')
>>> df.dropna(axis=1, how='any')
>>> df.dropna(axis=0, thresh=2)  # Require that many non-NA values.
>>> df.dropna(axis=0, threshold=2, inplace=True)  # If `inplace` is `True`, do operation inplace and return None.
>>> df.drop(index=3)  # drop single row
>>> df.drop(index=[1,2])  # drop multiple rows
>>> df.drop(columns=['A', 'B'])  # drop multiple columns
>>> df.drop(labels=[1,2])  # drop multiple rows
>>> df.drop(labels=['A', 'B'], axis=1)  # drop multiple columns
```

### Filter
#### Single Condition
```python
>>> df.species == 'setosa'
0       True
1       True
2       True
       ...
148    False
149    False
Name: species, Length: 150, dtype: bool
>>> df[df.species == 'setosa']
# returns a DataFrame
>>> df[df.sepal_length > 7]
# returns a DataFrame
```

#### Multiple Condition
```python
>>> con_1 = df.sepal_length > 5
>>> con_2 = df.species == 'setosa'
>>> con_3 = df.species == ''
>>> (con_1 & con_2).head()
0     True
1    False
2    False
3    False
4    False
dtype: bool
>>> df[con_1 & con_2]
# returns a DataFrame
>>> df[con_1 & (con_2 | con_3)]
# returns a DataFrame
```

#### `isin()`
```python
>>> df.species.unique()
array(['setosa', 'versicolor', 'virginica'], dtype=object)
>>> df.species.isin(['setosa', 'versicolor'])
0       True
1       True
2       True
3       True
4       True
       ...  
145    False
146    False
147    False
148    False
149    False
Name: species, Length: 150, dtype: bool
>>> df[df.species.isin(['setosa', 'versicolor'])]
# returns a DataFrame
```

#### `.between()`
```python
>>> df.sepal_width.between(3, 4)
0       True
1       True
2       True
3       True
4       True
       ...  
145     True
146    False
147     True
148     True
149     True
Name: sepal_width, Length: 150, dtype: bool
>>> df[df.sepal_width.between(3, 4)]
# returns a DataFrame
```

### `unique` and `nunique`
```python
>>> df.species.unique()
array(['setosa', 'versicolor', 'virginica'], dtype=object)
>>> df.species.nunique()
3
>>> df.sepal_length.unique()
array([5.1, 4.9, 4.7, 4.6, 5. , 5.4, 4.4, 4.8, 4.3, 5.8, 5.7, 5.2, 5.5,
       4.5, 5.3, 7. , 6.4, 6.9, 6.5, 6.3, 6.6, 5.9, 6. , 6.1, 5.6, 6.7,
       6.2, 6.8, 7.1, 7.6, 7.3, 7.2, 7.7, 7.4, 7.9])
>>> df.sepal_length.nunique()
35
```

### Sorting
```python
>>> df.sort_values(by='sepal_width', ascending=True, inplace=True)
>>> df
sepal_length  sepal_width   petal_length  petal_width   species
60	5.0	2.0	3.5	1.0	versicolor
62	6.0	2.2	4.0	1.0	versicolor
119	6.0	2.2	5.0	1.5	virginica
68	6.2	2.2	4.5	1.5	versicolor
41	4.5	2.3	1.3	0.3	setosa
...	...	...	...	...	...
16	5.4	3.9	1.3	0.4	setosa
14	5.8	4.0	1.2	0.2	setosa
32	5.2	4.1	1.5	0.1	setosa
33	5.5	4.2	1.4	0.2	setosa
15	5.7	4.4	1.5	0.4	setosa
150 rows × 5 columns
```

You can also sort by multiple columns
```python
>>> df.sort_values(by=['sepal_length', 'sepal_width'])

sepal_length  sepal_width   petal_length  petal_width   species
13	4.3	3.0	1.1	0.1	setosa
8	4.4	2.9	1.4	0.2	setosa
38	4.4	3.0	1.3	0.2	setosa
42	4.4	3.2	1.3	0.2	setosa
41	4.5	2.3	1.3	0.3	setosa
...	...	...	...	...	...
118	7.7	2.6	6.9	2.3	virginica
122	7.7	2.8	6.7	2.0	virginica
135	7.7	3.0	6.1	2.3	virginica
117	7.7	3.8	6.7	2.2	virginica
131	7.9	3.8	6.4	2.0	virginica
150 rows × 5 columns
```

You can also sort a DataFrame column (a series) directly.
```python
>>> df.sepal_width.sort_values(ascending=True)
60     2.0
62     2.2
119    2.2
68     2.2
41     2.3
      ... 
16     3.9
14     4.0
32     4.1
33     4.2
15     4.4
Name: sepal_width, Length: 150, dtype: float64
>>> df.sepal_width.sort_values(ascending=True, inplace=True)
ValueError: This Series is a view of some other array, to sort in-place you must create a copy
>>> s = df.sepal_width
>>> s.sort_values(inplace=True)  # this is still a reference to DataFrame
ValueError: This Series is a view of some other array, to sort in-place you must create a copy
>>> s = df.sepal_width.copy()  # this is a copy and inplace sorting is valid
>>> s.sort_values(inplace=True)
>>> s
60     2.0
62     2.2
119    2.2
68     2.2
41     2.3
      ... 
16     3.9
14     4.0
32     4.1
33     4.2
15     4.4
Name: sepal_width, Length: 150, dtype: float64
```

Sort by index
```python
>>> df.sort_index(ascending=False)
sepal_length  sepal_width     petal_length       petal_width   species
149	5.9	3.0	5.1	1.8	virginica
148	6.2	3.4	5.4	2.3	virginica
147	6.5	3.0	5.2	2.0	virginica
146	6.3	2.5	5.0	1.9	virginica
145	6.7	3.0	5.2	2.3	virginica
...	...	...	...	...	...
4	5.0	3.6	1.4	0.2	setosa
3	4.6	3.1	1.5	0.2	setosa
2	4.7	3.2	1.3	0.2	setosa
1	4.9	3.0	1.4	0.2	setosa
0	5.1	3.5	1.4	0.2	setosa
150 rows × 5 columns
```
