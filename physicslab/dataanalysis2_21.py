def toSolve(x0_current,data,max):
    #print(x0_current)
    mass_start = 0.045
    mass_end = 0.15
    mass_inc = 0.001
    result = [[0, 0, 0, 10000000]]
    for mass in range((int)((mass_end - mass_start) / mass_inc)):

        mass_current = mass_start + mass * mass_inc

        # if mass % 1000 == 10:
        #     print("x0", x0_current, "mass", mass_current)

        k_start = 9
        k_end = 16
        k_inc = 0.01
        for k in range((int)((k_end - k_start) / k_inc)):
            #
            # if k % 1000 == 100:
            #     print("k", k)

            k_current = k_start + k * k_inc

            mechanical_energy = []
            for i in range(len(data[1])):
                mechanical_energy.append(mass_current * (data[1][i]) * 9.80665 + mass_current * 0.5 * data[2][
                    i] ** 2 + 0.5 * k_current * (data[1][i] - x0_current) ** 2)
                # mechanical_energy.append(0.05 * 0.5 * data[2][i] ** 2 + 0.5 * 10 * (data[1][i] - current) ** 2)

            # discrete_derivative = []
            # skip = 1
            # for i in range(len(mechanical_energy) - skip):
            #     discrete_derivative.append(
            #         (mechanical_energy[i + skip] - mechanical_energy[i]) / (data[0][i + skip] - data[0][i]))

            # max_d = -10000000
            # for i in range(len(discrete_derivative)):
            #     if discrete_derivative[i] > max_d:
            #         max_d = discrete_derivative[i]

            #max mech eng from 95 sec to 105 sec
            max_d = -10000000
            for i in range(len(mechanical_energy)):
                if data[0][i] > 95 and data[0][i] < 105:
                    if mechanical_energy[i] > max_d:
                        max_d = mechanical_energy[i]
            #min mech eng from 95 sec to 105 sec
            min_d = 10000000
            for i in range(len(mechanical_energy)):
                if data[0][i] > 95 and data[0][i] < 105:
                    if mechanical_energy[i] < min_d:
                        min_d = mechanical_energy[i]

            max_d = max_d - min_d

            solution_works = True
            if max_d > max:
                solution_works = False
                # print("doesnt work:",current, "maxv", max_d)

            if solution_works:
                # print("works:", x0_current, "m", mass_current, "k", k_current, "maxd", max_d)
                result.append([x0_current, mass_current, k_current, max_d])
    return result
