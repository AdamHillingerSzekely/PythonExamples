
# Functions Taxes

 def Tax(salary):
 	T = salary * 21/100
 	return T

 s = int(input("Enter Your Salary "))
 print("Your Tax is =", Tax(s))
 print("Your Net Salary is =", s-Tax(s))

 if Tax(s) > 500:
 	print("Tax is too damn high!!")