

class Text:
	def writefile(self):
		self.result=open( "file.txt", "w")
	def insertrecords(self)
		while True:
			enterreg=(input("Enter registration number"))
			entername=input("Enter name")
			enteradd=input("Enter address")
			save= input("Do you want to save record, yes or no? ")
			if save.upper() == "YES":
				print(self2, enterreg, entername, enteradd, sep=",", file=FileWrite)
				another=input("Do you want to save another file, yes or no ")
			if another.upper() != "YES":
				break
	def Find(self):
		for line in FileRead:
			for letter in line:
				if letter=="Sha" or letter=="E":
					print("*", end="", file=FileWrite)
				else:
					print(letter, end="", file=FileWrite)

T=Text()
T.writefile()
T.insertrecords()


