# Seaborn

## Visualizing linear relationships
### Simple Linear Regression
Two main functions in seaborn are used to visualize a linear relationship as determined through regression. These functions, `regplot()` and `lmplot()` are closely related, and share much of their core functionality. It is important to understand the ways they differ, however, so that you can quickly choose the correct tool for particular job.

In the simplest invocation, both functions draw a scatterplot of two variables, `x` and `y`, and then fit the regression model `y ~ x` and plot the resulting regression line and a 95% confidence interval for that regression:

```python
sns.regplot(x="total_bill", y="tip", data=tips)
```
![regplot](../figures/seaborn-regplot.png =250x)

```python
sns.lmplot(x="total_bill", y="tip", data=tips)
```
![lmplot](../figures/seaborn-lmplot.png =250x)

You should note that the resulting plots are identical, except that the figure shapes are different. We will explain why this is shortly. For now, the other main difference to know about is that `regplot()` accepts the `x` and `y` variables in a variety of formats including simple numpy arrays, pandas `Series` objects, or as references to variables in a pandas `DataFrame` object passed to data. In contrast, `lmplot()` has data as a required parameter and the `x` and `y` variables must be specified as strings. This data format is called “long-form” or “tidy” data. Other than this input flexibility, `regplot()` possesses a subset of `lmplot()`’s features, so we will demonstrate them using the latter.

It’s possible to fit a linear regression when one of the variables takes discrete values, however, the simple scatterplot produced by this kind of dataset is often not optimal:

```python
sns.lmplot(x="size", y="tip", data=tips)
```
![lmplot](../figures/seaborn-lmplot-categorical.png =250x)

One option is to add some random noise (“jitter”) to the discrete values to make the distribution of those values more clear. Note that jitter is applied only to the scatterplot data and does not influence the regression line fit itself:

```python
sns.lmplot(x="size", y="tip", data=tips, x_jitter=.05)
```
![lmplot](../figures/seaborn-lmplot-jitter.png =250x)

A second option is to collapse over the observations in each discrete bin to plot an estimate of central tendency along with a confidence interval:

```python
sns.lmplot(x="size", y="tip", data=tips, x_estimator=np.mean)
```
![lmplot](../figures/seaborn-lmplot-central-tendency.png =250x)

### Fitting different kinds of models

In the presence of these kind of higher-order relationships, lmplot() and regplot() can fit a polynomial regression model to explore simple kinds of nonlinear trends in the dataset:
```python
>>> anscombe = sns.load_dataset("anscombe")
>>> sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"), ci=None, scatter_kws={"s": 80})
```
![lmplot](../figures/seaborn-lmplot-linear.png =250x)

```python
>>> sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"), order=2, ci=None, scatter_kws={"s": 80})
```
![lmplot](../figures/seaborn-lmplot-linear-order.png =250x)

A different problem is posed by “outlier” observations that deviate for some reason other than the main relationship under study:

```python
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"), ci=None, scatter_kws={"s": 80})
```
![lmplot](../figures/seaborn-lmplot-outlier.png =250x)

```python
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"), robust=True, ci=None, scatter_kws={"s": 80})
```
![lmplot](../figures/seaborn-lmplot-outlier-robust.png =250x)


### `residplot`
The `residplot()` function can be a useful tool for checking whether the simple regression model is appropriate for a dataset. It fits and removes a simple linear regression and then plots the residual values for each observation. Ideally, these values should be randomly scattered around `y = 0`:

```python
sns.residplot(x="x", y="y", data=anscombe.query("dataset == 'I'"), scatter_kws={"s": 80})
```
![residplot](../figures/seaborn-residplot-random.png =250x)

If there is structure in the residuals, it suggests that simple linear regression is not appropriate:
```python
sns.residplot(x="x", y="y", data=anscombe.query("dataset == 'II'"), scatter_kws={"s": 80})
```
![residplot](../figures/seaborn-residplot-structure.png =250x)

### Conditioning on other variables
```python
sns.lmplot(x="total_bill", y="tip", hue="smoker", col="time", row="sex", data=tips, palette='husl')
```
![lmplot](../figures/seaborn-lmplot-facetgrid.png =400x)

### Plotting a regression in other contexts
A few other seaborn functions use `regplot()` in the context of a larger, more complex plot. The first is the `jointplot()` function that we introduced in the distributions tutorial. In addition to the plot styles previously discussed, `jointplot()` can use `regplot()` to show the linear regression fit on the joint axes by passing `kind="reg"`:

```python
sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
```
![jointplot](../figures/seaborn-jointplot-regplot.png =250x)

Like `lmplot()`, but unlike `jointplot()`, conditioning on an additional categorical variable is built into `pairplot()` using the hue parameter:
```python
sns.pairplot(tips, x_vars=["total_bill", "size"], y_vars=["tip"], hue="smoker", height=5, aspect=.8, kind="reg")
```
![jointplot](../figures/seaborn-pairplot-regplot.png =400x)

```python
>>> g = sns.PairGrid(tips, x_vars=["total_bill", "size"], y_vars=["tip"], hue='smoker', palette='husl', height=5, aspect=0.7)
>>> g.map(sns.regplot, order=2, scatter_kws={'s': 10})
>>> g.add_legend()
```
![jointplot](../figures/seaborn-pairgrid-regplot.png =400x)