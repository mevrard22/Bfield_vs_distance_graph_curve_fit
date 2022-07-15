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

print(xdata)
print(ydata)
# Make a satterplot with the graph
plt.scatter(xdata, ydata)

# Adding a title and x, y labels to the graph
plt.title("Magnetic Field Strength of Disc Magnet vs Gauss Meter Distance")
plt.xlabel("Distance (m)")
plt.ylabel("Magnetic Field Strength (T)")


def func(x, a, c):
    return (10**(-7)) * (((3 * a) - a) / (x + c)**3)

# Create placeholder function data to plot func
funcdata = []
for i in range(0, 41):
    funcdata += [func(xdata[i], 0.42337, 0.00766)]

# Lenghts of both data sets need to be same for plot to work
print(len(xdata))
print(len(funcdata))
plt.plot(xdata, funcdata)

# plt.plot(xdata, funcdata)
popt, pcov = curve_fit(func, xdata, ydata)


# Make the graph
plt.show()
