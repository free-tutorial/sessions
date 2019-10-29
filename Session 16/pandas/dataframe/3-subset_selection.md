# Pandas

## Selecting Subset of Data
### Selection with `[ ]`, `.loc` and `.iloc`
Subset selection happens frequently during an actual analysis. This could mean selecting all the rows and some of the columns, some of the rows and all of the columns, or some of each of the rows and columns. Because you are frequently making subset selections, you need to master it in order to make your life with pandas easier.

The documentation uses the term indexing frequently. This term is essentially just a one-word phrase to say ‘subset selection’. Indexing is also the term used in the official Python documentation.

![df-anatomy](df-anatomy.png =700x)

### The three components of a DataFrame
A DataFrame is composed of three different components, the index, columns, and the data. The data is also known as the values.

The **index** represents the sequence of values on the far left-hand side of the DataFrame. All the values in the index are in bold font. Each individual value of the index is called a label. Sometimes the index is referred to as the row labels. In the example above, the row labels are not very interesting and are just the integers beginning from `0` up to `n-1`, where n is the number of rows in the table. Pandas defaults DataFrames with this simple index.

### Pandas dual references: by label and by integer location
Each row and each column have a specific label that can be used to reference them. Each row and column may be referenced by an integer as well. I call this integer location. The integer location begins at 0 and ends at n-1 for each row and column.

Square brackets (`[]`), `.loc` and `.iloc`. Collectively, they are called the indexers. These are by far the most common ways to select data.

If you have a DataFrame, df, your subset selection will look something like the following:
```python
df[ ]
df.loc[ ]
df.iloc[ ]
```

### Extracting the individual DataFrame components
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

### Selecting a single column as a Series
Selecting a single column of data returns the other pandas data container, the Series. A Series is a one-dimensional sequence of labeled data. There are two main components of a Series, the index and the data(or values). There are **NO columns** in a Series.

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

### Selecting multiple columns with just the indexing operator
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

### Using just the indexing operator to select rows from a DataFrame — Confusing!
Writing `df['abc']` selects a column, but writing `df[2:4]` selects rows!

Use `.loc` and `.iloc` operators.

### `.loc` Operator
`.loc` can select subsets of rows or columns. It can also simultaneously select subsets of rows and columns. Most importantly, it only selects data by the LABEL of the rows and columns.

#### Select a single row or multiple rows
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

#### Select a Range of Rows
```python
>>> df.loc['Niko':'Christian':2]  # start, stop, step
       state	color	food	age	height	score
Niko	TX	green	Lamb	2	70	8.3
Penelope	AL	white	Apple	4	80	3.3
Christina	TX	black	Melon	33	172	9.5
>>> # other examples include: df['Niko':], df[:'Dean']
```

Notice that the row labeled with `Christina` was kept. In other data containers such as Python lists, the last value is excluded

#### Selecting Rows and Columns Simultaneously

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

### `.iloc` Operator
The `.iloc` indexer is very similar to .loc but only uses integer locations to make its selections. The word `.iloc` itself stands for integer location so that should help with remember what it does.

```python
>>> df.iloc[[2,3,4], [0, 4]]       # DataFrame
>>> df.iloc[2:8:2, [0, 1, 2]]      # DataFrame
>>> df.iloc[[2], [0, 1, 2]]        # DataFrame
>>> df.iloc[2, [0, 1, 2]]          # Series
>>> df.iloc[2, [0]]                # Series
>>> df.iloc[2, 0]                  # Scalar
>>> df.iloc[0:5, 2]                # Series
>>> df.iloc[[1,2,3], 3]            # Series
```

### Series selection with `.loc`
Series selection with .loc is quite simple, since we are only dealing with a single dimension.

```python
>>> food.loc['Aaron']
'Mango'
```

```python
>>> food.loc[['Dean', 'Niko', 'Cornelia']]
Dean        Cheese
Niko          Lamb
Cornelia     Beans
Name: food, dtype: object
```

```python
>>> food.loc['Niko':'Christina']
Niko           Lamb
Aaron         Mango
Penelope      Apple
Dean         Cheese
Christina     Melon
Name: food, dtype: object
```

```python
>>> food.loc['Penelope':]
Penelope      Apple
Dean         Cheese
Christina     Melon
Cornelia      Beans
Name: food, dtype: object
```

```python
>>> food.loc[['Aaron']]
Aaron    Mango
Name: food, dtype: object
```

### Series selection with .iloc
```python
>>> food.iloc[0]
'Steak'
```

```python
>>> food.iloc[[4, 1, 3]]
Dean        Cheese
Niko          Lamb
Penelope     Apple
Name: food, dtype: object
```

```python
>>> food.iloc[4:6]
Dean         Cheese
Christina     Melon
Name: food, dtype: object
```

### Comparison to Python lists and dictionaries
Python lists allow for selection of data only through integer location. You can use a single integer or slice notation to make the selection but **NOT** a list of integers.

All values in each dictionary are labeled by a key. We use this key to make single selections. Dictionaries only allow selection with a single label. Slices and lists of labels are not allowed.

### Setting an index from a column after reading in data
It is common to see pandas code that reads in a DataFrame with a RangeIndex and then sets the index to be one of the columns. This is typically done with the `set_index` method:

```python
>>> df2_idx = df2.set_index('Names')
>>> df2_idx
```

### References
- https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c
