import glio
s = glio.GadgetSnapshot('snapshot_040')
s.load()


f = open('data_gas_mass','w')
for i in range(0, len(s.mass[0][:])):
	f.write("%s\n" % s.mass[0][i])

f.close()


f = open('data_halo_mass','w')
for i in range(0, len(s.mass[1][:])):
	f.write("%s\n" % s.mass[1][i])

f.close()


f = open('data_disk_mass','w')
for i in range(0, len(s.mass[2][:])):
	f.write("%s\n" % s.mass[2][i])

f.close()


f = open('data_bulge_mass','w')
for i in range(0, len(s.mass[3][:])):
	f.write("%s\n" % s.mass[3][i])

f.close()


f = open('data_star_mass','w')
for i in range(0, len(s.mass[4][:])):
	f.write("%s\n" % s.mass[4][i])

f.close()


f = open('data_boundary_mass','w')
for i in range(0, len(s.mass[5][:])):
	f.write("%s\n" % s.mass[5][i])

f.close()