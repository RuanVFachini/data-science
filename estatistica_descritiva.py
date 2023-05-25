# https://www.kaggle.com/datasets/prasertk/netflix-daily-top-10-in-us?resource=download - Dataset
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt

df = read_csv(".\DataSets\\netflix daily top 10.csv")

df = df[df['As of'] == '2020-04-01']
df = df.filter(['Title', 'Viewership Score'])

acessos = df['Viewership Score'].values
titulos = df['Title'].values

fig=plt.figure()
ax=plt.subplot()

bars = plt.bar(titulos,acessos)

labels = list(map(lambda k: k.replace(" ", "\n"), df['Title'].values))

ax.set_title('Notas da lista TOP10(1/4/2020) - Netflix')
ax.set_xlabel('Título')
ax.set_ylabel('Nota')

ax.set_xticklabels(labels, rotation = 45)

ax.set_yticks(np.arange(plt.ylim()[0], plt.ylim()[1], 5))


plt.show()