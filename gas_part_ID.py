import math 
import numpy as np
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_040')
s.load()

#f = open('data_gas_part_ID', 'w')
#for i in range(0, len(s.ID[0][:])):
#	f.write("%s\n" % s.ID[0][i])

#f.close()

#part_ID = open('data_gas_part_ID')
#lines = part_ID.readlines()
#lines.sort(key=int)
#print lines

#f = open('sorted_part_ID', 'w')
#for line in lines:
#	f.write("%s" % line)

#f.close()

f = open('data_gas_x', 'w')
for i in range(0, len(s.pos[0][:])):
	f.write("%s %s\n" % (s.pos[0][i][0], s.pos[0][i][1]))

f.close()

f2 = open('data_gas_xy')
lines = f2.readlines()
f2.close()

gas_x = []
gas_y = []

for line in lines:
	p = line.split()
	gas_x.append(float(p[0]))
	gas_y.append(float(p[1]))

gas_px = np.array(gas_x)
a = gas_px[0:90000]

gas_py = np.array(gas_y)
b = gas_py[0:90000]






sorted = open('data_gas_xy')
lines = sorted.readlines()
lines.sort()

f = open('sorted_gas_xy', 'w')
for line in lines:
	f.write("%s" % line)

f.close()

f2 = open('sorted_gas_xy')
lines = f2.readlines()
f2.close()

gas_x_sort = []
gas_y_sort = []

for line in lines:
	p = line.split()
	gas_x_sort.append(float(p[0]))
	gas_y_sort.append(float(p[1]))

gas_px_sort = np.array(gas_x_sort)
c = gas_px_sort[0:60000]

gas_py_sort = np.array(gas_y_sort)
d = gas_py_sort[0:60000]






#plt.subplot(121)
#plt.plot(gas_px, gas_py, '.', markersize=3)

#plt.subplot(122)
#plt.plot(gas_px_sort, gas_py_sort, '.', markersize=3)
#plt.show()

plt.subplot(121)
plt.plot(a, b, '.', markersize=3)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(122)
plt.plot(c, d, '.', markersize=3)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

plt.show()

