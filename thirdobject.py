class college:
	physics=0
	chemistry=0
	def message(self):
		print("hello")
		print("my friend")
A=college()
A.message()
A.chemistry = 7
A.physics = 6
print(A.physics + A.chemistry)