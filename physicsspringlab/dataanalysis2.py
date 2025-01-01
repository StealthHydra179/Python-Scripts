import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#time, position, velocity, acceleration
#open data in run1processed2.csv
data = pd.read_csv('run1processed2.csv', header=None)

#calculate mechanical energy
#mechanical energy = gravitational potential energy + kinetic energy + spring potential energy
#gravitational potential energy = mass * height * gravity
#kinetic energy = mass * velocity^2 / 2
#spring potential energy = spring constant * height^2 / 2
#mass is 50g
mechanical_energy = []
#height is position relative to 0.2875723796296133
#0.24052874999999999+0.049= 0.28952874999999999
for i in range(len(data[1])):
    # mechanical_energy.append([0.05 * (data[1][i]) * 9.8 + 0.05 * 0.5 * data[2][i]**2 + 0.5 * 10 * (data[1][i] - 0.28020000000000002)**2, 0.05*(data[1][i])*9.8, 0.05 * 0.5 * data[2][i]**2, 0.5*10*(data[1][i] - 0.28020000000000002)**2])
    # mechanical_energy.append(
    #     0.05 * data[2][i] ** 2 * 0.5 + 0.5 * 10 * (
    #                 data[1][i] - 0.24020000000000002) ** 2)
    # mechanical_energy.append(0.04 * (data[1][i]) * 9.80665 + 0.04 * 0.5 * data[2][i]**2 + 0.5 * 10 * (data[1][i] - 0.28020000000000002)**2)
    mechanical_energy.append(
        0.04 * (data[1][i]) * 9.80665 + 0.04 * 0.5 * data[2][i] ** 2 + 0.5 * 9.5 * (
                    data[1][i] - 0.281746) ** 2)

    plt.plot(data[0][i], mechanical_energy[i], 'ro')
    # plt.plot(data[0][i], mechanical_energy[i][1]+mechanical_energy[i][2]+mechanical_energy[i][3], 'ro')
    # plt.plot(data[0][i], mechanical_energy[i][1], 'bo')
    # plt.plot(data[0][i], mechanical_energy[i][2], 'go')
    # plt.plot(data[0][i], mechanical_energy[i][3], 'yo')
# plt.xlim(50, 52)
plt.show()
print(1)

# #split graphs into seperate graphs
# for i in range(len(mechanical_energy)):
#     plt.plot(data[0][i], mechanical_energy[i][1], 'bo')
# plt.figure(dpi=1500)
# plt.show()
#
# for i in range(len(mechanical_energy)):
#     plt.plot(data[0][i], mechanical_energy[i][2], 'go')
# plt.show()
# for i in range(len(mechanical_energy)):
#     plt.plot(data[0][i], mechanical_energy[i][3], 'yo')
# plt.show()
#
# for i in range(len(mechanical_energy)):
#     plt.plot(data[0][i], mechanical_energy[i][1]+mechanical_energy[i][2]+mechanical_energy[i][3], 'ro')
# plt.show()
#
# print(len(mechanical_energy))

#calculate discrite derivative of mechanical energy
#discrite derivative = (mechanical energy at time t + 1 - mechanical energy at time t) / (time at t + 1 - time at t)
discrite_derivative = []
skip = 450
for i in range(len(mechanical_energy)-skip):
    discrite_derivative.append((mechanical_energy[i+skip] - mechanical_energy[i]) / (data[0][i+skip] - data[0][i]))
    plt.plot(data[0][i], discrite_derivative[i], 'ro')
plt.show()
print(len(mechanical_energy))
print(len(discrite_derivative))