### Writes put data files for xyz positions for gas, disk, and star ###
import numpy as np
import matplotlib.pyplot as plt
import glio
for num1 in range(5):
	for num2 in range(10):
		snap_name = 'snapshot_0%d%d' % (num1, num2)			
		print snap_name
		s = glio.GadgetSnapshot(snap_name)
		s.load()

		### Produces xyz position data for the gas ###
		f = open('data_gas_xyz', 'w')
		for i in range(0, len(s.pos[0][:])):
				f.write("%s %s %s\n" % (s.pos[0][i][0],s.pos[0][i][1],s.pos[0][i][2]))
			  
		f.close()
			
			
		### Produces xyz position data for the disk ###
		f = open('data_disk_xyz', 'w')
		for i in range(0, len(s.pos[2][:])):
				f.write("%s %s %s\n" % (s.pos[2][i][0],s.pos[2][i][1],s.pos[2][i][2]))
			  
		f.close()
			
			
		### Produces xyz position data for the stars ###
		f = open('data_star_xyz', 'w')
		for i in range(0, len(s.pos[4][:])):
				f.write("%s %s %s\n" % (s.pos[4][i][0],s.pos[4][i][1],s.pos[4][i][2]))
			  
		f.close()


		### Plots x vs y graphs for all gas, disk, and star on the same canvas ###
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


		### Plots x vs y position graphs for gas, disk, and star on one canvas ###
		plt.subplot(131)
		plt.plot(gas_px, gas_py, '.', markersize=3, alpha=0.3)
		plt.xlabel('x (kpc)', fontsize=18)
		plt.ylabel('y (kpc)', fontsize=18)
		plt.title('Gas x vs y', fontsize=22)
		plt.text(20, 25, 't = %d%d' % (num1, num2), fontsize=15)
		plt.axis([-30, 30, -30, 30])
		plt.gca().set_aspect('equal', adjustable='box')
			
		plt.subplot(132)
		plt.plot(disk_px, disk_py, '.', markersize=3, alpha=0.3)
		plt.xlabel('x (kpc)', fontsize=18)
		plt.ylabel('y (kpc)', fontsize=18)
		plt.title('Disk x vs y', fontsize=22)
		plt.text(20, 25, 't = %d%d' % (num1, num2), fontsize=15)
		plt.axis([-30, 30, -30, 30])
		plt.gca().set_aspect('equal', adjustable='box')
			
		plt.subplot(133)
		plt.plot(star_px, star_py, '.', markersize=3, alpha=0.3)
		plt.xlabel('x (kpc)', fontsize=18)
		plt.ylabel('y (kpc)', fontsize=18)
		plt.title('Star x vs y', fontsize=22)
		plt.text(20, 25, 't = %d%d' % (num1, num2), fontsize=15)
		plt.axis([-30, 30, -30, 30])
		plt.gca().set_aspect('equal', adjustable='box')
			
		plt.show()
