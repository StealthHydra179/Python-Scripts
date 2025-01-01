# import pandas as pd
# data = pd.read_csv('run1processed2.csv', header=None)

from multiprocessing import Pool
import csv
import dataanalysis2_21

if __name__ == '__main__':

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


    x0_start = 0.20
    x0_end = 0.35
    x0_inc = 0.001
    max = 0.2


    minx0 = 0
    minm = 0
    mink = 0
    mind = 10000000

    for x0 in range(0,(int)((x0_end - x0_start) / x0_inc), 10):
        # if x0 % 10 == 0:
        #     print("x0", x0)

        x0_current = x0_start + x0 * x0_inc

        if x0 % 1 == 0:
            print("x0", x0_current)

        with Pool(10) as p:
            results = p.starmap(dataanalysis2_21.toSolve, [(x0_current, data,max),(x0_current + x0_inc, data,max), (x0_current + 2 * x0_inc, data,max), (x0_current + 3 * x0_inc, data,max), (x0_current + 4 * x0_inc, data,max), (x0_current + 5 * x0_inc, data,max), (x0_current + 6 * x0_inc, data,max), (x0_current + 7 * x0_inc, data,max), (x0_current + 8 * x0_inc, data,max), (x0_current + 9 * x0_inc, data,max)])
            for resultList in results:
                for result in resultList:
                    if result[3] < mind:
                        minx0 = result[0]
                        minm = result[1]
                        mink = result[2]
                        mind = result[3]
                        print("new min", minx0, minm, mink, mind)

    print(1)
