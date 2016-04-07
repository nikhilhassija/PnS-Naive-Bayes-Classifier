f = open("raw.data","r")
x = open("training.data","w")

for i in f:
	a = i.split()
	for i in range(256):
		x.write(a[i]+" ")
	for i in range(10):
		if(a[256+i] == '1'):
			x.write(str(i))
	x.write("\n")