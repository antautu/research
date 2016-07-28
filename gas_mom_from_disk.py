import math
import numpy as np
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_040')						### Change snapshot here ###
s.load()


########## Produces data for the vx, vy, and vz velocity values for the disk ##########
f = open('data_disk_vxyz', 'w')
for i in range(0, len(s.vel[2][:])):
	f.write("%s %s %s\n" % (s.vel[2][i][0], s.vel[2][i][1], s.vel[2][i][2]))

f.close()


########## Produces data for the mass of the disk particles ##########
f = open('data_disk_mass', 'w')
for i in range(0, len(s.mass[2][:])):
	f.write("%s\n" % s.mass[2][i])

f.close()


########## Sets up the  vx, vy, and vz velocity arrays ##########
f2 = open('data_disk_vxyz')
lines = f2.readlines()

f2.close()

disk_vx = []
disk_vy = []
disk_vz = []

for line in lines:
	p = line.split()
	disk_vx.append(float(p[0]))
	disk_vy.append(float(p[1]))
	disk_vz.append(float(p[2]))

disk_pvx = np.array(disk_vx)
disk_pvy = np.array(disk_vy)
disk_pvz = np.array(disk_vz)

disk_vxm = np.array(disk_vx)
disk_vym = np.array(disk_vy)
disk_vzm = np.array(disk_vz)


########## Sets up the mass array ##########
f2 = open('data_disk_mass')
lines = f2.readlines()
f2.close()

disk_mass = []

for line in lines:
	p = line.split()
	disk_mass.append(float(p[0]))

disk_m = np.array(disk_mass)


########## Find the momentum in all directions ##########
disk_vxm[:] = [vx * (8.76209*(10**-6)) for vx in disk_vxm]
disk_vxm_sum = sum(disk_vxm)

disk_vym[:] = [vy * (8.76209*(10**-6)) for vy in disk_vym]
disk_vym_sum = sum(disk_vym)

disk_vzm[:] = [vz * (8.76209*(10**-6)) for vz in disk_vzm]
disk_vzm_sum = sum(disk_vzm)

disk_mass_sum = sum(disk_m)

mom_vx = disk_vxm_sum / disk_mass_sum
print mom_vx

mom_vy = disk_vym_sum / disk_mass_sum
print mom_vy

mom_vz = disk_vzm_sum / disk_mass_sum
print mom_vz


########## Centers the values by subtracting the momentum ##########
disk_centered_vx = np.array(disk_vx)
disk_centered_vy = np.array(disk_vy)
disk_centered_vz = np.array(disk_vz)

disk_centered_vx[:] = [vx - mom_vx for vx in disk_centered_vx]
disk_centered_vy[:] = [vy - mom_vy for vy in disk_centered_vy]
disk_centered_vz[:] = [vz - mom_vz for vz in disk_centered_vz]


########## Produces data for the vx, vy, and vz velocity values for the gas ##########
f = open('data_gas_vxyz', 'w')
for i in range(0, len(s.vel[0][:])):
	f.write("%s %s %s\n" % (s.vel[0][i][0], s.vel[0][i][1], s.vel[0][i][2]))

f.close()


########## Produces data for the mass of the gas particles ##########
f = open('data_gas_mass', 'w')
for i in range(0, len(s.mass[0][:])):
	f.write("%s\n" % s.mass[0][i])

f.close()


########## Sets up the  vx, vy, and vz velocity arrays ##########
f2 = open('data_gas_vxyz')
lines = f2.readlines()

f2.close()

gas_vx = []
gas_vy = []
gas_vz = []

for line in lines:
	p = line.split()
	gas_vx.append(float(p[0]))
	gas_vy.append(float(p[1]))
	gas_vz.append(float(p[2]))

gas_pvx = np.array(gas_vx)
gas_pvy = np.array(gas_vy)
gas_pvz = np.array(gas_vz)

gas_vxm = np.array(gas_vx)
gas_vym = np.array(gas_vy)
gas_vzm = np.array(gas_vz)


########## Centers the values by subtracting the momentum ##########
gas_centered_vx = np.array(gas_vx)
gas_centered_vy = np.array(gas_vy)
gas_centered_vz = np.array(gas_vz)

gas_centered_vx[:] = [vx - mom_vx for vx in gas_centered_vx]
gas_centered_vy[:] = [vy - mom_vy for vy in gas_centered_vy]
gas_centered_vz[:] = [vz - mom_vz for vz in gas_centered_vz]


########## Plots centered gas position graphs ##########
plt.subplot(121)
plt.plot(gas_pvx, gas_pvy, '.', markersize=3, alpha=0.3)
plt.title('Gas vx vs vy', fontsize=22)
plt.xlabel('vx (km/sec)', fontsize=18)
plt.ylabel('vy (km/sec)', fontsize=18)
plt.text(250, 250, 't = 40', fontsize=15)						### Make sure to change time label ###
plt.axis([-300, 300, -300, 300])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(122)
plt.plot(gas_centered_vx, gas_centered_vy, '.', markersize=3, alpha=0.3)
plt.title('Centered Gas x vs y', fontsize=22)
plt.xlabel('vx (km/sec)', fontsize=18)
plt.ylabel('vy (km/sec)', fontsize=18)
plt.text(250, 250, 't = 40', fontsize=15)						### Make sure to change time label ### 
plt.axis([-300, 300, -300, 300])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.show()

plt.subplot(121)
plt.plot(gas_pvx, gas_pvz, '.', markersize=3, alpha=0.3)
plt.title('Gas vx vs vz', fontsize=22)
plt.xlabel('vx (km/sec)', fontsize=18)
plt.ylabel('vz (kpc)', fontsize=18)
#plt.text(25, 25, 't = 0', fontsize=15)
#plt.axis([-25, 25, -25, 25])
#plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.subplot(122)
plt.plot(gas_centered_vx, gas_centered_vz, '.', markersize=3, alpha=0.3)
plt.title('Centered Gas vx vs vz', fontsize=22)
plt.xlabel('vx (km/sec)', fontsize=18)
plt.ylabel('vz (km/sec)', fontsize=18)
#plt.text(20, 20, 't = 0', fontsize=15)
#plt.axis([-25, 25, -25, 25])
#plt.gca().set_aspect('equal', adjustable='box')
plt.grid()

plt.show()










