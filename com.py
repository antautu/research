import math
import numpy as np
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_020')						### Change snapshot here ###
s.load()


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


########## Sets up the  x, y, and z postion arrays ##########
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


########## Sets up the mass array ##########
f2 = open('data_gas_mass')
lines = f2.readlines()
f2.close()

gas_mass = []

for line in lines:
	p = line.split()
	gas_mass.append(float(p[0]))

gas_m = np.array(gas_mass)


########## Find the center of mass in all directions ##########
gas_xm[:] = [x * (2.19052*(10**-6)) for x in gas_xm]
gas_xm_sum = sum(gas_xm)

gas_ym[:] = [y * (2.19052*(10**-6)) for y in gas_ym]
gas_ym_sum = sum(gas_ym)

gas_zm[:] = [z * (2.19052*(10**-6)) for z in gas_zm]
gas_zm_sum = sum(gas_zm)

gas_mass_sum = sum(gas_m)

com_x = gas_xm_sum / gas_mass_sum
print com_x

com_y = gas_ym_sum / gas_mass_sum
print com_y

com_z = gas_zm_sum / gas_mass_sum
print com_z


########## Centers the values by subtracting the center of mass ##########
gas_centered_x = np.array(gas_x)
gas_centered_y = np.array(gas_y)
gas_centered_z = np.array(gas_z)

gas_centered_x[:] = [x - com_x for x in gas_centered_x]
gas_centered_y[:] = [y - com_y for y in gas_centered_y]
gas_centered_z[:] = [z - com_z for z in gas_centered_z]


########## Plots centered gas position graphs ##########
plt.plot(gas_centered_x, gas_centered_y, '.', markersize=3, alpha=0.3)
plt.title('Centered Gas x vs y', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.text(20, 20, 't = 0', fontsize=15)
plt.axis([-25, 25, -25, 25])
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.show()

plt.plot(gas_centered_x, gas_centered_z, '.', markersize=3, alpha=0.3)
plt.title('Centered Gas x vs z', fontsize=22)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('z (kpc)', fontsize=18)
plt.text(20, 20, 't = 0', fontsize=15)
#plt.axis([-25, 25, -25, 25])
#plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.show()







