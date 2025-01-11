import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#inport data from run1processed2.csv
data = pd.read_csv('run1processed2.csv', header=None)

# find the point with the maximum magnitude of velocity
max = 0
maxx = 0
for i in range(len(data[3])):
    if data[3][i] > max:
        max = data[3][i]
        maxx = data[0][i]

# find the point with the minimum magnitude of velocity
min = 1
minx = 0
for i in range(len(data[3])):
    if data[3][i] < min:
        min = data[3][i]
        minx = data[0][i]

# log the max and min points
print("max: " + str(max) + " at " + str(maxx))
print("min: " + str(min) + " at " + str(minx))

#graph velocity
plt.plot(data[0], data[3])
plt.xlim(350,400)
plt.ylim(0,1)
plt.show()