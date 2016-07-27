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
#gas_px[:] = [x - # for x in gas_px]			### Not sure if needed in z slices ###
#gas_py[:] = [y - # for y in gas_py]			### Not sure if needed in z slices ###
gas_pz[:] = [z - 1.235 for z in gas_pz]


########## For loop that splits up gas z values ##########

sub = 2						### Sets the subsample rate ###

### z > 0.3 ###
x1 = []
y1 = []

for i in range(len(gas_pz)):
	if gas_pz[i] > 0.3:
		x1.append(gas_px[i])
		y1.append(gas_py[i])

x1_sub = x1[0::sub]
y1_sub = y1[0::sub]

### 0.3 > z 0.2 ###
x2 = []
y2 = []

for i in range(len(gas_pz)):
	if 0.3 > gas_pz[i] > 0.2:
		x2.append(gas_px[i])
		y2.append(gas_py[i])

x2_sub = x2[0::sub]
y2_sub = y2[0::sub]

### 0.2 > z > 0.1 ###
x3 = []
y3 = []

for i in range(len(gas_pz)):
	if 0.2 > gas_pz[i] > 0.1:
		x3.append(gas_px[i])
		y3.append(gas_py[i])

x3_sub = x3[0::sub]
y3_sub = y3[0::sub]

### 0.1 > z 0.0 ###
x4 = []
y4 = []

for i in range(len(gas_pz)):
	if 0.1 > gas_pz[i] > 0.0:
		x4.append(gas_px[i])
		y4.append(gas_py[i])

x4_sub = x4[0::sub]
y4_sub = y4[0::sub]

### 0.0 > z -0.1 ###
x5 = []
y5 = []

for i in range(len(gas_pz)):
	if 0.0 > gas_pz[i] > -0.1:
		x5.append(gas_px[i])
		y5.append(gas_py[i])

x5_sub = x5[0::sub]
y5_sub = y5[0::sub]

### -0.1 > z > -0.2 ###
x6 = []
y6 = []

for i in range(len(gas_pz)):
	if -0.1 > gas_pz[i] > -0.2:
		x6.append(gas_px[i])
		y6.append(gas_py[i])

x6_sub = x6[0::sub]
y6_sub = y6[0::sub]

### -0.2 > z -0.3 ###
x7 = []
y7 = []

for i in range(len(gas_pz)):
	if -0.2 > gas_pz[i] > -0.3:
		x7.append(gas_px[i])
		y7.append(gas_py[i])

x7_sub = x7[0::sub]
y7_sub = y7[0::sub]

### z < -0.3 ###
x8 = []
y8 = []

for i in range(len(gas_pz)):
	if gas_pz[i] < -0.3:
		x8.append(gas_px[i])
		y8.append(gas_py[i])

x8_sub = x8[0::sub]
y8_sub = y8[0::sub]


########## Plots x vs y gas position graph for specific z values ##########

### z > 0.3 ###
plt.suptitle('Subsampled gas z values for t = 40', fontsize=28)							### Make sure to change time label ###
plt.subplot(241)
plt.plot(x1_sub, y1_sub, '.', markersize=3, alpha=0.3)
plt.title('z > 0.3', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

### 0.3 > z > 0.2 ###
plt.subplot(242)
plt.plot(x2_sub, y2_sub, '.', markersize=3, alpha=0.3)
plt.title('0.3 > z > 0.2', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

### 0.2 > z > 0.1 ###
plt.subplot(243)
plt.plot(x3_sub, y3_sub, '.', markersize=3, alpha=0.3)
plt.title('0.2 > z > 0.1', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

### 0.1 > z > 0.0 ###
plt.subplot(244)
plt.plot(x4_sub, y4_sub, '.', markersize=3, alpha=0.3)
plt.title('0.1 > z > 0.0', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

### 0.0 > z > -0.1 ###
plt.subplot(245)
plt.plot(x5_sub, y5_sub, '.', markersize=3, alpha=0.3)
plt.title('0.0 > z > -0.1', fontsize=18)
plt.text(-35, 37, 'y (kpc)', fontsize=22, rotation='vertical')
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

### -0.1 > z > -0.2 ###
plt.subplot(246)
plt.plot(x6_sub, y6_sub, '.', markersize=3, alpha=0.3)
plt.title('-0.1 > z > -0.2', fontsize=18)
plt.text(25, -35, 'x (kpc)', fontsize=22)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

### -0.2 > z > -0.3 ###
plt.subplot(247)
plt.plot(x7_sub, y7_sub, '.', markersize=3, alpha=0.3)
plt.title('-0.2 > z > -0.3', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

### z < -0.3 ###
plt.subplot(248)
plt.plot(x8_sub, y8_sub, '.', markersize=3, alpha=0.3)
plt.title('z < -0.3', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.show()