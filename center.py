import math
import numpy as np
import matplotlib.pyplot as plt
import glio
for num1 in range(4, 5): 
	for num2 in range(10):
		snap_name = 'snapshot_0%d%d' % (num1, num2)
		print snap_name
		s = glio.GadgetSnapshot(snap_name)
		s.load()


		f = open('data_gas_pos_vel','w')
		for i in range(0, len(s.vel[0][:])):

			x_gas = s.pos[0][i][0]
			y_gas = s.pos[0][i][1]
			z_gas = s.pos[0][i][2]

			r_gas = math.sqrt(x_gas**2 + y_gas**2)
			theta_gas = math.atan2(y_gas, x_gas)

			vx_gas = s.vel[0][i][0]
			vy_gas = s.vel[0][i][1]
			vz_gas = s.vel[0][i][2]

			vr_gas = vx_gas * math.cos(theta_gas) + vy_gas * math.sin(theta_gas)
			vtheta_gas = vy_gas * math.cos(theta_gas) - vx_gas * math.sin(theta_gas)

			f.write("%s %s %s %s %s %s\n" % (x_gas, y_gas, z_gas, vr_gas, vtheta_gas, vz_gas))

				
		f.close()
		
		f2 = open('data_gas_pos_vel')
		lines = f2.readlines()
		f2.close()
				
		gas_x = []
		gas_y = []
		gas_z = []
		gas_vr = []
		gas_vtheta = []
		gas_vz = []
				
		for line in lines:
			p = line.split()
			gas_x.append(float(p[0]))
			gas_y.append(float(p[1]))
			gas_z.append(float(p[2]))
			gas_vr.append(float(p[3]))
			gas_vtheta.append(float(p[4]))
			gas_vz.append(float(p[5]))
				
		gas_px = np.array(gas_x)
		gas_py = np.array(gas_y)
		gas_pz = np.array(gas_z)
		gas_pvr = np.array(gas_vr)
		gas_pvtheta = np.array(gas_vtheta)
		gas_pvz = np.array(gas_vz)
		
		
		#####################################
		plt.subplot(131)
		plt.hist(gas_px, 1000)
		plt.title('Gas x', fontsize=25)
		
		plt.subplot(132)
		plt.hist(gas_py, 1000)
		plt.title('Gas y', fontsize=25)
		
		plt.subplot(133)
		plt.hist(gas_pz, 1000)
		plt.title('Gas z', fontsize=25)
		
		plt.show()

		plt.subplot(131)
		plt.hist(gas_pvr, 1000)
		plt.title('Gas vr', fontsize=25)
		
		plt.subplot(132)
		plt.hist(gas_pvtheta, 1000)
		plt.title('Gas vtheta',fontsize=25)
		
		plt.subplot(133)
		plt.hist(gas_pvz, 1000)
		plt.title('Gas vz', fontsize=25)
		
		plt.show()