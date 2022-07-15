# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import ax as ax
import scipy
import csv
import matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import functions

# Importing x and y coordinates of the data collected into 2 seperate arrays
x = functions.read_csv()[0]
y = functions.read_csv()[1]

# Make a scatterplot with the graph
plt.scatter(x, y)

# Adding a title and x, y labels to the graph
plt.title("Magnetic Field Strength of Disc Magnet vs Gauss Meter Distance")
plt.xlabel("Distance (m)")
plt.ylabel("Magnetic Field Strength (T)")



# Make the graph
plt.show()