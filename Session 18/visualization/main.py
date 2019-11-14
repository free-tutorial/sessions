import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('iris.csv')
cmap = {'setosa': 'g', 'versicolor': 'b', 'virginica': 'r'}
mmap = {'setosa': 'v', 'versicolor': 'o', 'virginica': 'x'}

fig = plt.figure()
ax = fig.add_subplot(111)
for label in df.species.unique():
    df_t = df[df.species == 'setosa']
    ax.scatter(df_t.sepal_length, df_t.sepal_width, c=df_t.species.apply(lambda x: cmap[x]), marker='v');

plt.show()