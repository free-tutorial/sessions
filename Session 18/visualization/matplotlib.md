# Matplotlib

In essence, there are two big components that you need to take into account:
- The Figure is the overall window or page that everything is drawn on. It’s the top-level component of all the ones that you will consider in the following points. You can create multiple independent Figures. A Figure can have several other things in it, such as a suptitle, which is a centered title to the figure. You’ll also find that you can add a legend and color bar, for example, to your Figure.
- To the figure you add Axes. The Axes is the area on which the data is plotted with functions such as plot() and scatter() and that can have ticks, labels, etc. associated with it. This explains why Figures can contain multiple Axes.

Tip: when you see, for example, `plt.xlim`, you’ll call `ax.set_xlim()` behind the covers. All methods of an Axes object exist as a function in the pyplot module and vice versa. Note that mostly, you’ll use the functions of the pyplot module because they’re much cleaner, at least for simple plots!

You’ll see what “clean” means when you take a look at the following pieces of code. Compare, for example, this piece of code:

```python
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
ax.set_xlim(0.5, 4.5)
plt.show()
```

with this one:
```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
plt.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
plt.xlim(0.5, 4.5)
plt.show()
```

First off, you’ll already know Matplotlib by now. When you talk about “Matplotlib”, you talk about the whole Python data visualization package. This should not come to you as a big surprise :)

Secondly, pyplot is a module in the matplotlib package. That’s why you often see matplotlib.pyplot in code. The module provides an interface that allows you to implicitly and automatically create figures and axes to achieve the desired plot.

This is especially handy when you want to quickly plot something without instantiating any Figures or Axes, as you saw in the example in the first section of this tutorial. You see, you haven’t explicitly specified these components, yet you manage to output a plot that you have even customized! The defaults are initialized and any customizations that you do, will be done with the current Figure and Axes in mind.

## Create Your Plot
Alright, you’re off to create your first plot yourself with Python! As you have read in one of the previous sections, the Figure is the first step and the key to unlocking the power of this package. Next, you see that you initialize the axes of the Figure in the code chunk above with `fig.add_axes()`


```python
# Import `pyplot`
import matplotlib.pyplot as plt

# Initialize a Figure 
fig = plt.figure()

# Add Axes to the Figure
fig.add_axes([0,0,1,1])
```

What Is A Subplot?
You have seen all components of a plot and you have initialized your first figure and Axes, but to make things a bit more complicated, you’ll sometimes see subplots pop up in code.

Now, don’t get discouraged just yet!

You use subplots to set up and place your Axes on a regular grid. So that means that in most cases, Axes and subplot are synonymous, they will designate the same thing. When you do call subplot to add Axes to your figure, do so with the `add_subplots()` function. There is, however, a difference between the `add_axes()` and the `add_subplots()` function, but you’ll learn more about this later on in the tutorial.

Consider the following example:

```python
# Import the necessary packages and modules
import matplotlib.pyplot as plt
import numpy as np

# Create a Figure
fig = plt.figure()

# Set up Axes
ax = fig.add_subplot(111)

# Scatter the data
ax.scatter(np.linspace(0, 1, 5), np.linspace(0, 5, 5))

# Show the plot
plt.show()
```

You see that the `add_subplot()` function in itsef also poses you with a challenge, because you see `add_subplots(111)` in the above code chunk.

What does `111` mean?

Well, `111` is equal to `1,1,1`, which means that you actually give three arguments to add_subplot(). The three arguments designate the number of rows (1), the number of columns (1) and the plot number (1). So you actually make one subplot.

Consider the following commands and try to envision what the plot will look like and how many Axes your Figure will have: `ax = fig.add_subplot(2,2,1)`.

Got it?

That’s right, your Figure will have four axes in total, arranged in a structure that has two rows and two columns. With the line of code that you have considered, you say that the variable ax is the first of the four axes to which you want to start plotting. The “first” in this case means that it will be the first axes on the left of the 2x2 structure that you have initialized.

## What Is The Difference Between add_axes() and add_subplot()?

The difference between `fig.add_axes()` and `fig.add_subplot()` doesn’t lie in the result: they both return an Axes object. However, they do differ in the mechanism that is used to add the axes: you pass a list to `add_axes()` which is the lower left point, the width and the height. This means that the axes object is positioned in absolute coordinates.

