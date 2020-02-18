g = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output=""
i=0
while i <=len(g):
	if i == 0:
		output = output + str(i)
	else:
		output= output +","+str(i)
	print(output,".")
	i=i+1