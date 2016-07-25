import math
import numpy as np
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_000')					### Change snapshot here ###
s.load()

########## Produces data for x, y, and z gas postion values ##########
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
gas_pz = np.array(gas_z)


########## For loops that split up gas z values ##########

### z > 0.3 ###
x_1 = []
y_1 = []

for i in range(len(gas_pz)):
	if gas_pz[i] > 0.3:
		x_1.append(gas_px[i])
		y_1.append(gas_py[i])

x1 = x_1[0::8]
y1 = y_1[0::8]

### 0.3 > z 0.2 ###
x_2 = []
y_2 = []

for i in range(len(gas_pz)):
	if 0.3 > gas_pz[i] > 0.2:
		x_2.append(gas_px[i])
		y_2.append(gas_py[i])

x2 = x_2[0::8]
y2 = y_2[0::8]

### 0.2 > z > 0.1 ###
x_3 = []
y_3 = []

for i in range(len(gas_pz)):
	if 0.2 > gas_pz[i] > 0.1:
		x_3.append(gas_px[i])
		y_3.append(gas_py[i])

x3 = x_3[0::8]
y3 = y_3[0::8]

### 0.1 > z 0.0 ###
x_4 = []
y_4 = []

for i in range(len(gas_pz)):
	if 0.1 > gas_pz[i] > 0.0:
		x_4.append(gas_px[i])
		y_4.append(gas_py[i])

x4 = x_4[0::8]
y4 = y_4[0::8]

### 0.0 > z -0.1 ###
x_5 = []
y_5 = []

for i in range(len(gas_pz)):
	if 0.0 > gas_pz[i] > -0.1:
		x_5.append(gas_px[i])
		y_5.append(gas_py[i])

x5 = x_5[0::8]
y5 = y_5[0::8]

### -0.1 > z > -0.2 ###
x_6 = []
y_6 = []

for i in range(len(gas_pz)):
	if -0.1 > gas_pz[i] > -0.2:
		x_6.append(gas_px[i])
		y_6.append(gas_py[i])

x6 = x_6[0::8]
y6 = y_6[0::8]

### -0.2 > z -0.3 ###
x_7 = []
y_7 = []

for i in range(len(gas_pz)):
	if -0.2 > gas_pz[i] > -0.3:
		x_7.append(gas_px[i])
		y_7.append(gas_py[i])

x7 = x_7[0::8]
y7 = y_7[0::8]

### z < -0.3 ###
x_8 = []
y_8 = []

for i in range(len(gas_pz)):
	if gas_pz[i] < -0.3:
		x_8.append(gas_px[i])
		y_8.append(gas_py[i])

x8 = x_8[0::8]
y8 = y_8[0::8]


########## Plots x vs y gas position graph for specific z values ##########

### z > 0.3 ###
plt.suptitle('Subsampled z values for t = 0', fontsize=28)						### Make sure to change time label ### 
plt.subplot(241)
plt.plot(x1, y1, '.', markersize=3, alpha=0.3)
plt.title('z > 0.3', fontsize=18)
plt.xlabel('x (kpc)', fontsize=15)
plt.ylabel('y (kpc)', fontsize=15)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

### 0.3 > z > 0.2 ###
plt.subplot(242)
plt.plot(x2, y2, '.', markersize=3, alpha=0.3)
plt.title('0.3 > z > 0.2', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

### 0.2 > z > 0.1 ###
plt.subplot(243)
plt.plot(x3, y3, '.', markersize=3, alpha=0.3)
plt.title('0.2 > z > 0.1', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

### 0.1 > z > 0.0 ###
plt.subplot(244)
plt.plot(x4, y4, '.', markersize=3, alpha=0.3)
plt.title('0.1 > z > 0.0', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

### 0.0 > z > -0.1 ###
plt.subplot(245)
plt.plot(x5, y5, '.', markersize=3, alpha=0.3)
plt.title('0.0 > z > -0.1', fontsize=18)
plt.xlabel('x (kpc)', fontsize=15)
plt.ylabel('y (kpc)', fontsize=15)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

### -0.1 > z > -0.2 ###
plt.subplot(246)
plt.plot(x6, y6, '.', markersize=3, alpha=0.3)
plt.title('-0.1 > z > -0.2', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

### -0.2 > z > -0.3 ###
plt.subplot(247)
plt.plot(x7, y7, '.', markersize=3, alpha=0.3)
plt.title('-0.2 > z > -0.3', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

### z < -0.3 ###
plt.subplot(248)
plt.plot(x8, y8, '.', markersize=3, alpha=0.3)
plt.title('z < -0.3', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

plt.show()