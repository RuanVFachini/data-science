from pandas import read_csv
import numpy as np
from matplotlib import pyplot as plt

df = read_csv(".\DataSets\covid_12-04-2020.csv")
subjects = ["new_cases"]
dataset = df.groupby(["date", "location"])[subjects].mean()

contries_count = df['location'].unique()

for i in contries_count:
    

# indx = np.arange(len(subjects))
# score_labels = np.array(0,110,10)


# print(dataset)
# plt.show()