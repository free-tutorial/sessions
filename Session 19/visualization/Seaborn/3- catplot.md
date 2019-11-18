# Seaborn
## Plotting with categorical data with `catplot` (figure level)
If one of the main variables is “categorical” (divided into discrete groups) it may be helpful to use a more specialized approach to visualization.

There are a number of axes-level functions for plotting categorical data in different ways and a figure-level interface, `catplot()`, that gives unified higher-level access to them.

It’s helpful to think of the different categorical plot kinds as belonging to three different families, which we’ll discuss in detail below. They are:

1. Categorical scatterplots:
- `stripplot()` (with kind="strip"; the default)
- `swarmplot()` (with kind="swarm")

2. Categorical distribution plots:
- `boxplot()` (with kind="box")
- `violinplot()` (with kind="violin")
- `boxenplot()` (with kind="boxen")

3. Categorical estimate plots:
- `pointplot()` (with kind="point")
- `barplot()` (with kind="bar")
- `countplot()` (with kind="count")

### Categorical Scatterplot
There are actually two different categorical scatter plots in seaborn. The approach used by `stripplot()`, which is the default “kind” in `catplot()` is to adjust the positions of points on the categorical axis with a small amount of random “jitter”:

```python
tips = sns.load_dataset("tips")
sns.catplot(x="day", y="total_bill", data=tips)
```
![seaborn](../figures/seaborn-catplot-jitter.png =250x)

The jitter parameter controls the magnitude of jitter or disables it altogether:

```python
tips = sns.load_dataset("tips")
sns.catplot(x="day", y="total_bill", jitter=False, data=tips)
```
![seaborn](../figures/seaborn-catplot-nojitter.png =250x)

The second approach adjusts the points along the categorical axis using an algorithm that prevents them from overlapping. It can give a better representation of the distribution of observations, although it only works well for relatively small datasets.

```python
sns.catplot(x="day", y="total_bill", kind="swarm", data=tips)
```
![seaborn](../figures/seaborn-catplot-swarm.png =250x)

```python
sns.catplot(x="day", y="total_bill", kind="swarm", data=tips, hue='time')
```
![seaborn](../figures/seaborn-catplot-swarm-hue.png =250x)

Unlike with numerical data, it is not always obvious how to order the levels of the categorical variable along its axis. In general, the seaborn categorical plotting functions try to infer the order of categories from the data.

The ordering can also be controlled on a plot-specific basis using the `order` parameter. This can be important when drawing multiple categorical plots in the same figure, which we’ll see more of below:

```python
sns.catplot(x="smoker", y="tip", order=["No", "Yes"], data=tips)
```
![seaborn](../figures/seaborn-catplot-order.png =250x)

## Distributions of observations within categories
As the size of the dataset grows,, categorical scatter plots become limited in the information they can provide about the distribution of values within each category. When this happens, there are several approaches for summarizing the distributional information in ways that facilitate easy comparisons across the category levels.

### Box plots
This kind of plot shows the three quartile values of the distribution along with extreme values.

```python
sns.catplot(x="day", y="total_bill", kind="box", data=tips)
```
![seaborn](../figures/seaborn-boxplot.png =250x)

When adding a hue semantic, the box for each level of the semantic variable is moved along the categorical axis so they don’t overlap:
```python
sns.catplot(x="day", y="total_bill", hue="smoker", kind="box", data=tips)
```
![seaborn](../figures/seaborn-catplot-hue.png =250x)

This behavior is called “dodging” and is turned on by default because it is assumed that the semantic variable is nested within the main categorical variable. If that’s not the case, you can disable the dodging:

```python
tips["weekend"] = tips["day"].isin(["Sat", "Sun"])
sns.catplot(x="day", y="total_bill", hue="weekend",
            kind="box", dodge=False, data=tips)
```
![seaborn](../figures/seaborn-catplot-hue-dodge.png =250x)

A related function, `boxenplot()`, draws a plot that is similar to a box plot but optimized for showing more information about the shape of the distribution. It is best suited for larger datasets:
```python
diamonds = sns.load_dataset("diamonds")
sns.catplot(x="color", y="price", kind="boxen",
            data=diamonds.sort_values("color"))
```
![seaborn](../figures/seaborn-catplot-boxen.png =250x)

