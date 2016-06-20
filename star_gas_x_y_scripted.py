### Plots star and gas position graphs next to eachother for ALL snapshots ###
### [0] = Gas ###
### [4] = Star ###

import numpy as np
import matplotlib.pyplot as plt
import glio
for num1 in range(5):
	for num2 in range(10):
		snap_name = 'snapshot_0%d%d' % (num1, num2)
		print snap_name
		s = glio.GadgetSnapshot(snap_name)		### Change snapshot here ###
		s.load()
		
		
		### Produces data for the gas x vs y graph ###
		f = open('data_gas_xy','w')
		for i in range(0, len(s.pos[0][:])):
			f.write("%s %s\n" % (s.pos[0][i][0],s.pos[0][i][1]))
		
		f.close()
		
		
		### Produces data for the star x vs y graph ###
		f = open('data_star_xy','w')
		for i in range(0, len(s.pos[4][:])):
			f.write("%s %s\n" % (s.pos[4][i][0],s.pos[4][i][1]))
		
		f.close()
		
		
		### Plots star and gas x vs y graphs on the same canvas ###
		f2 = open('data_star_xy')
		lines = f2.readlines()
		f2.close()
		
		star_x_xy = []
		star_y_xy = []
		
		for line in lines:
			p = line.split()
			star_x_xy.append(float(p[0]))
			star_y_xy.append(float(p[1]))
		
		star_px_xy = np.array(star_x_xy)
		star_py_xy = np.array(star_y_xy)
		
		f2 = open('data_gas_xy')
		lines = f2.readlines()
		f2.close()
		
		gas_x_xy = []
		gas_y_xy = []
		
		for line in lines:
			p = line.split()
			gas_x_xy.append(float(p[0]))
			gas_y_xy.append(float(p[1]))
		
		gas_px_xy = np.array(gas_x_xy)
		gas_py_xy = np.array(gas_y_xy)
		
		
		plt.subplot(121)
		plt.plot(star_px_xy, star_py_xy, '.', markersize=3, alpha=0.3)
		plt.xlabel('x')
		plt.ylabel('y')
		plt.title('Star x vs y')
		plt.text(20, 20, 't = %d%d' % (num1, num2))			### Make sure to change time label ###
		plt.axis([-25, 25, -25, 25])
		plt.gca().set_aspect('equal', adjustable='box')
		
		plt.subplot(122)
		plt.plot(gas_px_xy, gas_py_xy, '.', markersize=3, alpha=0.3)
		plt.xlabel('x')
		plt.ylabel('y')
		plt.title('Gas x vs y')
		plt.text(20, 20, 't = %d%d' % (num1, num2))			### Make sure to change time label ###
		plt.axis([-25, 25, -25, 25])
		plt.gca().set_aspect('equal', adjustable='box')
		
		plt.show()
