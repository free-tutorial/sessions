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
>>> df['sepal_width', 'sepal_length']  # Pandas DataFrame
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

### Selecting Subset of Data
#### Selection with `[ ]`, `.loc` and `.iloc`
Subset selection happens frequently during an actual analysis. This could mean selecting all the rows and some of the columns, some of the rows and all of the columns, or some of each of the rows and columns. Because you are frequently making subset selections, you need to master it in order to make your life with pandas easier.

The documentation uses the term indexing frequently. This term is essentially just a one-word phrase to say ‘subset selection’. Indexing is also the term used in the official Python documentation.

![df-anatomy](df-anatomy.png =700x)

#### The three components of a DataFrame
A DataFrame is composed of three different components, the index, columns, and the data. The data is also known as the values.

The **index** represents the sequence of values on the far left-hand side of the DataFrame. All the values in the index are in bold font. Each individual value of the index is called a label. Sometimes the index is referred to as the row labels. In the example above, the row labels are not very interesting and are just the integers beginning from `0` up to `n-1`, where n is the number of rows in the table. Pandas defaults DataFrames with this simple index.

#### Pandas dual references: by label and by integer location
Each row and each column have a specific label that can be used to reference them. Each row and column may be referenced by an integer as well. I call this integer location. The integer location begins at 0 and ends at n-1 for each row and column.

Square brackets (`[]`), `.loc` and `.iloc`. Collectively, they are called the indexers. These are by far the most common ways to select data.

If you have a DataFrame, df, your subset selection will look something like the following:
```python
df[ ]
df.loc[ ]
df.iloc[ ]
```

#### Extracting the individual DataFrame components
```python
>>> df = pd.read_csv("state.csv", index_col=0)
>>> df.index
Index(['Jane', 'Niko', 'Aaron', 'Penelope', 'Dean', 'Christina', 'Cornelia'], dtype='object')
>>> df.columns
Index(['state', 'color', 'food', 'age', 'height', 'score'], dtype='object')
>>> df.values
array([['NY', 'blue', 'Steak', 30, 165, 4.6],
       ['TX', 'green', 'Lamb', 2, 70, 8.3],
       ['FL', 'red', 'Mango', 12, 120, 9.0],
       ['AL', 'white', 'Apple', 4, 80, 3.3],
       ['AK', 'gray', 'Cheese', 32, 180, 1.8],
       ['TX', 'black', 'Melon', 33, 172, 9.5],
       ['TX', 'red', 'Beans', 69, 150, 2.2]], dtype=object)
>>> type(df.index)
pandas.core.indexes.base.Index
>>> type(df.columns)
pandas.core.indexes.base.Index
>>> type(df.values)
numpy.ndarray
```

Note: Interestingly, both the index and the columns are the same type. They are both a pandas Index object. This object is quite powerful in itself, but for now you can just think of it as a sequence of labels for either the rows or the columns.

#### Selecting a single column as a Series
Selecting a single column of data returns the other pandas data container, the Series. A Series is a one-dimensional sequence of labeled data. There are two main components of a Series, the index and the data(or values). There are NO columns in a Series.

```python
>>> df['food']
Jane          Steak
Niko           Lamb
Aaron         Mango
Penelope      Apple
Dean         Cheese
Christina     Melon
Cornelia      Beans
Name: food, dtype: object
>>> df.food
Jane          Steak
Niko           Lamb
Aaron         Mango
Penelope      Apple
Dean         Cheese
Christina     Melon
Cornelia      Beans
Name: food, dtype: object
```

You will also notice two extra pieces of data on the bottom of the Series. The name of the Series becomes the old-column name.

#### Selecting multiple columns with just the indexing operator
```python
>>> df['color', 'age'] # should be:  df[['color', 'age']]
KeyError: ('color', 'age')
>>> df[['color', 'food', 'score']]

       color	food	score
Jane	blue	Steak	4.6
Niko	green	Lamb	8.3
Aaron	red	Mango	9.0
Penelope	white	Apple	3.3
Dean	gray	Cheese	1.8
Christina	black	Melon	9.5
Cornelia	red	Beans	2.2
```

Selecting multiple columns returns a DataFrame. You can actually select a single column as a DataFrame with a one-item list:

```python
>>> df[['food']]

       food
Jane	Steak
Niko	Lamb
Aaron	Mango
Penelope	Apple
Dean	Cheese
Christina	Melon
Cornelia	Beans
```

#### `.loc` operator
`.loc` can select subsets of rows or columns. It can also simultaneously select subsets of rows and columns. Most importantly, it only selects data by the LABEL of the rows and columns.

##### Select a single row or multiple rows
Single row returns a `Series`.
```python
>>> df.loc['Niko']
state        TX
color     green
food       Lamb
age           2
height       70
score       8.3
Name: Niko, dtype: object
```

Multiple rows returns a `DataFrame`
```python
>>> df.loc[['Niko', 'Penelope']]
       state	color	food	age	height	score
Niko	TX	green	Lamb	2	70	8.3
Penelope	AL	white	Apple	4	80	3.3
```

##### Select a Range of Rows
```python
>>> df['Niko':'Christian':2]  # start, stop, step
       state	color	food	age	height	score
Niko	TX	green	Lamb	2	70	8.3
Penelope	AL	white	Apple	4	80	3.3
Christina	TX	black	Melon	33	172	9.5
>>> # other examples include: df['Niko':], df[:'Dean']
```

Notice that the row labeled with `Christina` was kept. In other data containers such as Python lists, the last value is excluded

##### Selecting Rows and Columns Simultaneously

```python
>>> df.loc[['Dean', 'Cornelia'], ['age', 'state', 'score']]
# DataFrame
       age	state	score
Dean	32	AK	1.8
Cornelia	69	TX	2.2
```

```python
>>> df.loc['Niko':'Christina':2 , ['state', 'age']]
# DataFrame
       state	age
Niko	TX	2
Penelope	AL	4
Christina	TX	33
```

```python
>>> df.loc[['Dean'], ['age', 'state', 'score']]
# DataFrame
       age	state	score
Dean	32	AK	1.8
```

```python
>>> df.loc['Dean', ['age', 'state', 'score']]
# Series
age       32
state     AK
score    1.8
Name: Dean, dtype: object
```

```python
>>> df.loc['Dean', ['age']]
# Series
age    32
Name: Dean, dtype: object
```

```python
>>> df.loc['Dean', 'age']
# Scalar
32
```

```python
>>> df.loc[:'Dean', 'height':]
# DataFrame
       height	score
Jane	165	4.6
Niko	70	8.3
Aaron	120	9.0
Penelope	80	3.3
Dean	180	1.8
```

All rows and some columns
```python
>>> df.loc[:, ['food', 'color']]
       food	color
Jane	Steak	blue
Niko	Lamb	green
Aaron	Mango	red
Penelope	Apple	white
Dean	Cheese	gray
Christina	Melon	black
Cornelia	Beans	red
```

All columns and some rows
```python
>>> df.loc[['Penelope','Cornelia'], :]
              state	color	food	age	height	score
Penelope	AL	white	Apple	4	80	3.3
Cornelia	TX	red	Beans	69	150	2.2
```

#### References
- https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c
