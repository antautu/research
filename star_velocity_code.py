### Plots vx vs vy, vy vs vz, and vx vs vz star velocity graphs for any snapshot ###
### [4] = Star ###

import numpy as np
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_001')		### Change snapshot here ###
s.load()


### Produces data for the v(x) vs v(y) graph ###
f = open('data_xy','w')
for i in range(0, len(s.vel[4][:])):
	f.write("%s %s\n" % (s.vel[4][i][0],s.vel[4][i][1]))

f.close()


### Produces data for the v(y) vs v(z) graph ###
f = open('data_yz','w')
for i in range(0,len(s.vel[4][:])):
	f.write("%s %s\n" % (s.vel[4][i][1],s.vel[4][i][2]))

f.close()


### Produces data for the v(x) vs v(z) graph ###
f = open('data_xz','w')
for i in range(0,len(s.vel[4][:])):
	f.write("%s %s\n" % (s.vel[4][i][0],s.vel[4][i][2]))

f.close()


### Plots v(x) vs v(y) graph ###
f2 = open('data_xy')
lines = f2.readlines()
f2.close()

x_xy = []
y_xy = []

for line in lines:
	p = line.split()
	x_xy.append(float(p[0]))
	y_xy.append(float(p[1]))

vx_xy = np.array(x_xy)
vy_xy = np.array(y_xy)

plt.plot(vx_xy, vy_xy, '.', markersize=3)
plt.xlabel('v(x)')
plt.ylabel('v(y)')
plt.text(300, 300, 't = 0')			### Make sure to change time label ###
plt.axis([-400, 400, -400, 400])

plt.show()


### Plots v(y) vs v(z) graph ###
f2 = open('data_yz')
lines = f2.readlines()
f2.close()

y_yz = []
z_yz = []

for line in lines:
	p = line.split()
	y_yz.append(float(p[0]))
	z_yz.append(float(p[1]))

vy_yz = np.array(y_yz)
vz_yz = np.array(z_yz)

plt.plot(vy_yz, vz_yz, '.', markersize=3)
plt.xlabel('v(y)')
plt.ylabel('v(z)')
plt.text(300, 300, 't = 0')			### Make sure to change time label ###
plt.axis([-400, 400, -400, 400])

plt.show()


### Plots v(x) vs v(z) graph ###
f2 = open('data_xz')
lines = f2.readlines()
f2.close()

x_xz = []
z_xz = []

for line in lines:
	p = line.split()
	x_xz.append(float(p[0]))
	z_xz.append(float(p[1]))

vx_xz = np.array(x_xz)
vz_xz = np.array(z_xz)

plt.plot(vx_xz, vz_xz, '.', markersize=3)
plt.xlabel('v(x)')
plt.ylabel('v(z)')
plt.text(300, 300, 't = 0')			### Make sure to change time label ###
plt.axis([-400, 400, -400, 400])		

plt.show()