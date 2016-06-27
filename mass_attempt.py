import math 
import matplotlib.pyplot as plt

plt.subplot(221)
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
11, 12, 13, 14, 15, 16, 17, 18, 19 ,20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 37, 38, 39, 40], 

[0, 21247, 43772, 77870, 109553, 130883, 152127, 185588, 222965, 263252, 317200, 
373579, 410611, 437118, 458272, 477832, 495426, 514188, 532361, 549503, 559971,
571234, 577387, 582725, 589476, 596327, 600549, 603550, 606394, 609568, 612128,
614722, 617504, 619984, 622431, 624246, 625861, 627851, 629392, 630523, 631734])

plt.xlabel('Time (Gyr)', fontsize=18)
plt.ylabel('Number of Stars', fontsize=18)
plt.title('Number of Stars Over Time', fontsize=22)
plt.axis([0, 40, 0, 650000])

plt.subplot(222)
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
11, 12, 13, 14, 15, 16, 17, 18, 19 ,20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 37, 38, 39, 40], 

[400000, 398755, 396597, 394963, 388674, 386159, 381506, 373506, 359975, 342346, 314609,
279596, 256769, 239981, 227717, 215308, 204652, 192854, 180368, 167708, 160379,
152725, 148358, 144784, 140047, 134992, 132032, 130061, 128108, 125984, 124187,
122468, 120625, 118878, 117294, 116080, 114999, 113563, 112471, 111662, 110895])

plt.xlabel('Time (Gyr)', fontsize=18)
plt.ylabel('Number of Particles', fontsize=18)
plt.title('Number of Gas Particles Over Time', fontsize=22)
plt.axis([0, 40, 0, 650000])



#####################################################################


mass_star = 1.09526 * (10**-6)
mass_gas = 2.19052 * (10**-6)

plt.subplot(223)
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 14, 15, 16, 17, 18, 19 ,20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 37, 38, 39, 40], 

[0, 21247*mass_star, 43772*mass_star, 77870*mass_star, 109553*mass_star, 130883*mass_star, 152127*mass_star, 185588*mass_star, 222965*mass_star, 263252*mass_star, 317200*mass_star, 
373579*mass_star, 410611*mass_star, 437118*mass_star, 458272*mass_star, 477832*mass_star, 495426*mass_star, 514188*mass_star, 532361*mass_star, 549503*mass_star, 559971*mass_star,
571234*mass_star, 577387*mass_star, 582725*mass_star, 589476*mass_star, 596327*mass_star, 600549*mass_star, 603550*mass_star, 606394*mass_star, 609568*mass_star, 612128*mass_star,
614722*mass_star, 617504*mass_star, 619984*mass_star, 622431*mass_star, 624246*mass_star, 625861*mass_star, 627851*mass_star, 629392*mass_star, 630523*mass_star, 631734*mass_star])

plt.xlabel('Time (Gyr)', fontsize=18)
plt.ylabel('Mass (1e10 solar masses)', fontsize=18)
plt.title('Mass of Stars Over Time', fontsize=22)
plt.axis([0, 40, 0, 0.9])

plt.subplot(224)
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
11, 12, 13, 14, 15, 16, 17, 18, 19 ,20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 37, 38, 39, 40], 

[400000*mass_gas, 398755*mass_gas, 396597*mass_gas, 394963*mass_gas, 388674*mass_gas, 386159*mass_gas, 381506*mass_gas, 373506*mass_gas, 359975*mass_gas, 342346*mass_gas, 314609*mass_gas,
279596*mass_gas, 256769*mass_gas, 239981*mass_gas, 227717*mass_gas, 215308*mass_gas, 204652*mass_gas, 192854*mass_gas, 180368*mass_gas, 167708*mass_gas, 160379*mass_gas,
152725*mass_gas, 148358*mass_gas, 144784*mass_gas, 140047*mass_gas, 134992*mass_gas, 132032*mass_gas, 130061*mass_gas, 128108*mass_gas, 125984*mass_gas, 124187*mass_gas,
122468*mass_gas, 120625*mass_gas, 118878*mass_gas, 117294*mass_gas, 116080*mass_gas, 114999*mass_gas, 113563*mass_gas, 112471*mass_gas, 111662*mass_gas, 110895*mass_gas])

plt.xlabel('Time (Gyr)', fontsize=18)
plt.ylabel('Mass (1e10 solar masses)', fontsize=18)
plt.title('Mass of Gas Over Time', fontsize=22)
plt.axis([0, 40, 0, 0.9])

plt.show()






















































#import numpy as np
#import matplotlib.pyplot as plt
#import glio
#for num1 in range(5):
#	for num2 in range(10):
#		snap_name = 'snapshot_0%d%d' % (num1, num2)
#		print snap_name
#		s = glio.GadgetSnapshot(snap_name)
#		s.load()
#
#		f = open('data_gas_xy', 'w')
#		for i in range(0, len(s.pos[0][:])):
#			f.write("%s\n" % s.pos[0][i][0])
#		
#		f.close()
#		
#		my_file = open('data_gas_xy')
#		file_contents = my_file.read()
#		print len(my_file)
