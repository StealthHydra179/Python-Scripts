import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

files = [["data/file4044.csv", "4044"], ["data/file4045.csv", "4045"], ["data/file4047.csv", "4047"]]

fileData = []
lines = []

for fileInfo in files:
    print("Reading", fileInfo[0])

    # Read the file
    df = pd.read_csv(fileInfo[0])
    print(df.head())

    # Solve for average for each row, not including the time (first column)
    df['average'] = df.iloc[:, 1:].mean(axis=1)
    print(df.head())

    # Convert time to seconds
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')
    df['Time'] = df['Time'].dt.second + df['Time'].dt.minute * 60 + df['Time'].dt.hour * 3600
    print(df.head())

    # Save the average to fileData
    fileData.append([df['Time'], df['average']])

    # Get names of each column
    columns = df.columns

    # if column name is time or average, skip
    for i in range(len(columns)):
        if columns[i] == "Time" or columns[i] == "average":
            continue
        # If the column name is not time or average, save it to lines
        lines.append([df['Time'], df[columns[i]], fileInfo[1] + " " + columns[i]])

# Graph the data
for i in range(len(fileData)):
    plt.plot(fileData[i][0], fileData[i][1], label=files[i][1])
plt.legend()
plt.show()

# Graph the lines
for line in lines:
    plt.plot(line[0], line[1], label=line[2])
plt.legend()
plt.show()
