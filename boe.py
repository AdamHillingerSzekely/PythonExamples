class bankofengland:
	def accountopen(self):
		print("account opening")
	def deposit(self):
		print("deposit money")
	def withdraw(self):
		print("withdraw money")

class HSBC(bankofengland):
	def loans(self):
		print("loan pricing")

class Natwest(bankofengland):
	def carfinance(self):
		print("car finance pricing")

H=HSBC()
N=Natwest()
a=N.carfinance()
b=N.accountopen()
z=H.loans()
y=H.accountopen()