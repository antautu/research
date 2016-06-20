### Produces a 3D plot of any snapshot ###

import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_020')
s.load()


f = open('data_xyz','w')
for i in range(0, len(s.pos[0][:])):
	f.write("%s %s %s\n" % (s.pos[0][i][0], s.pos[0][i][1], s.pos[0][i][2]))

f.close()


f2 = open('data_xyz')
lines = f2.readlines()
f2.close()

x_xyz = []
y_xyz = []
z_xyz = []

for line in lines:
	p = line.split()
	x_xyz.append(float(p[0]))
	y_xyz.append(float(p[1]))
	z_xyz.append(float(p[2]))

vx_xyz = np.array(x_xyz)
vy_xyz = np.array(y_xyz)
vz_xyz = np.array(z_xyz)

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot(vx_xyz, vy_xyz, vz_xyz, '.', markersize=3)

plt.show()