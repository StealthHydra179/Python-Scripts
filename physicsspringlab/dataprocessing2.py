#import csv from run1processed.csv
#shift times so that the first time is equal to 0
#output: run1processed2.csv

import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#open data in run1processed.csv
data = pd.read_csv('run1processed.csv', header=None)

#create new csv with shifted times
new_csv = pd.DataFrame(columns=[0, 1, 2, 3])
new_csv[0] = data[0] - data[0][0]
new_csv[1] = data[1]
new_csv[2] = data[2]
new_csv[3] = data[3]

#second graph the data
plt.plot(new_csv[0], new_csv[1])
plt.show()

#save the data to run1processed2.csv
new_csv.to_csv('run1processed2.csv', header=False, index=False)