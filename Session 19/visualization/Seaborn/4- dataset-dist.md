# Seaborn
## Visualizing the distribution of a dataset
When dealing with a set of data, often the first thing you’ll want to do is get a sense for how the variables are distributed. This chapter of the tutorial will give a brief introduction to some of the tools in seaborn for examining univariate and bivariate distributions.

### Plotting univariate distributions
```python
x = np.random.normal(size=100)
sns.distplot(x)
```

#### Histograms
```python
sns.distplot(x, bins=20, kde=False, rug=True)
```

#### Kernel density estimation
The kernel density estimate may be less familiar, but it can be a useful tool for plotting the shape of a distribution. Like the histogram, the KDE plots encode the density of observations on one axis with height along the other axis.

Drawing a KDE is more computationally involved than drawing a histogram. What happens is that each observation is first replaced with a normal (Gaussian) curve centered at that value:
```python
from scipy import stats

x = np.random.normal(0, 1, size=30)
bandwidth = 1.06 * x.std() * x.size ** (-1 / 5.)
support = np.linspace(-4, 4, 200)

kernels = []
for x_i in x:

    kernel = stats.norm(x_i, bandwidth).pdf(support)
    kernels.append(kernel)
    plt.plot(support, kernel)

sns.rugplot(x, color=".2", linewidth=3)
```
![seaborn](../figures/seaborn-kde.png =250x)

Next, these curves are summed to compute the value of the density at each point in the support grid. The resulting curve is then normalized so that the area under it is equal to 1:
```python
from scipy.integrate import trapz
density = np.sum(kernels, axis=0)
density /= trapz(density, support)
plt.plot(support, density)
sns.kdeplot(x, shade=True)
```
![seaborn](../figures/seaborn-kde-estimation.png =250x)

The bandwidth (bw) parameter of the KDE controls how tightly the estimation is fit to the data, much like the bin size in a histogram. It corresponds to the width of the kernels we plotted above. The default behavior tries to guess a good value using a common reference rule, but it may be helpful to try larger or smaller values:

```python
sns.kdeplot(x, label="bw: default")
sns.kdeplot(x, bw=.2, label="bw: 0.2")
sns.kdeplot(x, bw=2, label="bw: 2")
plt.legend()
```
![seaborn](../figures/seaborn-kde-bandwidth.png =250x)

#### Fitting parametric distributions
You can also use `distplot()` to fit a parametric distribution to a dataset and visually evaluate how closely it corresponds to the observed data:
```python
x = np.random.gamma(6, size=200)
sns.distplot(x, kde=False, fit=stats.gamma)
sns.distplot(x, kde=False, hist=False, fit=stats.uniform)
sns.distplot(x, kde=False, hist=False, fit=stats.skewnorm)
```
![seaborn](../figures/seaborn-kde-fit-dist.png =250x)

### Plotting bivariate distributions
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
![seaborn](../figures/seaborn-jointplot-kde.png =250x)

```python
df = sns.load_dataset('tips')
sns.jointplot(x='total_bill', y='tip', data=df, kind='hex', height=5)
```
![seaborn](../figures/seaborn-jointplot-hex.png =250x)

You can also draw a two-dimensional kernel density plot with the `kdeplot()` function. This allows you to draw this kind of plot onto a specific (and possibly already existing) matplotlib axes, whereas the `jointplot()` function manages its own figure:

```python
f, ax = plt.subplots(figsize=(6, 6))
sns.kdeplot(df.x, df.y, ax=ax)
sns.rugplot(df.x, color="g", ax=ax)
sns.rugplot(df.y, vertical=True, ax=ax)
```
![seaborn](../figures/seaborn-kdeplot-bivariate.png =250x)

If you wish to show the bivariate density more continuously, you can simply increase the number of contour levels:
```python
f, ax = plt.subplots(figsize=(6, 6))
sns.kdeplot(df.total_bill, df.tip, ax=ax, shade=True, n_levels=30)
sns.rugplot(df.total_bill, color="g", ax=ax)
sns.rugplot(df.tip, vertical=True, ax=ax)
```
![seaborn](../figures/seaborn-kdeplot-bivariate-shade.png =250x)

The `jointplot()` function uses a `JointGrid` to manage the figure. For more flexibility, you may want to draw your figure by using `JointGrid` directly. `jointplot()` returns the `JointGrid` object after plotting, which you can use to add more layers or to tweak other aspects of the visualization:

```python
>>> g = sns.jointplot(x="total_bill", y="tip", data=tips, kind="kde")
>>> g.plot_joint(plt.scatter, c="w", s=30, linewidth=1, marker="+")
>>> g.ax_joint.collections[0].set_alpha(0)
>>> g.set_axis_labels("$X$", "$Y$")
```
![seaborn](../figures/seaborn-jointplot-jointgrid.png =250x)

### Visualizing pairwise relationships in a dataset
```python
iris = sns.load_dataset("iris")
sns.pairplot(iris)
```
![seaborn](../figures/seaborn-pairplot.png =500x)

Much like the relationship between `jointplot()` and `JointGrid`, the `pairplot()` function is built on top of a PairGrid object, which can be used directly for more flexibility:
```python
g = sns.PairGrid(iris)
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.kdeplot, n_levels=6)
```
![seaborn](../figures/seaborn-pairgrid.png =500x)