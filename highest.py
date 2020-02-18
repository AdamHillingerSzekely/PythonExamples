List=[]
while True:
	x= int(input("Enter any number "))
	List.append(x)
	if x ==-1:
		Max = List[0]
		for x in List:
			if x>Max:
				Max= x
		print(Max)
		break
