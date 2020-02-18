class Results:
	phys=0
	chem=0
	math=0
	def showResults(self):
		total= self.phys + self.chem + self.math
		print("Result", total)
Shafeeq= Results()
Peter= Results()
Shafee.phys=100
Shafeeq.chem=100
Shafeeq.math=100
Shafeeq.showResults()
Peter.showResults()