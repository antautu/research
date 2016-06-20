### Plots  x vs y, y vs z, and x vs z star position graphs for any snapshot ###
### [4] = Star ###

import numpy as np
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_001')		### Change snapshot here ###
s.load()


### Produces data for the x vs y graph ###
f = open('data_xy','w')
for i in range(0, len(s.pos[4][:])):
	f.write("%s %s\n" % (s.pos[4][i][0],s.pos[4][i][1]))

f.close()


### Produces data for the y vs z graph ###
f = open('data_yz','w')
for i in range(0,len(s.pos[4][:])):
	f.write("%s %s\n" % (s.pos[4][i][1],s.pos[4][i][2]))

f.close()


### Produces data for the x vs z graph ###
f = open('data_xz','w')
for i in range(0,len(s.pos[4][:])):
	f.write("%s %s\n" % (s.pos[4][i][0],s.pos[4][i][2]))

f.close()


### Plots x vs y graph ###
f2 = open('data_xy')
lines = f2.readlines()
f2.close()

x_xy = []
y_xy = []

for line in lines:
	p = line.split()
	x_xy.append(float(p[0]))
	y_xy.append(float(p[1]))

px_xy = np.array(x_xy)
py_xy = np.array(y_xy)

plt.plot(px_xy, py_xy, '.', markersize=3, alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.text(15, 15, 't = 40')			### Make sure to change time label ###
plt.axis([-20, 20, -20, 20])

plt.show()


### Plots y vs z graph ###
f2 = open('data_yz')
lines = f2.readlines()
f2.close()

y_yz = []
z_yz = []

for line in lines:
	p = line.split()
	y_yz.append(float(p[0]))
	z_yz.append(float(p[1]))

py_yz = np.array(y_yz)
pz_yz = np.array(z_yz)

plt.plot(py_yz, pz_yz, '.', markersize=3, alpha=0.3)
plt.xlabel('y')
plt.ylabel('z')
plt.text(15, 3, 't = 40')			### Make sure to change time label ###
plt.axis([-20, 20, -4, 4])

plt.show()


### Plots x vs z graph ###
f2 = open('data_xz')
lines = f2.readlines()
f2.close()

x_xz = []
z_xz = []

for line in lines:
	p = line.split()
	x_xz.append(float(p[0]))
	z_xz.append(float(p[1]))

px_xz = np.array(x_xz)
pz_xz = np.array(z_xz)

plt.plot(px_xz, pz_xz, '.', markersize=3,alpha=3)
plt.xlabel('x')
plt.ylabel('z')
plt.text(15, 3, 't = 40')			### Make sure to change time label ###		
plt.axis([-20, 20, -4, 4])

plt.show()