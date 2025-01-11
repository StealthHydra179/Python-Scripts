import csv
import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#open data in run1processed2.csv
data = pd.read_csv('run1processed2.csv', header=None)

#create an array of the peaks, also store the previous or the next point, which everone is greater in position
peaks = []
for i in range(len(data[1])):
    if i == 0:
        if data[1][i] > data[1][i+1]:
            peaks.append([i,data[0][i], data[1][i], data[2][i], data[3][i]])
    elif i == len(data[1])-1:
        if data[1][i] > data[1][i-1]:
            peaks.append([i,data[0][i], data[1][i], data[2][i], data[3][i]])
    else:
        if data[1][i] > data[1][i-1] and data[1][i] > data[1][i+1]:
            peaks.append([i,data[0][i], data[1][i], data[2][i], data[3][i]])

secondpeaks = []
for i in range(len(peaks)):
    index = peaks[i][0]
    if index == 0:
        secondpeaks.append([index+1,data[0][index+1], data[1][index+1], data[2][index+1], data[3][index+1]])
    elif index == len(data[1])-1:
        secondpeaks.append([index-1,data[0][index-1], data[1][index-1], data[2][index-1], data[3][index-1]])
    else:
        if data[1][index-1] > data[1][index+1]:
            secondpeaks.append([index-1,data[0][index-1], data[1][index-1], data[2][index-1], data[3][index-1]])
        else:
            secondpeaks.append([index+1,data[0][index+1], data[1][index+1], data[2][index+1], data[3][index+1]])

# for i in range(len(peaks)):
#     print(peaks[i], secondpeaks[i])

def calculateTruePeak(v1,v2, x1,x2, t1,t2):
    a = v1*100
    range = math.acos(v2/a) - math.acos(v1/a)
    print(range)
    timediff = t2-t1
    # print(timediff)
    velocityleft = math.acos(0)-math.acos(v1/a)
    v_l = timediff*velocityleft/range

    theta = math.pi/2 * v_l/0.25 * -1
    final = x1/math.cos(theta)
    # print(final)
    return v_l+t1, final


finalpeaks = []
for i in range(len(peaks)):
    if peaks[i][0] > secondpeaks[i][0]:
        #peaks comes second
        truepeaktime, truepeakheight = calculateTruePeak(secondpeaks[i][3], peaks[i][3], secondpeaks[i][2], peaks[i][2], secondpeaks[i][1], peaks[i][1])
    else:
        #secondpeaks comes second
        truepeaktime, truepeakheight = calculateTruePeak(peaks[i][3], secondpeaks[i][3], peaks[i][2], secondpeaks[i][2], peaks[i][1], secondpeaks[i][1])
    finalpeaks.append([truepeaktime, truepeakheight])
    # print(truepeaktime, truepeakheight)

#plot final peaks
for i in range(len(finalpeaks)):
    plt.plot(finalpeaks[i][0], finalpeaks[i][1], 'ro')
plt.show()
