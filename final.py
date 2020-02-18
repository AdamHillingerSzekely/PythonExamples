import pymysql as mysql
class tabledata:
	def __init__(self):
		tabledata=mysql.connect("localhost","root", "", "QA")
		self.tabledata=tabledata
		self.C=tabledata.cursor()
	def mainscreen(self):
		choice=input("Enter your choice (entry/remove/view)? ")
		if choice.upper() == "ENTRY":
			self.dataentry()
		if choice.upper() == "REMOVE":
			self.dataremove()
		if choice.upper() == "VIEW":
			self.dataview()

	def dataentry(self):
		while True:
			regno=int(input("Enter registration number "))
			name=input("Enter name ")
			group=input("Enter group ")
			client= input("Enter client ")
			marks=input("Enter marks ")
			save= input("Do you want to save record, yes or no? ")
			if save.upper() == "YES":
				self.C.execute("select regno from consultant where Regno="+str(regno))
				data=self.C.fetchall()
				if len(data)>=1:
					print("This regno already exists,")
				else:
					self.C.execute( f"Insert into consultant values({regno}, '{name}', '{group}', '{client}', {marks})")
					self.tabledata.commit()
			another=input("Do you want to save another file, yes or no ")
			if another.upper() != "YES":
				break
	

	def dataremove(self):
		enterref=input("Enter registration number of record to remove. ")
		self.C.execute("select * from consultant where regno= "+enterref)
		data=self.C.fetchall()
		for rec in data:
			print(rec[0])
			print(rec[1])
			print(rec[2])
			print(rec[3])
			print(rec[4])
			sure = input("Are you sure you want to delete the record? ")
			if sure.upper() == "YES":
				self.C.execute("delete from consultant where regno = "+enterref)
				self.tabledata.commit()
			else:
				break

		
					


	def dataview(self):
		viewer=input("What would you like to view records based on? ")
		if viewer.upper() == "ALL":
			self.C.execute("select * from consultant")
			data=self.C.fetchall()
			for rec in data:
				print(rec[0])
				print(rec[1])
				print(rec[2])
				print(rec[3])
				print(rec[4])

		if viewer.upper() == "REGNO":
			regno = input('what regno would you like to view')
			self.C.execute("select * from consultant where Regno"+regno)
			data=self.C.fetchall()
			for rec in data:
				print(rec.Regno)
				print(rec.Name)
				print(rec.Group)
				print(rec.Client)
				print(rec.Marks)
		
		if viewer.upper() == "NAME":
			group= input('what name would you like to view')
			self.C.execute("select * from consultant where Name='"+name+"'")
			data=self.C.fetchall()
			for rec in data:
				print(rec[0])
				print(rec[1])
				print(rec[2])
				print(rec[3])
				print(rec[4])

		if viewer.upper() == "GROUP":
			group= input('what group would you like to view')
			self.C.execute("select * from consultant where Group='"+group+"'")
			data=self.C.fetchall()
			for rec in data:
				print(rec[0])
				print(rec[1])
				print(rec[2])
				print(rec[3])
				print(rec[4])
		if viewer.upper() == "CLIENT":
			client = input('what client would you like to view: ')
			self.C.execute("select * from consultant where Client='"+client+"'")
			data=self.C.fetchall()
			for rec in data:
				print(rec[0])
				print(rec[1])
				print(rec[2])
				print(rec[3])
				print(rec[4])
M=tabledata()


x=M.mainscreen()

			




