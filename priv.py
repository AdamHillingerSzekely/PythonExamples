class Results:
	__phy=0
	__che=0
	def physics(self, p):
		if p>=0 and p<=100:
			self.__phy=p
		else:
			print("invalid physics mark")
	def chemistry(self, c):
		if c>=0 and c<=100:
			self.__che=c
		else:
			print("invalid chemistry mark")
		

L=Results()
z=int(input("enter mark for physics"))
k=int(input("enter mark for chemistry"))
L.physics(z)  
L.chemistry(k)