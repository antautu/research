import math
import numpy as np
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_040')						### Change snapshot here ###
s.load()


########## Produces data for the x, y, and z position values for the disk ##########
f = open('data_disk_xyz', 'w')
for i in range(0, len(s.pos[2][:])):
	f.write("%s %s %s\n" % (s.pos[2][i][0], s.pos[2][i][1], s.pos[2][i][2]))

f.close()


########## Produces data for the mass of the gas particles ##########
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
print com_x

com_y = disk_ym_sum / disk_mass_sum
print com_y

com_z = disk_zm_sum / disk_mass_sum
print com_z


########## Centers the values by subtracting the center of mass ##########
disk_centered_x = np.array(disk_x)
disk_centered_y = np.array(disk_y)
disk_centered_z = np.array(disk_z)

disk_centered_x[:] = [x - com_x for x in disk_centered_x]
disk_centered_y[:] = [y - com_y for y in disk_centered_y]
disk_centered_z[:] = [z - com_z for z in disk_centered_z]


########## Plots centered disk position graphs ##########
plt.subplot(121)
plt.plot(disk_px, disk_py, '.', markersize=3, alpha=0.3)
plt.title('Disk x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(25, 25, 't = 40', fontsize=15)						### Make sure to change time label ###
plt.axis([-30, 30, -30, 30])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(122)
plt.plot(disk_centered_x, disk_centered_y, '.', markersize=3, alpha=0.3)
plt.title('Centered Disk x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(25, 25, 't = 40', fontsize=15)						### Make sure to change time label ### 
plt.axis([-30, 30, -30, 30])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.show()

plt.subplot(121)
plt.plot(disk_px, disk_pz, '.', markersize=3, alpha=0.3)
plt.title('Disk x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('z (kpc)', fontsize=18)
#plt.text(25, 25, 't = 0', fontsize=15)
#plt.axis([-25, 25, -25, 25])
#plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(122)
plt.plot(disk_centered_x, disk_centered_z, '.', markersize=3, alpha=0.3)
plt.title('Centered Disk x vs z', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('z (kpc)', fontsize=18)
#plt.text(20, 20, 't = 0', fontsize=15)
#plt.axis([-25, 25, -25, 25])
#plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.show()