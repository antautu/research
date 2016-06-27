import glio
s = glio.GadgetSnapshot('snapshot_000')
s.load()

f = open('data_gas_mass','w')
for i in range(0, len(s.mass[0][:])):
	f.write("%s\n" % s.mass[0][i])

f.close()


f = open('data_star_mass','w')
for i in range(0, len(s.mass[4][:])):
	f.write("%s\n" % s.mass[4][i])

f.close()