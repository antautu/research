### Plots star and gas position graphs next to eachother for any snapshot ###
### [0] = Gas ###
### [4] = Star ###

import numpy as np
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_020')
s.load()

### Produces data for the gas x vs y graph ###
#f = open('data_gas_xy','w')
#for i in range(0, len(s.pos[0][:])):
#	f.write("%s %s\n" % (s.pos[0][i][0],s.pos[0][i][1]))
		
#f.close()
		
		
### Produces data for the star x vs y graph ###
f = open('data_star_xy','w')
for i in range(0, len(s.pos[4][:])):
	f.write("%s %s\n" % (s.pos[4][i][0],s.pos[4][i][1]))
		
f.close()


#### Produces data for the disk x vs y graph ###
f = open('data_disk_xy', 'w')
for i in range(0, len(s.pos[2][:])):
	f.write("%s %s\n" % (s.pos[2][i][0],s.pos[2][i][1]))

f.close()
		
		
### Plots star and gas x vs y graphs on the same canvas ###
f2 = open('data_star_xy')
lines = f2.readlines()
f2.close()
		
star_x_xy = []
star_y_xy = []
		
for line in lines:
	p = line.split()
	star_x_xy.append(float(p[0]))
	star_y_xy.append(float(p[1]))
		
star_px_xy = np.array(star_x_xy)
a = star_px_xy[0::8]				### [0::n] starts from beginning and then takes steps of size n ###
star_py_xy = np.array(star_y_xy)
b = star_py_xy[0::8]
		
#f2 = open('data_gas_xy')
#lines = f2.readlines()
#f2.close()
		
#gas_x_xy = []
#gas_y_xy = []
		
#for line in lines:
#	p = line.split()
#	gas_x_xy.append(float(p[0]))
#	gas_y_xy.append(float(p[1]))
		
#gas_px_xy = np.array(gas_x_xy)
#c = gas_px_xy[0::2]
#gas_py_xy = np.array(gas_y_xy)
#d = gas_py_xy[0::2]


f2 = open('data_disk_xy')
lines = f2.readlines()
f2.close()

disk_x_xy = []
disk_y_xy = []

for line in lines:
	p = line.split()
	disk_x_xy.append(float(p[0]))
	disk_y_xy.append(float(p[1]))

disk_px_xy = np.array(disk_x_xy)
c = disk_px_xy[0::10]
disk_py_xy = np.array(disk_y_xy)
d = disk_py_xy[0::10]

		
		
plt.subplot(121)
plt.plot(a, b, '.', markersize=3, alpha=0.3)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.title('Star x vs y Subsampled', fontsize=22)
plt.text(20, 20, 't = 20', fontsize=20)					### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
		
plt.subplot(122)
plt.plot(c, d, '.', markersize=3, alpha=0.3)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
#plt.title('Gas x vs y Subsampled', fontsize = 22)
plt.title('Disk x vs y Subsampled', fontsize=22)
plt.text(20, 20, 't = 20', fontsize=20)					### Make sure to change time label ###
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
		
plt.show()
