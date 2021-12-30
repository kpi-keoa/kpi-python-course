import matplotlib.pyplot as plt
import numpy as np


xes = []
ys = []
with open('coordinates.txt') as f:
     for line in f:
         x, y = line.split()
         xes.append(x)
         ys.append(y)


fig, ax = plt.subplots()
ax.scatter(xes, ys)
ax.set_title('Points of activity')
plt.show()