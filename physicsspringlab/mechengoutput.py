import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('run1processed2.csv', header=None)

mechanical_energy = []

mass = 0.090
k = 10
x0 = 0.33

for i in range(len(data[1])):
    mechanical_energy.append([data[0][i],
        mass * (data[1][i]-x0) * 9.80665 + mass * 1/2 * data[2][i] ** 2 + 1/2 * k * (
                    data[1][i] - x0) ** 2])

    # plt.plot(data[0][i], mechanical_energy[i], 'bo', markersize=2)

#save mechanical energy
mechanical_energy_csv = pd.DataFrame(mechanical_energy)
mechanical_energy_csv.to_csv('mechanical_energy1.csv', header=False, index=False)