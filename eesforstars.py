FileRead=open("data.txt", "r")
FileWrite= open("data2.txt", "w")
for line in FileRead:
	for letter in line:
		if letter=="e" or letter=="E":
			print("*", end="", file=FileWrite)
		else:
			print(letter, end="", file=FileWrite)