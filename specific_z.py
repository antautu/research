import math
import numpy as np
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_010')
s.load()


### Produces data for gas x values ###
f = open('data_gas_x', 'w')
for i in range(0, len(s.pos[0][:])):
	f.write("%s\n" % s.pos[0][i][0])

f.close()

f2 = open('data_gas_x')
lines = f2.readlines()
f2.close()

gas_x = []

gas_px = np.array(gas_x)


### Produces data for gas y values ###
f = open('data_gas_y', 'w')
for i in range(0, len(s.pos[0][:])):
	f.write("%s\n" % s.pos[0][i][1])

f.close()

f2 = open('data_gas_y')
lines = f2.readlines()
f2.close()

gas_y = []

gas_py = np.array(gas_y)


### Produces data for gas z values ###
f = open('data_gas_z', 'w')
for i in range(0, len(s.pos[0][:])):
	f.write("%s\n" % s.pos[0][i][2])

f.close()

f2 = open('data_gas_z')
lines = f2.readlines()
f2.close()

gas_z = []

gas_pz = np.array(gas_z)


### For loop that chooses x and y values for specific values of z ###
x = []
y = []

for i in range(len(gas_pz)):
	if gas_pz > 0.5:
		x.append[gas_px[i]]
		y.append[gas_py[i]]

x_new = np.array(x)
y_new = np.array(y)

plt.plot(x_new, y_new)
plt.show()