In contrast, the `add_subplot()` function doesn’t provide the option to put the axes at a certain position: it does, however, allow the axes to be situated according to a subplot grid, as you have seen in the section above.

In most cases, you’ll use `add_subplot()` to create axes; Only in cases where the positioning matters, you’ll resort to `add_axes()`. Alternatively, you can also use `subplots()` if you want to get one or more subplots at the same time. You’ll see an example of how this works in the next section.


## Change The Size of Figures

```python
# Import `pyplot` from `matplotlib`
import matplotlib.pyplot as plt

# Initialize the plot
fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# or replace the three lines of code above by the following line:
#fig, (ax1, ax2) = plt.subplots(1,2, figsize=(20,10))

# Plot the data
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])

# Show the plot
plt.show()
```

## Basic Plots
```python
>>> import matplotlib.pyplot as plt
>>> y = [1, 2, 8, -2, 5]
>>> x = [1, 2, 3, 4, 5]
>>> plt.plot(x, y, '--')
>>> plt.xlabel('X label')
>>> plt.ylabel('Y label')
>>> plt.title('title')
>>> plt.show()  # shows the plot
>>> plt.show()  # does nothing as plot is reset!
# or ax.set(title="title", xlabel="X label", ylabel="Y label")
# or ax.set_xlim("X label"), ax.set_ylim("Y label") or ax.set_title("title").
```
Note: For a list of line markers see [matplotlib.pyplot.plot](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html)


```python
# Initialize a Figure 
fig, ax = plt.subplots(1, 1, figsize=(10,10))
# Add Axes to the Figure

ax.plot(
    range(10),                  # x
    range(10),                  # y
    'c^:',                      # color, marker, linestyle
    c='#000088',                # or color
    linestyle=':',
    marker='^',

    linewidth=3,
    alpha=1,                    # used for blending

    drawstyle='steps',          # or ds: 'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'
    fillstyle='full',           # 'full', 'left', 'right', 'bottom', 'top', 'none'

    label='label for legend',

    markerfacecolor='b',
    markeredgecolor='r',
    markeredgewidth=5,
    markersize=20,
    markevery=2,
    visible=True,
)

ax.set(xlabel='x', ylabel='y', title='title');
ax.legend(loc='best')
```


Setting ax legend location:
```python
fig, axes = plt.subplots(2, 2, figsize=(5, 5))
axes[0, 0].scatter(np.random.rand(20), np.random.rand(20), label='first')
axes[0, 1].scatter(np.random.rand(20), np.random.rand(20), c='r')
axes[0, 0].legend(loc='best')
```

|Location String|Location Code|
|--|--|
|'best'|0|
|'upper right'|1|
|'upper left'|2|
|'lower left'|3|
|'lower right'|4|
|'right'|5|
|'center left'|6|
|'center right' |7|
|'lower center'|8|
|'upper center'|9|
|'center'|10|


```python
>>> y2 = [1, 2, 3, 4, 5]
>>> plt.plot(x, y, label='first plot')
>>> plt.plot(x, y2, label='second plot')
>>> plt.legend()
>>> plt.xlabel('X label')
>>> plt.ylabel('Y label')
>>> plt.title('first plot')
>>> plt.yscale('linear')  # can be {"linear", "log", "symlog", "logit", ...}
>>> plt.show()  # shows the plot
>>> plt.show()  # does nothing as plot is reset!
```

Setting attributes with `ax`:
```python
fig, axes = plt.subplots(2, 2, figsize=(5, 5))
axes[0, 0].scatter(np.random.rand(20), np.random.rand(20), label='first')
axes[0, 1].scatter(np.random.rand(20), np.random.rand(20), c='r')
axes[0, 0].legend(loc='best')
axes[0, 0].set(xticks=[0, 0.5, 1], xticklabels=['0', '0.5', '1'], ylim=(0, 2), xlim=(0, 3))
```

## Bar Plot

### Vertical Bar Plot
Use vertical column charts when you’re graphing ordinal variables.
```python
>>> x = range(5)
>>> y = [3, 5, -2, -8, 11]
>>> plt.bar(x, y, color='r')
>>> plt.show()
```
![bar plot](figures/matplotlib-bar.png =300x)

