### Plots x vs y position graphs with vz color bar for gas ###
### Left graph is just vz coloring and right graph is vz coloring with blue gas positon on top to make it easier to see the spiral arms ###
### [0] = Gas ###
### [4] = Star ###

import math 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as ml
import matplotlib as mpl
import glio
s = glio.GadgetSnapshot('snapshot_010')		### Change snapshot here ###
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


### Plots star and gas x vs y graphs with a vz bar on the same canvas ###
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
a = gas_px_xy[0::2]
gas_py_xy = np.array(gas_y_xy)
b = gas_py_xy[0::2]
gas_vz_bar = np.array(gas_vz_xy)


### Plots the graphs ###
plt.subplot(121)
plt.hexbin(gas_px_xy, gas_py_xy, C=gas_vz_bar, cmap=cm.jet_r, gridsize=300, vmin=-20, vmax=20)
plt.title('Gas x vs y')
plt.xlabel('x')
plt.ylabel('y')
plt.text(20, 20, 't = 39')				### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
#cbar = plt.colorbar()
#cbar.set_label('Vz')
plt.grid()

plt.subplot(122)
plt.hexbin(gas_px_xy, gas_py_xy, C=gas_vz_bar, cmap=cm.jet_r, gridsize=300, vmin=-20, vmax=20)
plt.plot(a, b, '.', markersize=3, alpha=0.3)
plt.title('Gas x vs y')
plt.xlabel('x')
plt.ylabel('y')
plt.text(20, 20, 't = 39')				### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
#cbar = plt.colorbar()
#cbar.set_label('Vz')
plt.grid()

plt.show()