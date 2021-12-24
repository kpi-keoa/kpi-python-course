import matplotlib.pyplot as plt
import numpy as np
import math

# create two lists for x and y containing 24 elements each
x = np.random.randint(14, 41, 24)
y = np.random.randint(15, 51, 24)
# display the resulting points on the graph
fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set_title('24 случайные точки')
plt.show()
# determine the size and radius of the grid
grid_size = 1
r = 10
# min, max for x and y
x_min = min(x)
x_max = max(x)
y_min = min(y)
y_max = max(y)
# grid
x_grid = np.arange (x_min - r, x_max + r, grid_size)
y_grid = np.arange (y_min - r, y_max + r, grid_size)
x_mesh, y_mesh = np.meshgrid(x_grid, y_grid)
# center point for each grid square
xc = x_mesh + (grid_size / 2)
yc = y_mesh + (grid_size/ 2)
# function for calculating the density of points 
def kde_quartic(d, r):
    dn = d / r
    P = (15/16) * (1 - dn ** 2) ** 2
    return P
intensity_list = []
for j in range(len(xc)):
    intensity_row = []
    for k in range(len(xc[0])):
        kde_value_list = []
        for i in range(len(x)):
            # calculate the distance
            d = math.sqrt((xc[j][k] - x[i]) ** 2 + (yc[j][k] - y[i]) ** 2) 
            if d <= r:
                p = kde_quartic(d,r)
            else:
                p = 0
            kde_value_list.append(p)
        # sum up all density values
        p_total = sum(kde_value_list)
        intensity_row.append(p_total)
    intensity_list.append(intensity_row)
# heat map visualization
intensity = np.array(intensity_list)
plt.pcolormesh(x_mesh, y_mesh, intensity)
plt.plot(x, y,'ro')
plt.colorbar()
plt.show()