### Horizontal Bar Plot
Use horizontal bar charts when you’re graphing nominal variables or when plotting wide-form data

```python
>>> plt.barh(['name_1', 'name_2', 'name_3', 'name_4', 'name_5'], [26, 14, 39, 20, 15], color='g')
>>> plt.show()
```
![bar plot](figures/matplotlib-barh.png =300x)

### Bar Plot with Error Bars

```python
>>> x, y, z = (np.random.randint(0, 15, 100), np.random.randint(15, 20, 100), np.random.randint(0, 5, 100))
>>> plt.bar(['Ali', 'Reza', 'Hasan'], [np.mean(x), np.mean(y), np.mean(z)], yerr=[np.std(x), np.std(y), np.std(z)], ecolor='k', capsize=5)
```
![bar plot](figures/matplotlib-barplot-errorbars.png =300x)

## Histogram

```python
>>> scores = [3, 2, 0, 10, 10, 10, 10, 11, 11, 11, 12, 12, 13, 14, 14, 15, 15, 15, 15, 15.5, 15.7, 16, 16, 16, 16.5, 17, 17, 17, 17, 18, 18, 18, 19, 19, 19.75, 20]
>>> plt.hist(scores, cumulative=True, rwidth=0.9, histtype='bar')
```

```python
# create 3 data sets with 1,000 samples
>>> mu, sigma = 200, 25
>>> x = mu + sigma*np.random.randn(1000,3)
#Stack the data
>>> plt.figure()
>>> n, bins, patches = plt.hist(x, 20, stacked=True, normed = True)
>>> plt.show()
```

`histtype`:
- 'bar'
- 'barstacked'
- 'step'
- 'stepfilled'

## Stack Plot

```python
>>> taxes = [17, 18, 40, 43, 44, 8, 43, 32, 39, 30]
>>> overhead = [30, 22, 9, 29, 17, 12, 14, 24, 49, 35]
>>> entertainment = [41, 32, 27, 13, 19, 12, 22, 28, 28, 20]
>>> plt.stackplot(range(10), taxes, overhead, entertainment, labels=['taxes', 'overhead', 'entertainment'], colors=['m','c','b'])
>>> plt.legend()
```
## Scatter Plot

```python
>>> x = [1,2,3,4,5]
>>> y1 = [-1, 2, 8, 2, 3]
>>> y2 = [8, 8, 6, 5, 4]
>>> plt.scatter(x, y1, marker='o', color='c')
>>> plt.scatter(x, y2, marker='v', color='m')
```

for a list of merkers, see [matplotlib.markers](https://matplotlib.org/3.1.1/api/markers_api.html#module-matplotlib.markers)

```python
>>> df = pd.read_csv('iris.csv')
>>> cmap = {'setosa': 'g', 'versicolor': 'b', 'virginica': 'r'}
>>> plt.scatter(df.sepal_length, df.sepal_width, c=df.species.apply(lambda x: cmap[x]))
```

If you want to have the size of scatter dots as another variable:
```python
for x, y in zip(np.random.rand(100), np.random.rand(100)):
    plt.scatter(x, y, s=(x+y)*100)
```
![matplotlib-scatter-s](./figures/matplotlib-scatter-s.png =250x)

## Hexbin Plot
Hexbin plots can be a useful alternative to scatter plots if your data are too dense to plot each point individually.

```python
>>> plt.hexbin(np.random.rand(100).cumsum(), np.random.rand(100).cumsum(), gridsize=20, cmap='Blues')
```
![plot](./figures/matplotlib-hexbin.png =250x)

## Pie Chart

```python
>>> sizes = [25, 32, 12]
>>> colors = ['c', 'm', 'b']
>>> plt.pie(sizes, labels = ['taxes', 'overhead', 'entertainment'], startangle=90, autopct='%.2f%%', explode=(0, 0.1, 0))
```

```python
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v})'.format(p=pct,v=val)
    return my_autopct

>>> sizes = [25, 32, 12]
>>> colors = ['c', 'm', 'b']
>>> plt.pie(sizes, labels = ['taxes', 'overhead', 'entertainment'], startangle=90, autopct=make_autopct(sizes))
```

## Reference
- https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python