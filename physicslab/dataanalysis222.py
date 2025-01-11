import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('run1processed2.csv', header=None)

# #graph position vs time
#
# for i in range(len(data[1])):
#     # plt.plot(data[0][i], data[1][i], 'bo', markersize=2)
#
#     plt.plot(data[0][i], data[2][i], 'bo', markersize=2)
#
# # plt.ylabel("Position (m)")
#
# plt.ylabel("Velocity (m)")
# plt.xlabel("Time (s)")
#
# plt.yticks(fontsize=8)
# plt.xticks(fontsize=8)
# plt.xlim(0,)
# plt.ylim(0,)
# plt.show()


mechanical_energy = []
# mass = 0.045
# k = 4
# x0 = 0.349

# mass = 0.045
# k = 10
# x0 = 0.28500000000000003
#
mass = 0.08903040
k = 10
x0 = 0.32801421

# mass = 0.09
# k = 10.1
# x0 = 0.32801421

# mass = 0.045
# k = 15.46
# x0 = 0.269

for i in range(len(data[1])):
    mechanical_energy.append(
        mass * (data[1][i]) * 9.80665 + mass * 1/2 * data[2][i] ** 2 + 1/2 * k * (
                    data[1][i] - x0) ** 2)

    # plt.plot(data[0][i], mechanical_energy[i], 'bo', markersize=2)
# plt.xlim(90,110)
# plt.show()
print(1)

discrite_derivative = []
skip = 112
for i in range(len(mechanical_energy)-skip):
    discrite_derivative.append((mechanical_energy[i+skip] - mechanical_energy[i]) / (data[0][i+skip] - data[0][i]))
    plt.plot(data[0][i], discrite_derivative[i], 'bo', markersize=2)

plt.axhline(y=0, color='black', linewidth=0.5)
plt.ylabel("Rate of Change of Mechanical Energy (J/s)")
plt.xlabel("Time (s)")

plt.yticks(fontsize=8)
plt.xticks(fontsize=8)
plt.xlim(0,)



#graph \frac{dM}{dt} &= -0.000222 \times 10^{-0.008873 \times t} \\
x = np.linspace(0, data[0][len(data[0])-1], (len(data[0])-1)*100)
y = -0.000222 * 10**(-0.008873 * x)
plt.plot(x, y, 'r')

plt.show()
print(len(mechanical_energy))
print(len(discrite_derivative))



#average of discrete derivative
total = 0
for i in range(len(discrite_derivative)):
    total += discrite_derivative[i]
print(total/len(discrite_derivative))