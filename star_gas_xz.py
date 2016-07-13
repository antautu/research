### Plots star and gas position graphs next to eachother for any snapshot ###
### [0] = Gas ###
### [4] = Star ###

import numpy as np
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_010')
s.load()

### Produces data for the gas x vs z graph ###
f = open('data_gas_xz','w')
for i in range(0, len(s.pos[0][:])):
	f.write("%s %s\n" % (s.pos[0][i][0],s.pos[0][i][2]))
		
f.close()
		
		
### Produces data for the star x vs z graph ###
f = open('data_star_xz','w')
for i in range(0, len(s.pos[4][:])):
	f.write("%s %s\n" % (s.pos[4][i][0],s.pos[4][i][2]))
		
f.close()
		
		
### Plots star and gas x vs z graphs on the same canvas ###
f2 = open('data_star_xz')
lines = f2.readlines()
f2.close()
		
star_x_xz = []
star_z_xz = []
		
for line in lines:
	p = line.split()
	star_x_xz.append(float(p[0]))
	star_z_xz.append(float(p[1]))
		
star_px_xz = np.array(star_x_xz)
star_pz_xz = np.array(star_z_xz)
		
f2 = open('data_gas_xz')
lines = f2.readlines()
f2.close()
		
gas_x_xz = []
gas_z_xz = []
		
for line in lines:
	p = line.split()
	gas_x_xz.append(float(p[0]))
	gas_z_xz.append(float(p[1]))
		
gas_px_xz = np.array(gas_x_xz)
a = gas_px_xz[0::15]
gas_pz_xz = np.array(gas_z_xz)
b = gas_pz_xz[0::15]
		
		
plt.subplot(121)
plt.plot(star_px_xz, star_pz_xz, '.', markersize=3, alpha=0.3)
plt.title('Star x vs z')
plt.xlabel('x (kpc)')
plt.ylabel('z (kpc)')
plt.text(20, 20, 't = z')			### Make sure to change time label ###
plt.axis([-10, 10, -0.5, 1.5])
#plt.gca().set_aspect('equal', adjustable='box')
		
plt.subplot(122)
plt.plot(gas_px_xz, gas_pz_xz, '.', markersize=3, alpha=0.3)
#plt.plot(a, b, '.', markersize=3, alpha=0.3)
plt.title('Gas x vs z')
plt.xlabel('x (kpc)')
plt.ylabel('z (kpc)')
plt.text(20, 20, 't = 1')			### Make sure to change time label ###
plt.axis([-25, 25, -1.5, 1.5])
#plt.gca().set_aspect('equal', adjustable='box')
		
plt.show()
