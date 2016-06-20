### Plots 3 position graphs to compare x vs y, y vs z, and x vs z in star and gas for any snapshot ###
### [0] = Gas ###
### [4] = Star ###

import numpy as np
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_040')		### Change snapshot here ###
s.load()


### Produces data for the gas x vs y graph ###
f = open('data_gas_xy','w')
for i in range(0, len(s.pos[0][:])):
	f.write("%s %s\n" % (s.pos[0][i][0],s.pos[0][i][1]))

f.close()


### Produces data for the gas y vs z graph ###
f = open('data_gas_yz','w')
for i in range(0,len(s.pos[0][:])):
	f.write("%s %s\n" % (s.pos[0][i][1],s.pos[0][i][2]))

f.close()


### Produces data for the gas x vs z graph ###
f = open('data_gas_xz','w')
for i in range(0,len(s.pos[0][:])):
	f.write("%s %s\n" % (s.pos[0][i][0],s.pos[0][i][2]))

f.close()

### Produces data for the star x vs y graph ###
f = open('data_star_xy','w')
for i in range(0, len(s.pos[4][:])):
	f.write("%s %s\n" % (s.pos[4][i][0],s.pos[4][i][1]))

f.close()


### Produces data for the star y vs z graph ###
f = open('data_star_yz','w')
for i in range(0,len(s.pos[4][:])):
	f.write("%s %s\n" % (s.pos[4][i][1],s.pos[4][i][2]))

f.close()


### Produces data for the star x vs z graph ###
f = open('data_star_xz','w')
for i in range(0,len(s.pos[4][:])):
	f.write("%s %s\n" % (s.pos[4][i][0],s.pos[4][i][2]))

f.close()


### Plots star x vs y graph ###
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
star_py_xy = np.array(star_y_xy)

f2 = open('data_gas_xy')
lines = f2.readlines()
f2.close()

gas_x_xy = []
gas_y_xy = []

for line in lines:
	p = line.split()
	gas_x_xy.append(float(p[0]))
	gas_y_xy.append(float(p[1]))

gas_px_xy = np.array(gas_x_xy)
gas_py_xy = np.array(gas_y_xy)


plt.subplot(121)
plt.plot(star_px_xy, star_py_xy, '.', markersize=3, alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Star x vs y')
plt.text(15, 15, 't = 40')			### Make sure to change time label ###
plt.axis([-20, 20, -20, 20])

plt.subplot(122)
plt.plot(gas_px_xy, gas_py_xy, '.', markersize=3, alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gas x vs y')
plt.text(20, 20, 't = 40')			### Make sure to change time label ###
plt.axis([-30, 30, -30, 30])

plt.show()


### Plots y vs z graph ###
f2 = open('data_star_yz')
lines = f2.readlines()
f2.close()

star_y_yz = []
star_z_yz = []

for line in lines:
	p = line.split()
	star_y_yz.append(float(p[0]))
	star_z_yz.append(float(p[1]))

star_py_yz = np.array(star_y_yz)
star_pz_yz = np.array(star_z_yz)

f2 = open('data_gas_yz')
lines = f2.readlines()
f2.close()

gas_y_yz = []
gas_z_yz = []

for line in lines:
	p = line.split()
	gas_y_yz.append(float(p[0]))
	gas_z_yz.append(float(p[1]))

gas_py_yz = np.array(gas_y_yz)
gas_pz_yz = np.array(gas_z_yz)


plt.subplot(121)
plt.plot(star_py_yz, star_pz_yz, '.', markersize=3, alpha=0.3)
plt.xlabel('y')
plt.ylabel('z')
plt.title('Star y vs z')
plt.text(15, 3, 't = 40')			### Make sure to change time label ###
plt.axis([-20, 20, -4, 4])

plt.subplot(122)
plt.plot(gas_py_yz, gas_pz_yz, '.', markersize=3, alpha=0.3)
plt.xlabel('y')
plt.ylabel('z')
plt.title('Gas y vs z')
plt.text(20, 3, 't = 40')			### Make sure to change time label ###
plt.axis([-30, 30, -4, 4])

plt.show()


### Plots x vs z graph ###
f2 = open('data_star_xz')
lines = f2.readlines()
f2.close()

star_x_xz = []
star_z_xz = []

for line in lines:
	p = line.split()
	star_x_xz.append(float(p[0]))
	star_z_xz.append(float(p[1]))

star_px_xz = np.array(star_x_xz)
star_pz_xz = np.array(star_z_xz)

f2 = open('data_gas_xz')
lines = f2.readlines()
f2.close()

gas_x_xz = []
gas_z_xz = []

for line in lines:
	p = line.split()
	gas_x_xz.append(float(p[0]))
	gas_z_xz.append(float(p[1]))

gas_px_xz = np.array(gas_x_xz)
gas_pz_xz = np.array(gas_z_xz)

plt.subplot(121)
plt.plot(star_px_xz, star_pz_xz, '.', markersize=3,alpha=0.3)
plt.xlabel('x')
plt.ylabel('z')
plt.title('Star x vs z')
plt.text(15, 3, 't = 40')			### Make sure to change time label ###		
plt.axis([-20, 20, -4, 4])

plt.subplot(122)
plt.plot(gas_px_xz, gas_pz_xz, '.', markersize=0.3)
plt.xlabel('x')
plt.ylabel('z')
plt.title('Gas x vs z')
plt.text(20, 3, 't = 40')			### Make sure to change time label ###		
plt.axis([-30, 30, -4, 4])

plt.show()