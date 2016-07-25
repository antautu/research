import math
import numpy as np
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_030')					### Change snapshot here ###
s.load()

########## Produces data for x, y, and z gas postion values ##########
f = open('data_disk_xyz', 'w')
for i in range(0, len(s.pos[2][:])):
	f.write("%s %s %s\n" % (s.pos[2][i][0], s.pos[2][i][1], s.pos[2][i][2]))

f.close()


f2 = open('data_disk_xyz')
lines = f2.readlines()
f2.close()

disk_x = []
disk_y = []
disk_z = []


for line in lines:
	p = line.split()
	disk_x.append(float(p[0]))
	disk_y.append(float(p[1]))
	disk_z.append(float(p[2]))

disk_px = np.array(disk_x)
disk_py = np.array(disk_y)
disk_pz = np.array(disk_z)


########## For loops that split up gas z values ##########

### z > 0.5 ###
x_1 = []
y_1 = []

for i in range(len(disk_pz)):
	if disk_pz[i] > 1.5:
		x_1.append(disk_px[i])
		y_1.append(disk_py[i])

x1 = x_1[0::10]
y1 = y_1[0::10]

### 0.5 > z 0.4 ###
x_2 = []
y_2 = []

for i in range(len(disk_pz)):
	if 1.5 > disk_pz[i] > 1.25:
		x_2.append(disk_px[i])
		y_2.append(disk_py[i])

x2 = x_2[0::10]
y2 = y_2[0::10]

### 0.4 > z > 0.3 ###
x_3 = []
y_3 = []

for i in range(len(disk_pz)):
	if 1.25 > disk_pz[i] > 1.0:
		x_3.append(disk_px[i])
		y_3.append(disk_py[i])

x3 = x_3[0::10]
y3 = y_3[0::10]

### 0.3 > z 0.2 ###
x_4 = []
y_4 = []

for i in range(len(disk_pz)):
	if 1.0 > disk_pz[i] > 0.75:
		x_4.append(disk_px[i])
		y_4.append(disk_py[i])

x4 = x_4[0::10]
y4 = y_4[0::10]

### 0.2 > z 0.1 ###
x_5 = []
y_5 = []

for i in range(len(disk_pz)):
	if 0.75 > disk_pz[i] > 0.5:
		x_5.append(disk_px[i])
		y_5.append(disk_py[i])

x5 = x_5[0::10]
y5 = y_5[0::10]

### 0.1 > z > 0.0 ###
x_6 = []
y_6 = []

for i in range(len(disk_pz)):
	if 0.5 > disk_pz[i] > 0.25:
		x_6.append(disk_px[i])
		y_6.append(disk_py[i])

x6 = x_6[0::10]
y6 = y_6[0::10]

### 0.0 > z -0.1 ###
x_7 = []
y_7 = []

for i in range(len(disk_pz)):
	if 0.25 > disk_pz[i] > 0.0:
		x_7.append(disk_px[i])
		y_7.append(disk_py[i])

x7 = x_7[0::10]
y7 = y_7[0::10]

### z < -0.1 ###
x_8 = []
y_8 = []

for i in range(len(disk_pz)):
	if disk_pz[i] < 0.0:
		x_8.append(disk_px[i])
		y_8.append(disk_py[i])

x8 = x_8[0::10]
y8 = y_8[0::10]


########## Plots x vs y gas position graph for specific z values ##########

### z > 0.5 ###
plt.suptitle('Subsampled disk z values for t = 30', fontsize=28)						### Make sure to change time label ### 
plt.subplot(241)
plt.plot(x1, y1, '.', markersize=3, alpha=0.3)
plt.title('z > 1.5', fontsize=18)
plt.xlabel('x (kpc)', fontsize=15)
plt.ylabel('y (kpc)', fontsize=15)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

### 0.5 > z > 0.4 ###
plt.subplot(242)
plt.plot(x2, y2, '.', markersize=3, alpha=0.3)
plt.title('1.5 > z > 1.25', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

### 0.4 > z > 0.3 ###
plt.subplot(243)
plt.plot(x3, y3, '.', markersize=3, alpha=0.3)
plt.title('1.25 > z > 1.0', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

### 0.3 > z > 0.2 ###
plt.subplot(244)
plt.plot(x4, y4, '.', markersize=3, alpha=0.3)
plt.title('1.0 > z > 0.75', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

### 0.2 > z > 0.1 ###
plt.subplot(245)
plt.plot(x5, y5, '.', markersize=3, alpha=0.3)
plt.title('0.75 > z > 0.5', fontsize=18)
plt.xlabel('x (kpc)', fontsize=15)
plt.ylabel('y (kpc)', fontsize=15)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

### 0.1 > z > 0.0 ###
plt.subplot(246)
plt.plot(x6, y6, '.', markersize=3, alpha=0.3)
plt.title('0.5 > z > 0.25', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

### 0.0 > z > -0.1 ###
plt.subplot(247)
plt.plot(x7, y7, '.', markersize=3, alpha=0.3)
plt.title('0.25 > z > 0.0', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

### z < -0.1 ###
plt.subplot(248)
plt.plot(x8, y8, '.', markersize=3, alpha=0.3)
plt.title('z < 0.0', fontsize=18)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')

plt.show()