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
 	 
 	f.write("%s %s %s %s %s\n" % (x_star, y_star, vz_star, vr_star, vtheta_star)) 
 	 
 	 
f.close() 

f2 = open('data_star_bars') 
lines = f2.readlines() 
f2.close() 
 
 
star_x = [] 
star_y = [] 
star_vz = [] 
star_vr = [] 
star_vtheta = [] 
 
 
for line in lines: 
 	p = line.split() 
 	star_x.append(float(p[0])) 
 	star_y.append(float(p[1])) 
 	star_vz.append(float(p[2])) 
 	star_vr.append(float(p[3])) 
 	star_vtheta.append(float(p[4])) 
 	 
star_px = np.array(star_x) 
a = star_px[0::4]									### Change subsample rate here ###
star_py = np.array(star_y) 
b = star_py[0::4]									### Change subsample rate here ###
star_vz_bar = np.array(star_vz) 
star_vr_bar = np.array(star_vr) 
star_vtheta_bar= np.array(star_vtheta) 


### Plots the Vz bar graphs ### 
plt.subplot(121) 
plt.hexbin(star_px, star_py, C=star_vz_bar, cmap=cm.Set1, gridsize=300, vmin=-20, vmax=20) 
plt.title('Star x vs y', fontsize=22) 
plt.xlabel('x (kpc)', fontsize=18) 
plt.ylabel('y (kpc)', fontsize=18) 
plt.text(20, 20, 't = 20', fontsize=15)				### Make sure to change time label ### 
plt.axis([-25, 25, -25, 25]) 
plt.gca().set_aspect('equal', adjustable='box') 
plt.grid() 

plt.subplot(122)
plt.hexbin(star_px, star_py, C=star_vz_bar, cmap=cm.Set1, gridsize=300, vmin=-20, vmax=20)
plt.plot(a, b, '.', markersize=3, alpha=0.3)
plt.title('Star x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 20', fontsize=15)				### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

cax = plt.axes([0.125, 0.075, 0.775, 0.03])
cbar = plt.colorbar(cax = cax, orientation='horizontal')
cbar.set_label('Vz (km/sec)', fontsize=18)

plt.show()


### Plots the Vr bar graphs ### 
plt.subplot(121) 
plt.hexbin(star_px, star_py, C=star_vr_bar, cmap=cm.Set1, gridsize=300, vmin=-120, vmax=120) 
plt.title('Star x vs y', fontsize=22) 
plt.xlabel('x (kpc)', fontsize=18) 
plt.ylabel('y (kpc)', fontsize=18) 
plt.text(20, 20, 't = 20', fontsize=15)				### Make sure to change time label ### 
plt.axis([-25, 25, -25, 25]) 
plt.gca().set_aspect('equal', adjustable='box') 
plt.grid() 

plt.subplot(122)
plt.hexbin(star_px, star_py, C=star_vr_bar, cmap=cm.Set1, gridsize=300, vmin=-120, vmax=120)
plt.plot(a, b, '.', markersize=3, alpha=0.3)
plt.title('Star x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 20', fontsize=15)				### Make sure to change time label ### 
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

cax = plt.axes([0.125, 0.075, 0.775, 0.03])
cbar = plt.colorbar(cax = cax, orientation='horizontal')
cbar.set_label('Vr (km/sec)', fontsize=18)

plt.show()


### Plots the Vtheta bar graphs ### 
plt.subplot(121) 
plt.hexbin(star_px, star_py, C=star_vtheta_bar, cmap=cm.jet_r, gridsize=300, vmin=180, vmax=240) 
plt.title('Star x vs y', fontsize=22) 
plt.xlabel('x (kpc)', fontsize=18) 
plt.ylabel('y (kpc)', fontsize=18) 
plt.text(20, 20, 't = 20', fontsize=15)				### Make sure to change time label ### 
plt.axis([-25, 25, -25, 25]) 
plt.gca().set_aspect('equal', adjustable='box') 
plt.grid() 

plt.subplot(122)
plt.hexbin(star_px, star_py, C=star_vtheta_bar, cmap=cm.jet_r, gridsize=300, vmin=180, vmax=240)
plt.plot(a, b, '.', color='blueviolet', markersize=3, alpha=0.3)
plt.title('Star x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 20', fontsize=15)				### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

cax = plt.axes([0.125, 0.075, 0.775, 0.03])
cbar = plt.colorbar(cax = cax, orientation='horizontal')
cbar.set_label('Vtheta (km/sec)', fontsize=18)

plt.show()