# https://data.world/kgarrett/covid-19-open-research-dataset - link para dataset
from pandas import read_csv, Timestamp
import numpy as np
from matplotlib import pyplot as plt

df = read_csv(  ".\DataSets\covid_12-04-2020.csv",
                parse_dates=['date'],
                date_format="%Y-%m-%d")

df = df[df['location'] == 'Brazil']
df = df[df['date'].dt.strftime('%Y') == '2020']

df = df.filter(['date', 'total_cases','total_deaths', 'weekly_deaths'])
df = df.resample(rule='M', on='date').sum()

x = np.arange(len(df))

total_cases = df['total_cases'].values
total_deaths = df['total_deaths'].values
weekly_deaths = df['weekly_deaths'].values
width = 0.2
  
plt.bar(x-width, total_cases, width, color='cyan')
plt.bar(x, total_deaths, width, color='orange')
plt.bar(x+width, weekly_deaths, width, color='green')

monthStickList = []

for date in df.axes[0].values:
    monthStickList.append(Timestamp(date).strftime("%m/%Y"))

plt.xticks(x, monthStickList)
plt.xlabel("Meses")
plt.ylabel("Médias")
plt.legend(["Total de casos", "Total de mortes", "Mortes semanais"])
plt.ticklabel_format(style='sci', axis='y', useMathText=True)

plt.yticks(np.arange(plt.ylim()[0], plt.ylim()[1], 10000000))

plt.show()