### Violin plots
A different approach is a `violinplot()`, which combines a boxplot with the kernel density estimation procedure.
![seaborn](../figures/seaborn-violinplot.png =250x)

It’s also possible to “split” the violins when the hue parameter has only two levels, which can allow for a more efficient use of space:
```python
sns.catplot(x="day", y="total_bill", hue="sex",
            kind="violin", split=True, data=tips);
```
![seaborn](../figures/seaborn-violinplot-split.png =250x)

Finally, there are several options for the plot that is drawn on the interior of the violins, including ways to show each individual observation instead of the summary boxplot values:

```python
sns.catplot(x="day", y="total_bill", kind="violin", inner="stick", palette="pastel", data=tips)
```
![seaborn](../figures/seaborn-violinplot-inner.png =250x)
inner can be:
- box
- quartile
- point
- stick
- None

It can also be useful to combine `swarmplot()` or `striplot()` with a box plot or violin plot to show each observation along with a summary of the distribution:

```python
g = sns.catplot(x="day", y="total_bill", kind="violin", inner=None, data=tips)
sns.swarmplot(x="day", y="total_bill", color="k", size=3, data=tips, ax=g.ax)
```
![seaborn](../figures/seaborn-violinplot-inner.png =250x)

## Statistical estimation within categories
For other applications, rather than showing the distribution within each category, you might want to show an estimate of the central tendency of the values.

### Bar Plot
```python
titanic = sns.load_dataset("titanic")
sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)
```
![seaborn](../figures/seaborn-barplot.png =250x)


A special case for the bar plot is when you want to show the number of observations in each category rather than computing a statistic for a second variable. This is similar to a histogram over a categorical, rather than quantitative, variable.

```python
sns.catplot(x="deck", kind="count", palette="ch:.25", data=titanic)
```
![seaborn](../figures/seaborn-countplot.png =250x)

Note: See sns color palettes [here](https://seaborn.pydata.org/tutorial/color_palettes.html).

**Error bars** can communicate the following information about your data:
- How spread the data are around the mean value (small SD bar = low spread, data are clumped around the mean; larger SD bar = larger spread, data are more variable from the mean).
- The reliability of the mean value as a representative number for the data set.  In other words, how accurately the mean value represents the data (small SD bar = more reliable, larger SD bar = less reliable). It's important to note that just because you have a larger SD, it does not indicate your data is not valid. Biological measurements are notoriously variable.
- The likelihood of there being a significant difference between between data sets.

### Point Plot
An alternative style for visualizing the same information is offered by the `pointplot()` function. This function also encodes the value of the estimate with height on the other axis, but rather than showing a full bar, it plots the point estimate and confidence interval. Additionally, `pointplot()` connects points from the same hue category. This makes it easy to see how the main relationship is changing as a function of the hue semantic, because **your eyes are quite good at picking up on differences of slopes**:

```python
sns.catplot(x="sex", y="survived", hue="class", kind="point", data=titanic)
```
![seaborn](../figures/seaborn-pointplot-class.png =250x)

```python
sns.catplot(x="class", y="survived", hue="sex", kind="point", data=titanic)
```
![seaborn](../figures/seaborn-pointplot-sex.png =250x)

When the categorical functions lack the style semantic of the relational functions, it can still be a good idea to vary the marker and/or linestyle along with the hue to make figures that are maximally accessible and reproduce well in black and white:

```python
sns.catplot(x="class", y="survived", hue="sex",
            palette={"male": "g", "female": "m"},
            markers=["^", "o"], linestyles=["-", "--"],
            kind="point", data=titanic)
```
![seaborn](../figures/seaborn-pointplot-black-white.png =250x)

### Showing multiple relationships with facets
Just like `relplot()`, the fact that `catplot()` is built on a `FacetGrid` means that it is easy to add faceting variables to visualize higher-dimensional relationships:

```python
g = sns.catplot(x="fare", y="survived", row="class",
                kind="box", orient="h", height=1.5, aspect=4,
                data=titanic.query("fare > 0"))
g.set(xscale="log")
```
![seaborn](../figures/seaborn-catplot-facetgrid.png =350x)