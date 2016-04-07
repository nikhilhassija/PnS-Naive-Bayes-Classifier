f = open("raw.data","r")
x = open("training.data","w")

for i in f:
	a = i
	a = a.replace(" ","")
	a = a.replace(","," ")
	for j in a:
		x.write(j)