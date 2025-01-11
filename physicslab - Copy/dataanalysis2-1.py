# import pandas as pd
# data = pd.read_csv('run1processed2.csv', header=None)

import csv
data = []
with open('run1processed2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    current1 = []
    current2 = []
    current3 = []
    current4 = []
    for row in reader:
        current1 += [float(row[0])]
        current2 += [float(row[1])]
        current3 += [float(row[2])]
        current4 += [float(row[3])]

    data = [current1, current2, current3, current4]

x0_start = 0.23
x0_end = 0.28
x0_inc = 0.00001
max = 0.09
for x0 in range((int)((x0_end - x0_start) / x0_inc)):

    # if x0 % 10 == 0:
    #     print("x0", x0)

    x0_current = x0_start + x0 * x0_inc

    if x0 % 1 == 0:
        print("x0", x0_current)

    mass_start = 0.045
    mass_end = 0.055
    mass_inc = 0.0001
    for mass in range((int)((mass_end - mass_start) / mass_inc)):

        mass_current = mass_start + mass * mass_inc

        # if mass % 1000 == 10:
        #     print("x0", x0_current, "mass", mass_current)

        k_start = 9.5
        k_end = 10.5
        k_inc = 0.01
        for k in range((int)((k_end - k_start) / k_inc)):
            #
            # if k % 1000 == 100:
            #     print("k", k)

            k_current = k_start + k * k_inc

            mechanical_energy = []
            for i in range(len(data[1])):
                mechanical_energy.append(mass_current * (data[1][i]) * 9.80665 + mass_current * 0.5 * data[2][i] ** 2 + 0.5 * k_current * (data[1][i] - x0_current) ** 2)
                # mechanical_energy.append(0.05 * 0.5 * data[2][i] ** 2 + 0.5 * 10 * (data[1][i] - current) ** 2)


            discrete_derivative = []
            skip = 1
            for i in range(len(mechanical_energy) - skip):
                discrete_derivative.append((mechanical_energy[i + skip] - mechanical_energy[i]) / (data[0][i + skip] - data[0][i]))

            max_d = 0
            for i in range(len(discrete_derivative)):
                if discrete_derivative[i] > max_d:
                    max_d = discrete_derivative[i]

            solution_works = True
            if max_d > max:
                solution_works = False
                # print("doesnt work:",current, "maxv", max_d)

            if solution_works:
                print("works:", x0_current, "m", mass_current, "k", k_current, "maxd", max_d)


print(1)
