name= input("what is the name? ")
salary = int(input("what is the salary? "))
if salary>=3000:
   tax =salary*0.35
if salary>=2000 and salary<3000:
   tax =salary*0.25
if salary>=1000 and salary<2000:
   tax =salary*0.15
if salary<1000:
   tax =0
net= salary-tax     
print("Your tax is ", tax ,"and your net is ", net ,".")
