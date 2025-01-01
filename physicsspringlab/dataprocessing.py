#open data in run1csv.csv and process the data
#output: run1processed.csv

import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#open data in run1csv.csv
data = pd.read_csv('run1csv.csv', header=None)

#for all points in the graph find the maximum point and the x value
max = 0
maxx = 0
for i in range(len(data[1])):
    if data[1][i] > max:
        max = data[1][i]
        maxx = data[0][i]

#if the point is to the left of the maximum point, remove it from the csv
for i in range(len(data[1])):
    if data[0][i] < maxx:
        data = data.drop([i])

#second graph the data
plt.plot(data[0], data[1])
plt.show()

#save the data to run1processed.csv
data.to_csv('run1processed.csv', header=False, index=False)