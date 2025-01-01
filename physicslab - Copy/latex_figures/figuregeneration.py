import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../run1processed2.csv', header=None)


mass = 0.090
k = 10
x0 = 0.328
x=0.24

# #gravitational-potential-energy.png
gravitational_energy = []
for i in range(len(data[1])):
    gravitational_energy.append(
        mass * (data[1][i] - x0) * 9.80665)

#     plt.plot(data[0][i], gravitational_energy[i], 'bo', markersize=1)
#
# plt.ylim(-0.15, 0)
# plt.ylabel("Gravitational Potential Energy (J)")
# plt.xlabel("Time (s)")
# plt.show()
# print(1)


# #gravitational-potential-energy-zoomed.png
# gravitational_energy = []
# for i in range(len(data[1])):
#     gravitational_energy.append(
#         mass * (data[1][i] - x0) * 9.80665)
#
#     plt.plot(data[0][i], gravitational_energy[i], 'bo', markersize=1)
#
# plt.ylim(-0.15, 0)
# plt.xlim(0,2.5)
# plt.ylabel("Gravitational Potential Energy (J)")
# plt.xlabel("Time (s)")
# plt.show()
# print(1)


# #elastic-potential-energy.png
spring_energy = []
for i in range(len(data[1])):
    spring_energy.append(
        k * (x0 - data[1][i])**2/2)

#     plt.plot(data[0][i], spring_energy[i], 'bo', markersize=1)
#
# plt.ylim(0,0.1)
# plt.ylabel("Elastic Potential Energy (J)")
# plt.xlabel("Time (s)")
# plt.show()
# print(1)

# #elastic-potential-energy-zoomed.png
# spring_energy = []
# for i in range(len(data[1])):
#     spring_energy.append(
#         k * (x0 - data[1][i])**2/2)
#
#     plt.plot(data[0][i], spring_energy[i], 'bo', markersize=1)
#
# plt.ylim(-0.1,0.2)
#
# plt.axhline(0, color='black', linewidth=0.5)
# plt.xlim(0,2.5)
# plt.ylabel("Elastic Potential Energy (J)")
# plt.xlabel("Time (s)")
# plt.show()
# print(1)

# #elastic-potential-energy.png
kinetic_energy = []
for i in range(len(data[1])):
    kinetic_energy.append(
        mass * data[2][i]**2/2)

#     plt.plot(data[0][i], kinetic_energy[i], 'bo', markersize=1)
#
# plt.ylim(0.0,0.012)
#
# # plt.axhline(0, color='black', linewidth=0.5)
# # plt.xlim(0,2.5)
# plt.ylabel("Kinetic Energy (J)")
# plt.xlabel("Time (s)")
# plt.show()
# print(1)

# #elastic-potential-energy-zoomed.png
# kinetic_energy = []
# for i in range(len(data[1])):
#     kinetic_energy.append(
#         mass * data[2][i]**2/2)
#
#     plt.plot(data[0][i], kinetic_energy[i], 'bo', markersize=1)
#
# plt.ylim(-0.02,0.03)
#
# plt.axhline(0, color='black', linewidth=0.5)
# plt.xlim(0,1)
# plt.ylabel("Kinetic Energy (J)")
# plt.xlabel("Time (s)")
# plt.show()
# print(1)

# #mechanical-energy.png
mechanical_energy = []
for i in range(len(data[1])):
    mechanical_energy.append(
        kinetic_energy[i]+gravitational_energy[i]+spring_energy[i])

    plt.plot(data[0][i], mechanical_energy[i], 'bo', markersize=1)

plt.ylim(-0.04,-0.02)
# plt.yscale(0.002)
plt.yticks(np.arange(-0.04, -0.019, 0.002))
plt.yticks(fontsize=9)
x = np.linspace(0, data[0][len(data[0])-1], (len(data[0])-1)*100)

plt.xlim(0,)
y1 = -0.000322*x - 0.026
y2 = -0.000026*x-0.0346
y3 = -0.0000018*x-0.03821

plt.plot(x, y1, '-r', label='linear fit at t = 5')
plt.plot(x, y2, '-c', label='linear fit at t = 100')
plt.plot(x, y3, '-m', label='linear fit at t = 300')

# plt.axhline(0, color='black', linewidth=0.5)
# plt.xlim(90,110)
plt.ylabel("Mechanical Energy (J)")
plt.xlabel("Time (s)")
plt.legend()
plt.show()
print(1)



