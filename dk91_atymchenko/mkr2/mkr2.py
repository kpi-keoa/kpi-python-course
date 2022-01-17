import matplotlib.pyplot as plt
import numpy as np
import math

# read data from file
src_data = loadDataFromFile(E:\kpi-python-course\dk91_atymchenko\mkr2\data.csv)
# create variables with the received data  
x, y, grid_size, r = np.array([]), np.array([]), 0, 0
for key in src_data:
    x = np.append(np.random.randint(key[0:2]))
    y = np.append(np.random.randint(key[3:5]))
    grid_size = key[6]
    r = key[7]
# grid
x_mesh_grid = np.meshgrid(np.arange(min(x) - r, max(x) + r, grid_size))
y_mesh_grid = np.meshgrid(np.arange(min(y) - r, max(y) + r, grid_size))
# center point for each grid square
xc, yc = x_mesh_grid + (grid_size / 2), y_mesh_grid + (grid_size/ 2)
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
