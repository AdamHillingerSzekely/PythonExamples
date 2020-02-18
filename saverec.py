FileWrite=open("recset.txt", "w")
i=0
while i>=0:
	enterreg=int(input("Enter registration number"))
	entername=input("Enter name")
	enteradd=input("Enter address")
	save= input("Do you want to save record, yes or no? ")
	if save == "yes" or save == "Yes":
			print(enterreg, entername, enteradd, file=FileWrite)
	else:
		break
	another=input("Do you want to save another file, yes or no")
	if another == "yes" or another == "Yes":
		i=i+1
	else:
		break
