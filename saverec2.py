FileWrite=open("recset.txt", "w")
while True:
	enterreg=(input("Enter registration number"))
	entername=input("Enter name")
	enteradd=input("Enter address")
	save= input("Do you want to save record, yes or no? ")
	if save.upper() == "YES":
		print(enterreg, entername, enteradd, sep=",", file=FileWrite)
	another=input("Do you want to save another file, yes or no ")
	if another.upper() != "YES":
		break
