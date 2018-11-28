import random 


r1 = '700'
c1 = '150'
r2 = '150'
c2 = '1000'

f = open('mm_input.txt', 'w')
f.write(r1+' '+c1+' '+r2+' '+c2+'\n')
for x in range(0, int(r1)):
	for y in range(0, int(c1)):
		if not y == int(c1)-1:
			f.write(str(random.randint(-1000, 1000))+' ')
		else:
			f.write(str(random.randint(-1000, 1000)))
	f.write('\n')
for x in range(0, int(r2)):
	for y in range(0, int(c2)):
		if not y == int(c2)-1:
			f.write(str(random.randint(-1000, 1000))+' ')
		else:
			f.write(str(random.randint(-1000, 1000)))
	if not x == int(r2)-1:
		f.write('\n')
f.close()