# Purpose:
# This program reads data from multiple CSV files, processes the data, and visualizes it through graphs. 
# The program also calculates the average of the data (excluding the time column) and graphs the calculated averages.
# Additionally, the program processes time data from Excel format to seconds for better analysis and comparison.

# Key Features:
# 1. **File Handling**: Reads multiple CSV files containing time-series data.
# 2. **Data Processing**:
#    - Computes the row-wise average (ignoring the first column, which is the time).
#    - Converts time values from Excel time format (HH:MM:SS) to total seconds for consistency in graphing.
# 3. **Graphing**:
#    - Plots the averages of the data from each file.
#    - Plots the individual data lines (excluding time and average) with appropriate labels.
# 4. **Dynamic Labeling**: Automatically generates labels for each graph based on the file and column names.

# Libraries Used:
# - pandas: For reading and processing CSV data.
# - matplotlib: For creating graphs and visualizing the data.

# Output:
# - Two graphs: 
#   1. Average values from each file vs. time.
#   2. Individual data lines from the CSV files vs. time.

# Input Format:
# - CSV files with the first column as time in HH:MM:SS format, followed by numerical data columns.


import pandas as pd
import matplotlib.pyplot as plt

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

# Graph the data's averages
for i in range(len(fileData)):
    plt.plot(fileData[i][0], fileData[i][1], label=files[i][1])
plt.legend()
plt.show()

# Graph the lines
for line in lines:
    plt.plot(line[0], line[1], label=line[2])
plt.legend()
plt.show()
