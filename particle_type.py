### Writes put data files for xyz positions for all particle types ###
import numpy as np
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_001')
s.load()


### Produces xyz position data for the gas ###
f = open('data_gas_xyz', 'w')
for i in range(0, len(s.pos[0][:])):
	f.write("%s %s %s\n" % (s.pos[0][i][0],s.pos[0][i][1],s.pos[0][i][2]))
  
f.close()


### Produces xyz position data for the halo ###
f = open('data_halo_xyz', 'w')
for i in range(0, len(s.pos[1][:])):
	f.write("%s %s %s\n" % (s.pos[1][i][0],s.pos[1][i][1],s.pos[1][i][2]))
  
f.close()


### Produces xyz position data for the disk ###
f = open('data_disk_xyz', 'w')
for i in range(0, len(s.pos[2][:])):
	f.write("%s %s %s\n" % (s.pos[2][i][0],s.pos[2][i][1],s.pos[2][i][2]))
  
f.close()


### Produces xyz position data for the bulge ###
f = open('data_bulge_xyz', 'w')
for i in range(0, len(s.pos[3][:])):
	f.write("%s %s %s\n" % (s.pos[3][i][0],s.pos[3][i][1],s.pos[3][i][2]))
  
f.close()


### Produces xyz position data for the stars ###
f = open('data_star_xyz', 'w')
for i in range(0, len(s.pos[4][:])):
	f.write("%s %s %s\n" % (s.pos[4][i][0],s.pos[4][i][1],s.pos[4][i][2]))
  
f.close()


### Produces xyz position data for the boundary ###
f = open('data_boundary_xyz', 'w')
for i in range(0, len(s.pos[5][:])):
	f.write("%s %s %s\n" % (s.pos[5][i][0],s.pos[5][i][1],s.pos[5][i][2]))
  
f.close()


### Plots x vs y graphs for all particle types on the same canvas ###
### GAS ###
f2 = open('data_gas_xyz')
lines = f2.readlines()
f2.close()

gas_x = []
gas_y = []

for line in lines:
	p = line.split()
	gas_x.append(float(p[0]))
	gas_y.append(float(p[1]))
  
gas_px = np.array(gas_x)
gas_py = np.array(gas_y)


### HALO ###
f2 = open('data_halo_xyz')
lines = f2.readlines()
f2.close()

halo_x = []
halo_y = []

for line in lines:
	p = line.split()
	halo_x.append(float(p[0]))
	halo_y.append(float(p[1]))
  
halo_px = np.array(halo_x)
halo_py = np.array(halo_y)


### DISK ###
f2 = open('data_disk_xyz')
lines = f2.readlines()
f2.close()

disk_x = []
disk_y = []

for line in lines:
	p = line.split()
	disk_x.append(float(p[0]))
	disk_y.append(float(p[1]))
  
disk_px = np.array(disk_x)
disk_py = np.array(disk_y)


### BULGE ###
f2 = open('data_bulge_xyz')
lines = f2.readlines()
f2.close()

bulge_x = []
bulge_y = []

for line in lines:
	p = line.split()
	bulge_x.append(float(p[0]))
	bulge_y.append(float(p[1]))
  
bulge_px = np.array(bulge_x)
bulge_py = np.array(bulge_y)


### STAR ###
f2 = open('data_star_xyz')
lines = f2.readlines()
f2.close()

star_x = []
star_y = []

for line in lines:
	p = line.split()
	star_x.append(float(p[0]))
	star_y.append(float(p[1]))
  
star_px = np.array(star_x)
star_py = np.array(star_y)


### BOUNDARY ###
f2 = open('data_boundary_xyz')
lines = f2.readlines()
f2.close()

boundary_x = []
boundary_y = []

for line in lines:
	p = line.split()
	boundary_x.append(float(p[0]))
	boundary_y.append(float(p[1]))
  
boundary_px = np.array(boundary_x)
boundary_py = np.array(boundary_y)


### Plots x vs y position graphs for all particles types on one canvas ###
plt.subplot(231)
plt.plot(gas_px, gas_py, '.', markersize=3, alpha=0.3)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.title('Gas x vs y', fontsize=22)
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(232)
plt.plot(halo_px, halo_py, '.', markersize=3, alpha=0.3)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.title('Halo x vs y', fontsize=22)
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(233)
plt.plot(disk_px, disk_py, '.', markersize=3, alpha=0.3)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.title('Disk x vs y', fontsize=22)
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(234)
plt.plot(bulge_px, bulge_py, '.', markersize=3, alpha=0.3)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.title('Bulge x vs y', fontsize=22)
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(235)
plt.plot(star_px, star_py, '.', markersize=3, alpha=0.3)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.title('Star x vs y', fontsize=22)
plt.gca().set_aspect('equal', adjustable='box')

plt.subplot(236)
plt.plot(boundary_px, boundary_py, '.', markersize=3, alpha=0.3)
plt.xlabel('x (kpc)', fontsize=18)
plt.ylabel('y (kpc)', fontsize=18)
plt.title('Boundary x vs y', fontsize=22)
plt.gca().set_aspect('equal', adjustable='box')

plt.show()


