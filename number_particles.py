import glio
s = glio.GadgetSnapshot('snapshot_040')
s.load()

f = open('number_star','w')
for i in range(0, len(s.pos[4][:])):
	f.write("%s\n" % s.pos[4][i][0])
f.close()

f = open('number_gas','w')
for i in range(0, len(s.pos[0][:])):
	f.write("%s\n" % s.pos[0][i][0])
f.close()