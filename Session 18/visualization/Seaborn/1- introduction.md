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

## Controlling the size and shape of the plot
“axes-level” function draws onto a specific axes. This means that you can make multi-panel figures yourself and control exactly where the regression plot goes. If no axes object is explicitly provided, it simply uses the “currently active” axes, which is why the default plot has the same size and shape as most other matplotlib functions. To control the size, you need to create a figure object yourself.

```python
>>> tips = sns.load_dataset('tips')
>>> f, ax = plt.subplots(figsize=(5, 6))
>>> sns.regplot(x="total_bill", y="tip", data=tips, ax=ax)
```
![figsize](../figures/seaborn-figsize-axeslevel.png =250x)

In contrast, the size and shape of the figure level plots such as `lmplot()` is controlled through the `FacetGrid` interface using the size and aspect parameters, which apply to each facet in the plot, not to the overall figure itself:

```python
sns.lmplot(x="total_bill", y="tip", col="day", data=tips, col_wrap=2, height=3)
```
![figsize](../figures/seaborn-figsize-figurelevel.png =400x)