import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('run1processed2.csv', header=None)


mass = 0.090
k = 10
x0 = 0.328
x=0.24

gravitational_energy = []
for i in range(len(data[1])):
    gravitational_energy.append(
        mass * (data[1][i] - x0) * 9.80665)

spring_energy = []
for i in range(len(data[1])):
    spring_energy.append(
        k * (x0 - data[1][i])**2/2)


kinetic_energy = []
for i in range(len(data[1])):
    kinetic_energy.append(
        mass * data[2][i]**2/2)

mechanical_energy = []
for i in range(len(data[1])):
    mechanical_energy.append(
        kinetic_energy[i]+gravitational_energy[i]+spring_energy[i])

start = 8344
end = 8344

start -= 1

intc = 0
for i in range(start*5,end*5, 5):
    # print(i/100, int(data[1][int(i/5)]*1000)/1000, int(data[2][int(i/5)]*1000)/1000, int(mechanical_energy[int(i/5)]*1000)/1000)
    print("%.2f %.3f %.3f %.5f" % (i/100, data[1][int(i/5)], data[2][int(i/5)], mechanical_energy[int(i/5)]))
    intc += 1

print(intc)
#avg of mech eng
total = 0
for i in range(start*5, end*5, 5):
    total += mechanical_energy[int(i/5)]
print(total/intc)

# #mechanical energy at 5 seconds
# i = 5*100
# print("%.2f %.3f %.3f %.3f" % (i/100, data[1][int(i/5)], data[2][int(i/5)], mechanical_energy[int(i/5)]))