f = open("raw.data","r")
x = open("training.data","w")

for i in f:
	for j in i:
		x.write(j)