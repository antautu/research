### Produces a 3D gas position plot with a Vz bar for any snapshot  ###

import math
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as ml
import glio
s = glio.GadgetSnapshot('snapshot_013')
s.load()

### Produces data to plot star x vs y with a vz bar ###
f = open('data_star_xy_vz','w')
for i in range(0, len(s.pos[4][:])):

	x_star = s.pos[4][i][0]
	y_star = s.pos[4][i][1]
	z_star = s.pos[4][i][2]

	r_star = math.sqrt(x_star**2 + y_star**2)
	theta_star = math.atan2(y_star, x_star)

	vx_star = s.vel[4][i][0]
	vy_star = s.vel[4][i][1]
	vz_star = s.vel[4][i][2]

	vr_star = vx_star * math.cos(theta_star) + vy_star * math.sin(theta_star)
	vtheta_star = vy_star * math.cos(theta_star) - vx_star * math.sin(theta_star)

	f.write("%s %s %s\n" % (x_star, y_star, vz_star))

f.close()


### Produces data to plot gas x vs y with vz bar ###
f = open('data_gas_xy_vz','w')
for i in range(0, len(s.pos[0][:])):

	x_gas = s.pos[0][i][0]
	y_gas = s.pos[0][i][1]
	z_gas = s.pos[0][i][2]

	r_gas = math.sqrt(x_gas**2 + y_gas**2)
	theta_gas = math.atan2(y_gas, x_gas)

	vx_gas = s.vel[0][i][0]
	vy_gas = s.vel[0][i][1]
	vz_gas = s.vel[0][i][2]

	vr_gas = vx_gas * math.cos(theta_gas) + vy_gas * math.sin(theta_gas)
	vtheta_gas = vy_gas * math.cos(theta_gas) - vx_gas * math.sin(theta_gas)

	f.write("%s %s %s\n" % (x_gas, y_gas, vz_gas))

f.close()


### Plots a 3D graph of gas position with a Vz z axis and color bar ###
f2 = open('data_star_xy_vz')
lines = f2.readlines()
f2.close()

star_x_xy = []
star_y_xy = []
star_vz_xy = []

for line in lines:
	p = line.split()
	star_x_xy.append(float(p[0]))
	star_y_xy.append(float(p[1]))
	star_vz_xy.append(float(p[2]))

star_px_xy = np.array(star_x_xy)
star_py_xy = np.array(star_y_xy)
star_vz_bar = np.array(star_vz_xy)

f2 = open('data_gas_xy_vz')
lines = f2.readlines()
f2.close()

gas_x_xy = []
gas_y_xy = []
gas_vz_xy = []

for line in lines:
	p = line.split()
	gas_x_xy.append(float(p[0]))
	gas_y_xy.append(float(p[1]))
	gas_vz_xy.append(float(p[2]))

gas_px_xy = np.array(gas_x_xy)
gas_py_xy = np.array(gas_y_xy)
gas_vz_bar = np.array(gas_vz_xy)


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
p = ax.scatter3D(gas_px_xy, gas_py_xy, gas_vz_bar, c=gas_vz_bar, cmap='jet_r', s=10, vmin=-20, vmax=20)		### s is the size of the marker ###
cbar = fig.colorbar(p)
ax.set_xlim3d(-25, 25)
ax.set_ylim3d(-25, 25)
ax.set_zlim3d(-20, 20)

plt.show()