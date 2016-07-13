import math 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib as mpl
import glio
s = glio.GadgetSnapshot('snapshot_020')
s.load()


### Produces data to plot star x vs y position graphs with velocity color bars ###
f = open('data_star_bars', 'w')
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
	
	f.write("%s %s %s %s %s\n" % (x_star, y_star, vz_star, vx_star, vy_star))
	
f.close()


### Produces data to plot gas x vs y position graphs with velocity color bars ###
f = open('data_gas_bars', 'w')
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


f2 = open('data_star_bars')
lines = f2.readlines()
f2.close()

star_x = []
star_y = []
star_vz = []
star_vx = []
star_vy = []

for line in lines:
	p = line.split()
	star_x.append(float(p[0]))
	star_y.append(float(p[1]))
	star_vz.append(float(p[2]))
	star_vx.append(float(p[3]))
	star_vy.append(float(p[4]))
	
star_px = np.array(star_x)
star_py = np.array(star_y)
star_vz_bar = np.array(star_vz)
star_vx_bar = np.array(star_vx)
star_vy_bar= np.array(star_vy)

f2 = open('data_gas_bars')
lines = f2.readlines()
f2.close()

gas_x = []
gas_y = []
gas_vz = []
gas_vx = []
gas_vy = []

for line in lines:
	p = line.split()
	gas_x.append(float(p[0]))
	gas_y.append(float(p[1]))
	gas_vz.append(float(p[2]))
	gas_vx.append(float(p[3]))
	gas_vy.append(float(p[4]))
	
gas_px = np.array(gas_x)
gas_py = np.array(gas_y)
gas_vz_bar = np.array(gas_vz)
gas_vx_bar = np.array(gas_vx)
gas_vy_bar= np.array(gas_vy)


### Plots the Vz bar graphs ###
plt.subplot(121)
plt.hexbin(star_px, star_py, C=star_vz_bar, cmap=cm.Set1, gridsize=300, vmin=-20, vmax=20)
plt.title('Star x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 1', fontsize=15)						### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(122)
plt.hexbin(gas_px, gas_py, C=gas_vz_bar, cmap=cm.Set1, gridsize=300, vmin=-20, vmax=20)
plt.title('Gas x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 1', fontsize=15)						### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

cax = plt.axes([0.125, 0.075, 0.775, 0.03])
cbar = plt.colorbar(cax=cax, orientation='horizontal')
cbar.set_label('Vz (km/sec)', fontsize=18)

#plt.show()


### Plots the Vx bar graphs ###
plt.subplot(121)
plt.hexbin(star_px, star_py, C=star_vx_bar, cmap=cm.jet_r, gridsize=300)#, vmin=-120, vmax=120)
plt.title('Star x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 1', fontsize=15)						### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(122)
plt.hexbin(gas_px, gas_py, C=gas_vx_bar, cmap=cm.jet_r, gridsize=300)#, vmin=-120, vmax=120)
plt.title('Gas x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 1', fontsize=15)						### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

cax = plt.axes([0.125, 0.075, 0.775, 0.03])
cbar = plt.colorbar(cax=cax, orientation='horizontal')
cbar.set_label('Vx (km/sec)', fontsize=18)

plt.show()

### Plots the Vy bar graphs ###
plt.subplot(121)
plt.hexbin(star_px, star_py, C=star_vy_bar, cmap=cm.jet_r, gridsize=300)#, vmin=180, vmax=240)
plt.title('Star x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 1', fontsize=15)						### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(122)
plt.hexbin(gas_px, gas_py, C=gas_vy_bar, cmap=cm.jet_r, gridsize=300)#, vmin=180, vmax=240)
plt.title('Gas x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 1', fontsize=15)						### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

cax = plt.axes([0.125, 0.075, 0.775, 0.03])
cbar = plt.colorbar(cax=cax, orientation='horizontal')
cbar.set_label('Vy (km/sec)', fontsize=18)

plt.show()