# Seaborn
Seaborn is complimentary to Matplotlib and it specifically targets statistical data visualization. But it goes even further than that: Seaborn extends Matplotlib and that’s why it can address the two biggest frustrations of working with Matplotlib. Or, as Michael Waskom says in the “introduction to Seaborn”: “If matplotlib “tries to make easy things easy and hard things possible”, seaborn tries to make a well-defined set of hard things easy too.”

## Load dataset
```python
>>> sns.get_dataset_names()
['anscombe',
 'attention',
 'brain_networks',
 'car_crashes',
 'diamonds',
 'dots',
 'exercise',
 'flights',
 'fmri',
 'gammas',
 'iris',
 'mpg',
 'planets',
 'tips',
 'titanic']
>>> df = sns.load_dataset('iris')
```

## Plotting
As for Seaborn, you have two types of functions: axes-level functions and figure-level functions. The ones that operate on the Axes level are, for example, `regplot()`, `boxplot()`, `kdeplot()`, …, while the functions that operate on the Figure level are `lmplot()`, `factorplot()`, `jointplot()` and a couple others.

This means that the first group is identified by taking an explicit ax argument and returning an Axes object, while the second group of functions create plots that potentially include Axes which are always organized in a “meaningful” way. The Figure-level functions will therefore need to have total control over the figure so you won’t be able to plot an lmplot onto one that already exists. When you call the Figure-level functions, you always initialize a figure and set it up for the specific plot it’s drawing.

When you’re customizing your plots, this means that you will prefer to make customizations to your regression plot that you constructed with `regplot()` on Axes level, while you will make customizations for `lmplot()` on Figure level.

### Visualizing statistical relationships with `relplot` (Figure Level)
#### Relating variables with scatter plots

Seaborn have a dedicated scatter plot function, but it can also be achieved by `relplot`.

```python
sns.set_style('whitegrid')
tips = sns.load_dataset('tips')
sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker", data=tips)
```
![seaborn](figures/sns-relplot-hue-style.png =300x)

```python
sns.set_style('whitegrid')
tips = sns.load_dataset('tips')
sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker", size='size', col='time', row='sex', data=tips)
```
![seaborn](figures/sns-relplot-hue-style-row-column.png =300x)

In the examples above, the hue semantic was categorical, so the default qualitative palette was applied. If the hue semantic is numeric (specifically, if it can be cast to float), the default coloring switches to a sequential palette:

```python
sns.relplot(x="total_bill", y="tip", hue="size", data=tips)
```
![seaborn](figures/sns-relplot-hue-sequential.png =300x)

Unlike with `matplotlib.pyplot.scatter()`, the literal value of the variable is not used to pick the area of the point. Instead, the range of values in data units is normalized into a range in area units. This range can be customized:

```python
sns.relplot(x="total_bill", y="tip", hue="size", data=tips, palette='Blues', size='size', sizes=(0, 300))
```
![seaborn](figures/sns-relplot-hue-sizes.png =300x)

Note: all of this can be achieved by `scatterplot`.
```python
sns.scatterplot(x="total_bill", y="tip", hue="size", data=tips, palette='Blues', size='size', sizes=(0, 300))
```
![seaborn](figures/sns-scatterplot-hue-sizes.png =300x)

#### Emphasizing continuity with line plots
Scatter plots are highly effective, but there is no universally optimal type of visualiation. Instead, the visual representation should be adapted for the specifics of the dataset and to the question you are trying to answer with the plot.

With some datasets, you may want to understand changes in one variable as a function of time, or a similarly continuous variable. In this situation, a good choice is to draw a line plot. In seaborn, this can be accomplished by the `lineplot()` function, either directly or with `relplot()` by setting kind="line":

```python
df = pd.DataFrame(dict(time=np.arange(500),
                       value=np.random.randn(500).cumsum()))
g = sns.relplot(x="time", y="value", kind="line", data=df)
```

#### Aggregation and representing uncertainty
More complex datasets will have multiple measurements for the same value of the x variable. The default behavior in seaborn is to aggregate the multiple measurements at each x value by plotting the mean and the 95% confidence interval around the mean:
```python
fmri = sns.load_dataset("fmri")
sns.relplot(x="timepoint", y="signal", kind="line", data=fmri)
```
![seaborn](figures/seaborn-relplot-confidence-interval.png =250x)

The confidence intervals are computed using bootstrapping, which can be time-intensive for larger datasets. It’s therefore possible to disable them:

```python
sns.relplot(x="timepoint", y="signal", ci=None, kind="line", data=fmri)
```
![seaborn](figures/seaborn-relplot-no-confidence-interval.png =250x)

Adding a style semantic to a line plot changes the pattern of dashes in the line by default:
```python
sns.relplot(x="timepoint", y="signal", hue="region", style="event", dashes=False, markers=True, kind="line", data=fmri)
```
![seaborn](figures/seaborn-relplot-hue-style.png =250x)

The default colormap and handling of the legend in `lineplot()` also depends on whether the hue semantic is categorical or numeric:

```python
palette = sns.cubehelix_palette(light=.8, n_colors=6)
sns.relplot(x="time", y="firing_rate",
            hue="coherence", style="choice",
            palette=palette,
            kind="line", data=dots)
```
![seaborn](figures/seaborn-relplot-hue-style-palette.png =400x)

It is possible to map a categorical variable with the width of the lines. Be cautious when doing so, because it will be difficult to distinguish much more than “thick” vs “thin” lines. However, dashes can be hard to perceive when lines have high-frequency variability, so using different widths may be more effective in that case:
![seaborn](figures/seaborn-hue-size.png =400x)

