# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
from scipy.optimize import curve_fit as cf
import csv
import numpy
import matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import functions

# Importing x and y coordinates of the data collected into 2 seperate arrays
# If output two things you can define two variables in same line
xdata, ydata = functions.read_csv()

# print(xdata)
# print(ydata)
# Make a scatterplot with the graph
plt.scatter(xdata, ydata, label="Experimental Data")

# Adding a title and x, y labels to the graph, and a legend
plt.title("Magnetic Field Strength of Disc Magnet vs Gauss Meter Distance")
plt.xlabel("Distance (m)")
plt.ylabel("Magnetic Field Strength (T)")


def func(x, a, c):
    return (10 ** (-7)) * (((3 * a) - a) / (x + c) ** 3)


# Lengths of both data sets need to be same for plot to work
# print(len(xdata))

# Find the optimal parameters and fit of the curve (and formatting to 5 and 7 decimal places)
popt, perr = curve_fit(func, xdata, ydata)
print("Estimation of magnetization: " + str(format(float(popt[0]), '.5f'))
      + "\n" + "Zero error: " + str(format(float(popt[1]), '.7f')))

# Plot the curve with the optimal parameter
funcdata = []
for i in range(0, 41):
    funcdata += [func(xdata[i], popt[0], popt[1])]

plt.plot(xdata, funcdata, label="model", color="black")

# Make the graph
plt.legend()
plt.show()
