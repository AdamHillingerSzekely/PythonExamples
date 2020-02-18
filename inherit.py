class ONE:
	def message1(self):
		print("hello")

class TWO(ONE):
	def message2(self):
		print("my friends")

class THREE(TWO,ONE):
	def message3(self):
		print("world")



x=THREE()
x.message1()
x.message2() 
x.message3()