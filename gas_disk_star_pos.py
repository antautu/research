import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import glio
s = glio.GadgetSnapshot('snapshot_010')						### Change snapshot here ###
s.load()


########## Subsample Rates ##########
disk_sub = 6
gas_sub = 6
star_sub = 6


#################### DISK ####################
########## Produces data for the x, y, and z position values for the disk ##########
f = open('data_disk_xyz', 'w')
for i in range(0, len(s.pos[2][:])):
	f.write("%s %s %s\n" % (s.pos[2][i][0], s.pos[2][i][1], s.pos[2][i][2]))

f.close()


########## Produces data for the mass of the disk particles ##########
f = open('data_disk_mass', 'w')
for i in range(0, len(s.mass[2][:])):
	f.write("%s\n" % s.mass[2][i])

f.close()


########## Sets up the  x, y, and z postion arrays ##########
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

disk_xm = np.array(disk_x)
disk_ym = np.array(disk_y)
disk_zm = np.array(disk_z)


########## Sets up the mass array ##########
f2 = open('data_disk_mass')
lines = f2.readlines()
f2.close()

disk_mass = []

for line in lines:
	p = line.split()
	disk_mass.append(float(p[0]))

disk_m = np.array(disk_mass)


########## Find the center of mass in all directions ##########
disk_xm[:] = [x * (8.76209*(10**-6)) for x in disk_xm]
disk_xm_sum = sum(disk_xm)

disk_ym[:] = [y * (8.76209*(10**-6)) for y in disk_ym]
disk_ym_sum = sum(disk_ym)

disk_zm[:] = [z * (8.76209*(10**-6)) for z in disk_zm]
disk_zm_sum = sum(disk_zm)

disk_mass_sum = sum(disk_m)

com_x = disk_xm_sum / disk_mass_sum
#print com_x

com_y = disk_ym_sum / disk_mass_sum
#print com_y

com_z = disk_zm_sum / disk_mass_sum
#print com_z


########## Centers the values by subtracting the center of mass ##########
disk_centered_x = np.array(disk_x)
disk_centered_y = np.array(disk_y)
disk_centered_z = np.array(disk_z)

disk_centered_x[:] = [x - com_x for x in disk_centered_x]
disk_sub_x = disk_centered_x[0::disk_sub]
disk_centered_y[:] = [y - com_y for y in disk_centered_y]
disk_sub_y = disk_centered_y[0::disk_sub]
disk_centered_z[:] = [z - com_z for z in disk_centered_z]


########## GAS ##########
########## Produces data for the x, y, and z position values for the gas ##########
f = open('data_gas_xyz', 'w')
for i in range(0, len(s.pos[0][:])):
	f.write("%s %s %s\n" % (s.pos[0][i][0], s.pos[0][i][1], s.pos[0][i][2]))

f.close()


########## Produces data for the mass of the gas particles ##########
f = open('data_gas_mass', 'w')
for i in range(0, len(s.mass[0][:])):
	f.write("%s\n" % s.mass[0][i])

f.close()


########## Sets up the  x, y, and z postion arrays for the gas ##########
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

gas_xm = np.array(gas_x)
gas_ym = np.array(gas_y)
gas_zm = np.array(gas_z)


########## Centers the values by subtracting the center of mass ##########
gas_centered_x = np.array(gas_x)
gas_centered_y = np.array(gas_y)
gas_centered_z = np.array(gas_z)

gas_centered_x[:] = [x - com_x for x in gas_centered_x]
gas_sub_x = gas_centered_x[0::gas_sub]
gas_centered_y[:] = [y - com_y for y in gas_centered_y]
gas_sub_y = gas_centered_y[0::gas_sub]
gas_centered_z[:] = [z - com_z for z in gas_centered_z]


########## STAR ##########
########## Produces data for the x, y, and z position values for the stars ##########
f = open('data_star_xyz', 'w')
for i in range(0, len(s.pos[4][:])):
	f.write("%s %s %s\n" % (s.pos[4][i][0], s.pos[4][i][1], s.pos[4][i][2]))

f.close()


########## Produces data for the mass of the star particles ##########
f = open('data_star_mass', 'w')
for i in range(0, len(s.mass[4][:])):
	f.write("%s\n" % s.mass[4][i])

f.close()


########## Sets up the  x, y, and z postion arrays for the stars ##########
f2 = open('data_star_xyz')
lines = f2.readlines()

f2.close()

star_x = []
star_y = []
star_z = []

for line in lines:
	p = line.split()
	star_x.append(float(p[0]))
	star_y.append(float(p[1]))
	star_z.append(float(p[2]))

star_xm = np.array(star_x)
star_ym = np.array(star_y)
star_zm = np.array(star_z)


########## Centers the values by subtracting the center of mass ##########
star_centered_x = np.array(star_x)
star_centered_y = np.array(star_y)
star_centered_z = np.array(star_z)

star_centered_x[:] = [x - com_x for x in star_centered_x]
star_sub_x = star_centered_x[0::star_sub]
star_centered_y[:] = [y - com_y for y in star_centered_y]
star_sub_y = star_centered_y[0::star_sub]
star_centered_z[:] = [z - com_z for z in star_centered_z]


########## Plots ##########
plt.subplot(231)
plt.plot(gas_centered_x, gas_centered_y, '.', markersize=3, alpha=0.3)
plt.title('Gas x vs y', fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.axis([-30, 30, -30, 30])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(232)
plt.plot(disk_centered_x, disk_centered_y, '.', markersize=3, alpha=0.3)
plt.title('Disk x vs y', fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.text(-30, 40, 'Particle position plots for t = 10', fontsize=28)
plt.axis([-30, 30, -30, 30])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(233)
plt.plot(star_centered_x, star_centered_y, '.', markersize=3, alpha=0.3)
plt.title('Star x vs y', fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.axis([-30, 30, -30, 30])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(234)
plt.plot(gas_sub_x, gas_sub_y, '.', markersize=3, alpha=0.3)
plt.title('Subsampled Gas x vs y', fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.text(-45, 39, 'y (kpc)', fontsize=25, rotation='vertical')
plt.axis([-30, 30, -30, 30])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(235)
plt.plot(disk_sub_x, disk_sub_y, '.', markersize=3, alpha=0.3)
plt.title('Subsampled Disk x vs y', fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.text(-6, -40, 'x (kpc)', fontsize=25)
plt.axis([-30, 30, -30, 30])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(236)
plt.plot(star_sub_x, star_sub_y, '.', markersize=3, alpha=0.3)
plt.title('Subsampled Star x vs y', fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.axis([-30, 30, -30, 30])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.show()



