#### Plotting with date data
Line plots are often used to visualize data associated with real dates and times. These functions pass the data down in their original format to the underlying matplotlib functions, and so they can take advantage of matplotlib’s ability to format dates in tick labels. But all of that formatting will have to take place at the matplotlib layer, and you should refer to the matplotlib documentation to see how it works:

```python
>>> df = pd.DataFrame(dict(time=pd.date_range("2017-1-1", periods=500), value=np.random.randn(500).cumsum()))
>>> g = sns.relplot(x="time", y="value", kind="line", data=df)
>>> g.fig.autofmt_xdate(rotation=30)
```
![seaborn](figures/seaborn-date.png =250x)


#### Showing multiple relationships with facets
We’ve emphasized in this tutorial that, while these functions can show several semantic variables at once, it’s not always effective to do so. But what about when you do want to understand how a relationship between two variables depends on more than one other variable?

The best approach may be to make more than one plot. Because `relplot()` is based on the `FacetGrid`, this is easy to do. To show the influence of an additional variable, instead of assigning it to one of the semantic roles in the plot, use it to “facet” the visualization. This means that you make multiple axes and plot subsets of the data on each of them:

```python
sns.relplot(x="timepoint", y="signal", hue="subject",
            col="region", row="event", height=3,
            kind="line", data=fmri)
```
![seaborn](figures/seaborn-relplot-facetgrid.png =400x)

When you want to examine effects across many levels of a variable, it can be a good idea to facet that variable on the columns and then “wrap” the facets into the rows:

```python
sns.relplot(x="timepoint", y="signal", hue="event", style="event", col="subject", col_wrap=4, height=3, aspect=.75, linewidth=2.5, kind="line", data=fmri.query("region == 'frontal'"))
```
![seaborn](figures/seaborn-relplot-facetgrid-colwrap.png =400x)

These visualizations, which are often called “lattice” plots or “small-multiples”, are very effective because they present the data in a format that makes it easy for the eye to detect both overall patterns and deviations from those patterns. While you should make use of the flexiblity afforded by scatterplot() and relplot(), **always try to keep in mind that several simple plots are usually more effective than one complex plot**.

### Plotting with categorical data with `catplot` (figure level)
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

#### Categorical Scatterplot
There are actually two different categorical scatter plots in seaborn. The approach used by `stripplot()`, which is the default “kind” in `catplot()` is to adjust the positions of points on the categorical axis with a small amount of random “jitter”:

```python
tips = sns.load_dataset("tips")
sns.catplot(x="day", y="total_bill", data=tips)
```
![seaborn](figures/seaborn-catplot-jitter.png =250x)

The jitter parameter controls the magnitude of jitter or disables it altogether:

```python
tips = sns.load_dataset("tips")
sns.catplot(x="day", y="total_bill", jitter=False, data=tips)
```
![seaborn](figures/seaborn-catplot-nojitter.png =250x)

The second approach adjusts the points along the categorical axis using an algorithm that prevents them from overlapping. It can give a better representation of the distribution of observations, although it only works well for relatively small datasets.

```python
sns.catplot(x="day", y="total_bill", kind="swarm", data=tips)
```
![seaborn](figures/seaborn-catplot-swarm.png =250x)

```python
sns.catplot(x="day", y="total_bill", kind="swarm", data=tips, hue='time')
```
![seaborn](figures/seaborn-catplot-swarm-hue.png =250x)

Unlike with numerical data, it is not always obvious how to order the levels of the categorical variable along its axis. In general, the seaborn categorical plotting functions try to infer the order of categories from the data.

The ordering can also be controlled on a plot-specific basis using the `order` parameter. This can be important when drawing multiple categorical plots in the same figure, which we’ll see more of below:

```python
sns.catplot(x="smoker", y="tip", order=["No", "Yes"], data=tips)
```
![seaborn](figures/seaborn-catplot-order.png =250x)

### Distributions of observations within categories
As the size of the dataset grows,, categorical scatter plots become limited in the information they can provide about the distribution of values within each category. When this happens, there are several approaches for summarizing the distributional information in ways that facilitate easy comparisons across the category levels.

#### Box plots
This kind of plot shows the three quartile values of the distribution along with extreme values.

```python
sns.catplot(x="day", y="total_bill", kind="box", data=tips)
```
![seaborn](figures/seaborn-boxplot.png =250x)

When adding a hue semantic, the box for each level of the semantic variable is moved along the categorical axis so they don’t overlap:
```python
sns.catplot(x="day", y="total_bill", hue="smoker", kind="box", data=tips)
```
![seaborn](figures/seaborn-catplot-hue.png =250x)

This behavior is called “dodging” and is turned on by default because it is assumed that the semantic variable is nested within the main categorical variable. If that’s not the case, you can disable the dodging:

```python
tips["weekend"] = tips["day"].isin(["Sat", "Sun"])
sns.catplot(x="day", y="total_bill", hue="weekend",
            kind="box", dodge=False, data=tips)
```
![seaborn](figures/seaborn-catplot-hue-dodge.png =250x)

A related function, `boxenplot()`, draws a plot that is similar to a box plot but optimized for showing more information about the shape of the distribution. It is best suited for larger datasets:
![seaborn](figures/seaborn-catplot-boxen.png =250x)

#### Violin plots
A different approach is a `violinplot()`, which combines a boxplot with the kernel density estimation procedure.











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