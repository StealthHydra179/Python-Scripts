import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#inport data from run1processed2.csv
data = pd.read_csv('run1processed2.csv', header=None)

# print(data)

#find the average position of the points
avg = 0
for i in range(len(data[1])):
    avg += data[1][i]
avg /= len(data[1])
print(avg)

#draw a horizontal line through the data with the y value being the average position of the points
plt.plot(data[0], data[1])
plt.plot([0, data[0][len(data[0])-1]], [avg, avg])
plt.show()

#find maximum point
max = 0
maxx = 0
for i in range(len(data[1])):
    if data[1][i] > max:
        max = data[1][i]
        maxx = data[0][i]

#find minimum point
min = 1
minx = 0
for i in range(len(data[1])):
    if data[1][i] < min:
        min = data[1][i]
        minx = data[0][i]

#log min and max points and their differences to the average
print("max: " + str(max) + " at " + str(maxx) + " difference: " + str(max - avg))
print("min: " + str(min) + " at " + str(minx) + " difference: " + str(min - avg))
print("(max+min)/2 " + str((max+min)/2) + " difference: " + str((max+min)/2 - avg))

#create a list of the peak points and their times
#peak point is defined as the point to the left is non existent or lower and the point to the right is non existent or lower
peakpoints = []
for i in range(len(data[1])):
    if i == 0:
        if data[1][i] > data[1][i+1]:
            peakpoints.append([data[0][i], data[1][i], data[2][i], data[3][i]])
    elif i == len(data[1])-1:
        if data[1][i] > data[1][i-1]:
            peakpoints.append([data[0][i], data[1][i], data[2][i], data[3][i]])
    else:
        if data[1][i] > data[1][i-1] and data[1][i] > data[1][i+1]:
            peakpoints.append([data[0][i], data[1][i], data[2][i], data[3][i]])

# filter and make sure that a new array such that peakpoints is decreasing
for i in range(len(peakpoints[0])-1):
    if peakpoints[1][i] < peakpoints[1][i+1]:
        peakpoints = peakpoints.remove(peakpoints[i])

print(len(peakpoints))
#save peakpoints
# peakpointscsv = pd.DataFrame(peakpoints)
# peakpointscsv.to_csv('peakpoints.csv', header=False, index=False)

#graph peak points
for i in range(len(peakpoints)):
    plt.plot(peakpoints[i][0], peakpoints[i][1], 'ro', markersize=2)
plt.show()

#calculate and update in list peak point differences from average
for i in range(len(peakpoints)):
    peakpoints[i] = [peakpoints[i][0], peakpoints[i][1] - avg, peakpoints[i][2], peakpoints[i][3]]

#plot peakpoints[0] vs peakpoints[1]
# for i in range(len(peakpoints)):
#     plt.plot(peakpoints[i][0], peakpoints[i][1], 'ro')
# plt.show()

#calculate difference in time between peaks and graph and store in new list
peakpointstime = []
for i in range(len(peakpoints)-1):
    peakpointstime.append([peakpoints[i][0], peakpoints[i+1][0] - peakpoints[i][0]])
#     plt.plot(peakpointstime[i][0], peakpointstime[i][1], 'ro')
# plt.show()

#count most common period difference
# print(peakpointstime)


#calculate standard deviation
# std = 0
# for i in range(len(peakpointstime)):
#     std += peakpointstime[i][1]
# std /= len(peakpointstime)
# print("peakpointstime: " + str(std))
#
# print(len(peakpoints))

#using peakpoints curve fit a function and output the function
# curve = np.polyfit(peakpoints[0], peakpoints[1], 2)
# print(curve)

#graph the polyfit
# x = np.linspace(0, peakpoints[len(peakpoints)-1][0], len(peakpoints)-1)
# y = np.polyval(curve, x)
# for i in range(len(peakpoints)):
#     plt.plot(peakpoints[i][0], peakpoints[i][1], 'ro')
# plt.plot(x, y)
# plt.show()

#calculate mechanical energy: mgh + 1/2mv^2 + kdeltax^2/2
#h is difference from avg
#v is 0
#k is spring constant of 10
#deltax is difference from avg
#m is mass of 50g
#output: mechanical energy vs time
mechanicalenergy = []
for i in range(len(peakpoints)):
    mechanicalenergy.append([peakpoints[i][0], 10*peakpoints[i][1]*peakpoints[i][1]/2] + 0.05 * 1/2 * peakpoints[i][2]*peakpoints[i][2])
    plt.plot(mechanicalenergy[i][0], mechanicalenergy[i][1], 'ro')
plt.xlim(50,70)
plt.show()



#graph the discrete derivative of the mechanical energy
mechanicalenergyderivative = []
for i in range(len(mechanicalenergy)-1):
    mechanicalenergyderivative.append([mechanicalenergy[i][0], (mechanicalenergy[i+1][1] - mechanicalenergy[i][1])/(mechanicalenergy[i+1][0] - mechanicalenergy[i][0])])
    plt.plot(mechanicalenergyderivative[i][0], mechanicalenergyderivative[i][1], 'ro')
    # plt.ylim(-1,1)
    # plt.ylabel("change in mechanical energy")
    # plt.xlim(0,500)
plt.show()

#save peaks and mechanical energy to csv files
# peakpoints = pd.DataFrame(peakpoints)
# peakpoints.to_csv('peakpoints.csv', header=False, index=False)
# mechanicalenergy = pd.DataFrame(mechanicalenergy)
# mechanicalenergy.to_csv('mechanicalenergy.csv', header=False, index=False)


# filter and make sure that a new array such that peakpoints is decreasing
# for i in range(len(peakpoints)-1):
#     if peakpoints[i][1] < peakpoints[i+1][1]:
#         peakpoints = peakpoints.drop([i])


mechanicalenergyderivative2 = []
for i in range(len(mechanicalenergy)-50):
    mechanicalenergyderivative2.append([mechanicalenergy[i][0], (mechanicalenergy[i+50][1] - mechanicalenergy[i][1])/(mechanicalenergy[i+50][0] - mechanicalenergy[i][0])])
    plt.plot(mechanicalenergyderivative2[i][0], mechanicalenergyderivative2[i][1], 'ro')
plt.show()
print(len(mechanicalenergy))