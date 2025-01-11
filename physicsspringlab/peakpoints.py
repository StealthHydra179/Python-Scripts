import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#open data in peak points
peakpoints = pd.read_csv('peakpoints.csv', header=None)
print(len(peakpoints[0]))
print(peakpoints)

mechanicalenergy = []
for i in range(len(peakpoints[0])):
    mechanicalenergy.append([peakpoints[0][i], 0.05*9.8*peakpoints[1][i] + 10*peakpoints[1][i]*peakpoints[1][i]/2])
    plt.plot(mechanicalenergy[i][0], mechanicalenergy[i][1], 'ro')
plt.xlim(50,70)
plt.show()

for i in range(len(peakpoints)):
    plt.plot(peakpoints[0][i], peakpoints[1][i], 'ro')
plt.show()

for i in range(len(peakpoints)):
    plt.plot(peakpoints[0][i], peakpoints[2][i], 'ro')
plt.show()

center = 0.24039254068791988