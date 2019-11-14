# Pandas
## Visualization

Pandas visualization gives you another high level of visualization.

Series:
```python
>>> ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
>>> ts = ts.cumsum()
>>> ts.plot()
```

DataFrame:
```python
>>> df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
>>> df = df.cumsum()
>>> plt.figure()
>>> df.plot()
```

Note: by default `df.plot`, plots by index which can be changed:
```python
>>> df = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()
>>> df['A'] = pd.Series(list(range(len(df))))
>>> df.plot(x='A', y='B')
```

Note: check [`pd.date_range()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.date_range.html).

### Line Plot
```python
>>> df = pd.DataFrame(np.random.randn(100, 5))
>>> df.plot()
```
![plot](figures/plot_all.png =250x)
```python
>>> df[0].plot()  # or df[0].plot.line()
```
![plot](figures/plot_0.png =250x)
```python
>>> df[[0, 2]].plot()
```
![plot](figures/plot_0-2.png =250x)

### Vertical Bar Plot
Use vertical column charts when you’re graphing ordinal variables.

### Horizontal Bar Plot
Use horizontal bar charts when you’re graphing nominal variables.
```python
>>> df = pd.read_csv('datasets/titanic.csv')
>>> df.Sex.value_counts().plot(kind='barh')
```
![plot](figures/titanic-sex-barh.png =250x)


Stacked Horizontal Bar Plot:
```python
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df.plot.bar(stacked=True)
```
![plot](figures/pandas-stacked.png =250x)

### Scatter Plot
```python
>>> df.plot(x=0, y=1, kind='scatter')  # or df.plot.scatter(x=0, y=1)
```
![plot](figures/plot-scatter-0-1.png =250x)


```python
>>> df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
>>> ax = df.plot.scatter(x='a', y='b', color='g', label='Group 1', s=30)
>>> df.plot.scatter(x='c', y='d', color='y', label='Group 2', ax=ax, s=30)
```
![plot](figures/pandas-scatter-ax.png =250x)


The keyword c may be given as the name of a column to provide colors for each point:
```python
df.plot.scatter(x='a', y='b', c='c', s=50, colormap='Blues')
```
![plot](figures/pandas-scatter-colormap.png =250x)

For a list of colormaps, see: [matplotlib.colormaps](https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html)

You can pass other keywords supported by matplotlib scatter. The example below shows a bubble chart using a column of the DataFrame as the bubble size.

```python
>>> df.plot.scatter(x='a', y='b', s=df['c']*100)
```
![plot](figures/pandas-scatter-size.png =250x)

### Hexagonal Bin Plot
Hexbin plots can be a useful alternative to scatter plots if your data are too dense to plot each point individually.

```python
>>> df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
>>> df['b'] = df['b'] + np.arange(1000)
>>> df.plot(kind='hexbin', x='a', y='b', gridsize=15)
```
![plot](figures/pandas-hexbin.png =250x)

### Histogram Plot
```python
>>> df.Age.plot(kind='hist')
```
![plot](figures/titanic-age-hist.png =250x)

**Transparent**:
```python
>>> df = pd.DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000), 'c': np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
>>> df.plot.hist(y=['a', 'b'], bins=40, alpha=0.5)
```
![plot](figures/hist-transparent.png =250x)

**Cumulative**:
```python
>>> df = pd.DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000), 'c': np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
>>> df.plot.hist(y=['a'], bins=40, alpha=0.5, cumulative=True)
```

### Box Plot
```python
>>> df[['Age']].boxplot(kind='box')
```
![plot](figures/titanic-age-box.png =250x)

```python
df = pd.read_csv('Session 18/visualization/iris.csv')
df.plot.box()
```
![plot](figures/pandas-boxplot-iris.png =250x)

### Density Plot
```python
>>> df.Age.plot(kind='density')
```
![plot](figures/titanic-age-density.png =250x)


### Pie Plot
```python
>>> df.Sex.value_counts().plot(kind='pie')
```
![plot](figures/titanic-sex-pie.png =250x)

### Area Plot
```python
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df.plot(kind='area')
```
![plot](figures/pandas-area.png =250x)

```python
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df[['a', 'b']].plot(kind='area', stacked=False)
```
![plot](figures/pandas-area-unstacked.png =250x)


Note: Area plots are stacked by default. To produce stacked area plot, each column must be either all positive or all negative values.

## Plotting with Missing Data
Pandas tries to be pragmatic about plotting DataFrames or Series that contain missing data. Missing values are dropped, left out, or filled depending on the plot type.

|Plot Type|`NaN` Handling|
|--|--|
|Line| gaps at NaNs|
|Line|stacked)	Fill 0’s|
|Bar| 0’s|
|Scatter| NaNs|
|Histogram| NaNs (column-wise)|
|Box| NaNs (column-wise)|
|Area| 0’s|
|KDE| NaNs (column-wise)|
|Hexbin| NaNs|
|Pie| 0’s|

## References
- https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html