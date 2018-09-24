def naive(x,y):
	z = 0 
	while x >0:
		z = z+y
		x -= 1
	return z

def russian(x,y):
	z = 0
	while x>0:
		if x%2==1:
			z = z +y
		y = y<<1
		x = x>>1
	return z

print(naive(20, 10))
print(russian(20, 10))