class Maths:
	Result=0
	def doCalculation(self,A,B):
		self.Result=A+B
	def showResult(self):
		print("Result is", self.Result)
M=Maths()
M.doCalculation(10,20)
M.showResult()
M.doCalculation(27,4)
M.showResult()