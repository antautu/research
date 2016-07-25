import numpy as np
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_040')
s.load()

########## Produces data for x, y, and z gas position values ##########
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

########## Subtract densest value to center data ##########
gas_px[:] = [x - -0.347 for x in gas_px]
gas_py[:] = [y - 4.741 for y in gas_py]
gas_pz[:] = [z - 1.235 for z in gas_pz]


########## For loop that splits up gas z values ##########

### z > 0.3 ###
x1 = []
y1 = []

for i in range(len(gas_pz)):
	if gas_pz[i] > 0.3:
		x1.append(gas_px[i])
		y1.append(gas_py[i])

### 0.3 > z 0.2 ###
x2 = []
y2 = []

for i in range(len(gas_pz)):
	if 0.3 > gas_pz[i] > 0.2:
		x2.append(gas_px[i])
		y2.append(gas_py[i])

### 0.2 > z > 0.1 ###
x3 = []
y3 = []

for i in range(len(gas_pz)):
	if 0.2 > gas_pz[i] > 0.1:
		x3.append(gas_px[i])
		y3.append(gas_py[i])

### 0.1 > z 0.0 ###
x4 = []
y4 = []

for i in range(len(gas_pz)):
	if 0.1 > gas_pz[i] > 0.0:
		x4.append(gas_px[i])
		y4.append(gas_py[i])

### 0.0 > z -0.1 ###
x5 = []
y5 = []

for i in range(len(gas_pz)):
	if 0.0 > gas_pz[i] > -0.1:
		x5.append(gas_px[i])
		y5.append(gas_py[i])

### -0.1 > z > -0.2 ###
x6 = []
y6 = []

for i in range(len(gas_pz)):
	if -0.1 > gas_pz[i] > -0.2:
		x6.append(gas_px[i])
		y6.append(gas_py[i])

### -0.2 > z -0.3 ###
x7 = []
y7 = []

for i in range(len(gas_pz)):
	if -0.2 > gas_pz[i] > -0.3:
		x7.append(gas_px[i])
		y7.append(gas_py[i])

### z < -0.3 ###
x8 = []
y8 = []

for i in range(len(gas_pz)):
	if gas_pz[i] < -0.3:
		x8.append(gas_px[i])
		y8.append(gas_py[i])


########## Plots x vs y gas position graph for specific z values ##########

### z > 0.3 ###
plt.suptitle('Specific z values for t = 1', fontsize=28)					### Make sure to change time label ###
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