# Seaborn
## Visualizing statistical relationships with `relplot` (Figure Level)
### Relating variables with scatter plots

Seaborn have a dedicated scatter plot function, but it can also be achieved by `relplot`.

```python
sns.set_style('whitegrid')
tips = sns.load_dataset('tips')
sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker", data=tips)
```
![seaborn](../figures/sns-relplot-hue-style.png =300x)

Semantic Levels:
- hue
- style
- size

```python
sns.set_style('whitegrid')
tips = sns.load_dataset('tips')
sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker", size='size', col='time', row='sex', data=tips)
```
![seaborn](../figures/sns-relplot-hue-style-row-column.png =300x)

In the examples above, the hue semantic was categorical, so the default qualitative palette was applied. If the hue semantic is numeric (specifically, if it can be cast to float), the default coloring switches to a sequential palette:

```python
sns.relplot(x="total_bill", y="tip", hue="size", data=tips)
```
![seaborn](../figures/sns-relplot-hue-sequential.png =300x)

Unlike with `matplotlib.pyplot.scatter()`, the literal value of the variable is not used to pick the area of the point. Instead, the range of values in data units is normalized into a range in area units. This range can be customized:

```python
sns.relplot(x="total_bill", y="tip", hue="size", data=tips, palette='Blues', size='size', sizes=(0, 300))
```
![seaborn](../figures/sns-relplot-hue-sizes.png =300x)

Note: all of this can be achieved by `scatterplot`.
```python
sns.scatterplot(x="total_bill", y="tip", hue="size", data=tips, palette='Blues', size='size', sizes=(0, 300))
```
![seaborn](../figures/sns-scatterplot-hue-sizes.png =300x)

### Emphasizing continuity with line plots
Scatter plots are highly effective, but there is no universally optimal type of visualiation. Instead, the visual representation should be adapted for the specifics of the dataset and to the question you are trying to answer with the plot.

With some datasets, you may want to understand changes in one variable as a function of time, or a similarly continuous variable. In this situation, a good choice is to draw a line plot. In seaborn, this can be accomplished by the `lineplot()` function, either directly or with `relplot()` by setting kind="line":

```python
df = pd.DataFrame(dict(time=np.arange(500), value=np.random.randn(500).cumsum()))
g = sns.relplot(x="time", y="value", kind="line", data=df)
```

### Aggregation and representing uncertainty
More complex datasets will have multiple measurements for the same value of the x variable. The default behavior in seaborn is to aggregate the multiple measurements at each x value by plotting the mean and the 95% confidence interval around the mean:
```python
fmri = sns.load_dataset("fmri")
sns.relplot(x="timepoint", y="signal", kind="line", data=fmri)
```
![seaborn](../figures/seaborn-relplot-confidence-interval.png =250x)

The confidence intervals are computed using bootstrapping, which can be time-intensive for larger datasets. It’s therefore possible to disable them:

```python
sns.relplot(x="timepoint", y="signal", ci=None, kind="line", data=fmri)
```
![seaborn](../figures/seaborn-relplot-no-confidence-interval.png =250x)

Adding a style semantic to a line plot changes the pattern of dashes in the line by default:
```python
sns.relplot(x="timepoint", y="signal", hue="region", style="event", dashes=False, markers=True, kind="line", data=fmri)
```
![seaborn](../figures/seaborn-relplot-hue-style.png =250x)

The default colormap and handling of the legend in `lineplot()` also depends on whether the hue semantic is categorical or numeric:


```python
>>> dots = sns.load_dataset("dots").query("align == 'dots'")
>>> palette = sns.cubehelix_palette(light=.8, n_colors=6)
>>> sns.relplot(x="time", y="firing_rate",
            hue="coherence", style="choice",
            palette=palette,
            kind="line", data=dots)
```
![seaborn](../figures/seaborn-relplot-hue-style-palette.png =400x)

It is possible to map a categorical variable with the width of the lines. Be cautious when doing so, because it will be difficult to distinguish much more than “thick” vs “thin” lines. However, dashes can be hard to perceive when lines have high-frequency variability, so using different widths may be more effective in that case:
```python
sns.relplot(x="time", y="firing_rate",
           hue="coherence", size="choice",
           palette=palette,
           kind="line", data=dots)
```
![seaborn](../figures/seaborn-hue-size.png =400x)

### Plotting with date data
Line plots are often used to visualize data associated with real dates and times. These functions pass the data down in their original format to the underlying matplotlib functions, and so they can take advantage of matplotlib’s ability to format dates in tick labels. But all of that formatting will have to take place at the matplotlib layer, and you should refer to the matplotlib documentation to see how it works:

```python
>>> df = pd.DataFrame(dict(time=pd.date_range("2017-1-1", periods=500), value=np.random.randn(500).cumsum()))
>>> g = sns.relplot(x="time", y="value", kind="line", data=df)
>>> g.fig.autofmt_xdate(rotation=30)
```
![seaborn](../figures/seaborn-date.png =250x)


### Showing multiple relationships with facets
We’ve emphasized in this tutorial that, while these functions can show several semantic variables at once, it’s not always effective to do so. But what about when you do want to understand how a relationship between two variables depends on more than one other variable?

The best approach may be to make more than one plot. Because `relplot()` is based on the `FacetGrid`, this is easy to do. To show the influence of an additional variable, instead of assigning it to one of the semantic roles in the plot, use it to “facet” the visualization. This means that you make multiple axes and plot subsets of the data on each of them:

```python
sns.relplot(x="timepoint", y="signal", hue="subject",
            col="region", row="event", height=3,
            hue='subject', estimator=None,
            kind="line", data=fmri)
```
![seaborn](../figures/seaborn-relplot-facetgrid.png =400x)

When you want to examine effects across many levels of a variable, it can be a good idea to facet that variable on the columns and then “wrap” the facets into the rows:

```python
sns.set(style='white', font_scale=1.5)
sns.relplot(x="timepoint", y="signal", hue="event", style="event", col="subject", col_wrap=4, height=3, aspect=.75, linewidth=2.5, kind="line", data=fmri.query("region == 'frontal'"))
```
![seaborn](../figures/seaborn-relplot-facetgrid-colwrap.png =400x)

These visualizations, which are often called “lattice” plots or “small-multiples”, are very effective because they present the data in a format that makes it easy for the eye to detect both overall patterns and deviations from those patterns. While you should make use of the flexiblity afforded by scatterplot() and relplot(), **always try to keep in mind that several simple plots are usually more effective than one complex plot**.