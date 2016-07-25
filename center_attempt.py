import numpy as np
import matplotlib.pyplot as plt
import glio
s = glio.GadgetSnapshot('snapshot_037')
s.load()

f = open('data_gas_xyz','w')
for i in range(0, len(s.pos[0][:])):
	f.write("%s %s %s\n" % (s.pos[0][i][0],s.pos[0][i][1],s.pos[0][i][2]))
				
f.close()
		
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
				
gas_px = np.array(gas_x)
gas_py = np.array(gas_y)
gas_pz = np.array(gas_z)
		
		
#####################################
gas_px[:] = [x - -0.753 for x in gas_px]
gas_py[:] = [y - 0.796 for y in gas_py]
gas_pz[:] = [z - 1.000 for z in gas_pz]

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

plt.plot(gas_px, gas_pz, '.', markersize=3,alpha=0.3)
plt.title('Gas x vs z', fontsize=30)
plt.show()