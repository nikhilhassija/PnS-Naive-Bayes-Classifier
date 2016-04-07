#initialize data set
data = {}
for i in range(256):
	for j in range(2):
		for k in range(10):
			s = "{}.{}.{}".format(i,j,k)
			data[s] = 0

f = open("training.data","r")
C_code = [0 for i in range(10)]
total = 0

for i in f:
	a = i.split()
	C_code[int(a[256])] += 1
	total += 1
	for j in range(len(a)-1):
		s = "{}.{}.{}".format(str(j),str(a[j]),str(a[256]))
		data[s] += 1
f.close()

P_code = [0 for i in range(10)]

for i in range(len(C_code)):
	P_code[i] = C_code[i]/total

for i in range(256):
	for j in range(2):
		for c in range(10):
			s = "{}.{}.{}".format(i,j,c)
			data[s] = (data[s]/C_code[c])

correct = 0
incorrect = 0

f = open("testing.data","r")
for a in f:
	a = a.split()
	P = []
	for c in range(10):
		p = P_code[c]
		for i in range(256):
			s = "{}.{}.{}".format(i,a[i],c)
			p *= data[s]
		P.append(p)
	x = 0
	for i in range(10):
		if(P[i] > P[x]):
			x = i
	if(int(a[256]) == x):
		correct += 1
	else:
		# print("{}-{} | {}-{}".format(a[256],P[int(a[256])],x,P[x]))
		incorrect += 1

	#add to data set
	c = int(a[256])
	for i in range(256):
		s = "{}.{}.{}".format(i,a[i],c)
		data[s] = (data[s]*C_code[c]) + 1
		C_code[c] += 1
		data[s] = (data[s]/C_code[c])
f.close()

print("Correct Predictions: {}".format(str(correct)))
print("Inorrect Predictions: {}".format(str(incorrect)))
print("Accuracy in %: {}%".format(str(int((100*correct/(correct+incorrect))))))