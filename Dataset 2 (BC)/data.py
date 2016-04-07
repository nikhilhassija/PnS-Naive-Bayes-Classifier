f = open("raw.data","r")

for i in f:
	a = i.split()
	a[10] = (int(a[10])//2) - 1
	print(a[1:d])