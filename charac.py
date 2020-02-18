List=[]
while True:
	x= (input("Enter any name "))
	List.append(x)
	if x == '0':
		Max = List[0]
		for x in List:
			if len(x)>len(Max):
				Max= x
		print(Max)
		break
