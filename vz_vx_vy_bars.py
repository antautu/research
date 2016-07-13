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
s = glio.GadgetSnapshot('snapshot_030')		### Change snapshot here ###
s.load()


### Produces data to plot gas x vs y with vz bar ###
f = open('data_gas_bars','w')
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

	f.write("%s %s %s %s %s\n" % (x_gas, y_gas, vz_gas, vx_gas, vy_gas))

f.close()


### Plots gas on gas x vs y graphs with a vz bar on the same canvas ###
f2 = open('data_gas_bars')
lines = f2.readlines()
f2.close()

gas_x_xy = []
gas_y_xy = []
gas_vz_xy = []
gas_vx_xy = []
gas_vy_xy = []

for line in lines:
	p = line.split()
	gas_x_xy.append(float(p[0]))
	gas_y_xy.append(float(p[1]))
	gas_vz_xy.append(float(p[2]))
	gas_vx_xy.append(float(p[3]))
	gas_vy_xy.append(float(p[4]))

gas_px_xy = np.array(gas_x_xy)
a = gas_px_xy[0::2]						### Change subsampling rate here #########################
gas_py_xy = np.array(gas_y_xy)
b = gas_py_xy[0::2]						### Change subsampling rate here #########################
gas_vz_bar = np.array(gas_vz_xy)
gas_vx_bar = np.array(gas_vx_xy)
gas_vy_bar = np.array(gas_vy_xy)


### Plots the Vz bar graphs ###
plt.subplot(121)
plt.hexbin(gas_px_xy, gas_py_xy, C=gas_vz_bar, cmap=cm.Set1, gridsize=300, vmin=-20, vmax=20)
plt.title('Gas x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 0', fontsize=15)				### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
#cbar = plt.colorbar(fraction=0.046, pad=0.04, orientation='horizontal')
#cbar.set_label('Vz (km/sec)', fontsize=18)
plt.grid()

plt.subplot(122)
plt.hexbin(gas_px_xy, gas_py_xy, C=gas_vz_bar, cmap=cm.Set1, gridsize=300, vmin=-20, vmax=20)
plt.plot(a, b, '.', markersize=3, alpha=0.3)
plt.title('Gas x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 0', fontsize=15)				### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
#cbar = plt.colorbar(fraction=0.046, pad=0.04, orientation='horizontal')
#cbar.set_label('Vz (km/sec)', fontsize=18)
plt.grid()

cax = plt.axes([0.125, 0.075, 0.775, 0.03])
cbar = plt.colorbar(cax = cax, orientation='horizontal')
cbar.set_label('Vz (km/sec)', fontsize=18)

#plt.show()


### Plots the Vx bar graphs ###
plt.subplot(121)
plt.hexbin(gas_px_xy, gas_py_xy, C=gas_vx_bar, cmap=cm.jet_r, gridsize=300)#, vmin=-120, vmax=120)
plt.title('Gas x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 0', fontsize=15)				### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
#cbar = plt.colorbar(fraction=0.046, pad=0.04, orientation='horizontal')
#cbar.set_label('Vx (km/sec)', fontsize=18)
plt.grid()

plt.subplot(122)
plt.hexbin(gas_px_xy, gas_py_xy, C=gas_vx_bar, cmap=cm.jet_r, gridsize=300)#, vmin=-120, vmax=120)
plt.plot(a, b, '.', color='blueviolet', markersize=3, alpha=0.3)
plt.title('Gas x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 0', fontsize=15)				### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
#cbar = plt.colorbar(fraction=0.046, pad=0.04, orientation='horizontal')
#cbar.set_label('Vx (km/sec)', fontsize=18)
plt.grid()

cax = plt.axes([0.125, 0.075, 0.775, 0.03])
cbar = plt.colorbar(cax = cax, orientation='horizontal')
cbar.set_label('Vx (km/sec)', fontsize=18)

plt.show()


### Plots the Vy bar graphs ###
plt.subplot(121)
plt.hexbin(gas_px_xy, gas_py_xy, C=gas_vy_bar, cmap=cm.jet_r, gridsize=300)#, vmin=180, vmax=240)
plt.title('Gas x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 0', fontsize=15)				### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
#cbar = plt.colorbar(fraction=0.046, pad=0.04, orientation='horizontal')
#cbar.set_label('Vy (km/sec)', fontsize=18)
plt.grid()

plt.subplot(122)
plt.hexbin(gas_px_xy, gas_py_xy, C=gas_vy_bar, cmap=cm.jet_r, gridsize=300)#, vmin=180, vmax=240)
plt.plot(a, b, '.', color='blueviolet', markersize=3, alpha=0.3)
plt.title('Gas x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 0', fontsize=15)				### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
#cbar = plt.colorbar(fraction=0.046, pad=0.04, orientation='horizontal')
#cbar.set_label('Vy (km/sec)', fontsize=18)
plt.grid()

cax = plt.axes([0.125, 0.075, 0.775, 0.03])
cbar = plt.colorbar(cax = cax, orientation='horizontal')
cbar.set_label('Vy (km/sec)', fontsize=18)

plt.show()

