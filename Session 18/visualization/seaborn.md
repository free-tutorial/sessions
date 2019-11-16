















#### Joint Plot
It allows you to basically match up **two distplots for bivariate data**.

`kind`:
- scatter
- reg
- resid
- kde
- hex

```python
df = sns.load_dataset('tips')
sns.jointplot(x='total_bill', y='tip', data=df, kind='kde', height=5)
```
![seaborn](figures/seaborn-jointplot-kde.png =250x)

```python
df = sns.load_dataset('tips')
sns.jointplot(x='total_bill', y='tip', data=df, kind='hex', height=5)
```
![seaborn](figures/seaborn-jointplot-hex.png =250x)


### Axes Level
#### Dist Plot
The distplot shows the distribution of a **univariate** (one variable) set of observations.

```python
>>> df = sns.load_dataset('tips')
>>> sns.distplot(df.total_bill, bins=20)
```
![seaborn](figures/seaborn-hist.png =250x)

```python
>>> df = sns.load_dataset('tips')
>>> sns.distplot(df.total_bill, bins=20, rug=False, hist=False, kde=True)
```
![seaborn](figures/seaborn-nohist.png =250x)

```python
>>> df = sns.load_dataset('tips')
>>> sns.distplot(df.total_bill, bins=20, rug=True, hist=True, kde=True)
```
![seaborn](figures/seaborn-hist-rug-kde.png =250x)

#### Pair Plot
It will plot pairwise relationships across an entire dataframe (for the numerical columns) and supports a color hue argument (for categorical columns).

```python
>>> df = sns.load_dataset('tips')
>>> sns.pairplot(df)
```
![seaborn](figures/seaborn-pairplot.png =500x)

```python
>>> df = sns.load_dataset('tips')
>>> sns.pairplot(df, hue='sex')
```
![seaborn](figures/seaborn-pairplot-hue.png =500x)

`kind`:
- scatter
- reg

`diag_kind`:
- auto
- hist
- kde
```python
>>> df = sns.load_dataset('tips')
>>> sns.pairplot(df, hue='sex', kind='reg', diag_kind='kde')
```
![seaborn](figures/seaborn-pairplot-hue-kind.png =500x)

#### Box Plot
box plot and violinplots are used to show the **distribution of categorical data**.
Order to plot the categorical levels in, otherwise the levels are inferred from the data objects.

```python
>>> sns.boxplot(x='day', y='total_bill', data=df, palette='rainbow', hue_order=['Male', 'Female'], order=['Thur', 'Fri', 'Sat']) #, 'Sun'])
```
![seaborn](figures/seaborn-boxplot.png =250x)

with hue:
```python
>>> sns.boxplot(x='day', y='total_bill', data=df, palette='rainbow', order=['Thur', 'Fri', 'Sat']) #, 'Sun'])
```
![seaborn](figures/seaborn-boxplot-hue.png =250x)

#### Bar Plot
```python
sns.barplot(x='sex', y='total_bill', data=df, hue='day')
```
![seaborn](figures/seaborn-bar-hue.png =250x)

**Error bars** can communicate the following information about your data:
- How spread the data are around the mean value (small SD bar = low spread, data are clumped around the mean; larger SD bar = larger spread, data are more variable from the mean).
- The reliability of the mean value as a representative number for the data set.  In other words, how accurately the mean value represents the data (small SD bar = more reliable, larger SD bar = less reliable). It's important to note that just because you have a larger SD, it does not indicate your data is not valid. Biological measurements are notoriously variable.
- The likelihood of there being a significant difference between between data sets.

#### Count Plot
This is essentially the same as barplot, except the estimator is explicitly counting the number of occurrences. Which is why we only pass the x value.

```python
>>> sns.countplot(x='day', data=df, hue='sex')
```
![seaborn](figures/seaborn-countplot.png =250x)



## Seaborn with Pandas DataFrames
The reason why Seaborn is so great with DataFrames is, for example, because labels from DataFrames are automatically propagated to plots or other data structures, as you saw in the first example of this tutorial, where you plotted a violinplot with Seaborn. There, you saw that the x-axis had a legend total_bill, while this was not the case with the Matplotlib plot. This already takes a lot of work away from you.

## How To Scale Seaborn Plots For Other Contexts
If you need your plots for talks, posters, on paper or in notebooks, you might want to have larger or smaller plots. Seaborn has got you covered on this. You can make use of `set_context()` to control the plot elements:

```python
# Reset default params
>>> sns.set()

# Set context to `"paper"`
>>> sns.set_context("paper")

# Load iris data
>>> iris = sns.load_dataset("iris")

# Construct iris plot
>>> sns.swarmplot(x="species", y="petal_length", data=iris)
```
The four predefined contexts are "paper", "notebook", "talk" and "poster"

You can also pass more arguments to set_context() to scale more plot elements, such as font_scale or more parameter mappings that can override the values that are preset in the Seaborn context dictionaries. In the following code chunk, you overwrite the values that are set for the parameters font.size and axes.labelsize:

```python
# Set context to `"paper"`
>>> sns.set_context("poster", font_scale=0.5, rc={"font.size":1,"axes.labelsize":10})

# Load iris data
>>> iris = sns.load_dataset("iris")

# Construct iris plot
>>> sns.swarmplot(x="species", y="petal_length", data=iris)
```
Additionally, it’s good to keep in mind that you can use the higher-level set() function instead of set_context() to adjust other plot elements:

```python
# Reset default params
>>> sns.set(rc={"font.size":8,"axes.labelsize":5})

# Load iris data
>>> iris = sns.load_dataset("iris")

# Construct iris plot
>>> sns.swarmplot(x="species", y="petal_length", data=iris)
```

## How To Temporarily Set The Plot Style

You can use `axes_style()` in a with statement to temporarily set the plot style. This, in addition to the use of `plt.subplot()`, will allow you to make figures that have differently-styled axes, like in the example below:
```python
# Load data
iris = sns.load_dataset("iris")
tips = sns.load_dataset("tips")

# Set axes style to white for first subplot
with sns.axes_style("whitegrid"):
    plt.subplot(211)
    sns.swarmplot(x="species", y="petal_length", data=iris)

# Initialize second subplot
plt.subplot(212)
# Plot violinplot
sns.violinplot(x = "total_bill", data=tips)
```

## How To Set The Figure Size in Seaborn
For axes level functions, you can make use of the `plt.subplots()` function to which you pass the `figsize` argument.

## References
- https://www.datacamp.com/community/tutorials/seaborn-python-tutorial
- https://seaborn.pydata.org/tutorial/relational.html