import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('run1processed2.csv', header=None)

#round everything to three decimal places
for i in range(len(data[1])):
    data[1][i] = round(data[1][i], 3)
    data[2][i] = round(data[2][i], 3)
    data[3][i] = round(data[3][i], 3)
    data[0][i] = round(data[0][i], 3)

#save as csv but with & as the delimeter and \\ at the end of each line
data.to_csv('run1processed2_1.csv', sep='&', index=False, header=False, lineterminator='\\\\\n\\hline\n')