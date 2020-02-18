FileWrite=open("sports.txt", "w")
i=0
Sportsteamname = ["Chelsea", "Man utd", "Liverpool", "Arsenal", "Tottenham"]
while i<5:
	print(Sportsteamname, sep=",", file=FileWrite)
	if Sportsteamname[i]=/=4:
		File=open("sports.txt", "r")
	else:
		pass