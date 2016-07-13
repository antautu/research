import math
import numpy as np
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_010')
s.load()


f = open('data_gas_xyz', 'w')
for i in range(0, len(s.pos[0][:])):
	f.write("%s %s %s\n" % (s.pos[0][i][0], s.pos[0][i][1], s.pos[0][i][2]))

f.close()


f2 = open('data_gas_xyz')
lines = f2.readlines()
f2.close()

gas_x = []
gas_y = []
gas_z = []

for line in lines:
	p = line.split()
	gas_x.append(float(p[0]))
	gas_y.append(float(p[1]))
	gas_z.append(float(p[2]))

gas_px = np.array(gas_x)
gas_py = np.array(gas_y)
gas_pz = np.array(gas_y)


x = []
y = []

for i in range(len(gas_pz)):
	if gas_pz > 0.5:
		x.append[gas_px[i]]
		y.append[gas_py[i]]

plt.plot(x, y)
plt.show()