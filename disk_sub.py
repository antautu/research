### Plots subsampled x vs y positon graphs for the disk at all time steps ###

import numpy as np
import matplotlib.pyplot as plt
import glio
for num1 in range(5):
	for num2 in range(10):
		snap_name = 'snapshot_0%d%d' % (num1, num2)
		print snap_name
		s = glio.GadgetSnapshot(snap_name)
		s.load()

		### Produces data for the subsampled disk x vs y graph ###
		f = open('data_disk_xy','w')
		for i in range(0, len(s.pos[2][:])):
			f.write("%s %s\n" % (s.pos[2][i][0],s.pos[2][i][1]))
				
		f.close()
				
				
		### Plots subsampled x vs y graph for the disk ###
		f2 = open('data_disk_xy')
		lines = f2.readlines()
		f2.close()
				
		disk_x = []
		disk_y = []
				
		for line in lines:
			p = line.split()
			disk_x.append(float(p[0]))
			disk_y.append(float(p[1]))
				
		disk_px = np.array(disk_x)
		a = disk_px[0::9]					### [0::n] starts from beginning and then takes steps of size n ###
		disk_py = np.array(disk_y)
		b = disk_py[0::9]
		
		
		plt.subplot(121)
		plt.plot(disk_px, disk_py, '.', markersize=3, alpha=0.3)
		plt.xlabel('x (kpc)', fontsize=18)
		plt.ylabel('y (kpc)', fontsize=18)
		plt.title('Disk x vs y', fontsize=22)
		plt.text(20, 25, 't = %d%d' % (num1, num2), fontsize=15)			
		plt.axis([-30, 30, -30, 30])
		plt.gca().set_aspect('equal', adjustable='box')

		plt.subplot(122)
		plt.plot(a, b, '.', markersize=3, alpha=0.3)
		plt.xlabel('x (kpc)', fontsize=18)
		plt.ylabel('y (kpc)', fontsize=18)
		plt.title('Disk x vs y Subsampled', fontsize=22)
		plt.text(20, 25, 't = %d%d' % (num1, num2), fontsize=15)			
		plt.axis([-30, 30, -30, 30])
		plt.gca().set_aspect('equal', adjustable='box')
		
		plt.show()