import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from randomlist import list_num as rl
'''
sns.set_theme(style='darkgrid')
'catter'
sns.scatterplot(data=[1,2,3,4,5,6])

'linee'
sns.lineplot(data=rl(lung=5, minimo=1, massimo=10), color='red')
'bars'
sns.barplot(data=rl(lung=5, minimo=1, massimo=50), estimator='mean')
'histogram'
sns.histplot(data=rl(lung=5))
'box'
df = sns.load_dataset('tips')
sns.boxplot(df)
'violin'
sns.violinplot(data=df, x="day", y="total_bill", hue="sex", split=True)

df = sns.load_dataset('iris')
corr = df.drop(columns='species').corr()

sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")

df = sns.load_dataset("iris")
sns.pairplot(df, hue="species", diag_kind="kde")
'''

plt.title("TITOLO DEL GRAFICO", color="blue")
plt.show()