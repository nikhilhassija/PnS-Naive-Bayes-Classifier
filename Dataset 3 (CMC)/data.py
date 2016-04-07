f = open("raw.data","r")
x = open("training.data","w")

for i in f:
	a = i.split()
	for j in range(len(a)):
		a[j] = int(a[j])
	a[1] -= 1
	a[2] -= 1
	a[6] -= 1
	a[7] -= 1
	a[9] -= 1
	for p in a:
		x.write(str(p)+" ")
	x.write("\n")