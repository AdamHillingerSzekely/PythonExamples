bill= int(input("what is the bill? "))
paid= int(input("what was paid? "))
change= paid-bill
if change>=50:
	print(int(change/50), '50 pound notes')
else:
	print("no note")
rem1= change%50
if rem1>=20:
	print(int(rem1/20), '20 pound notes')
else:
	print("no note")
rem2= rem1%20
if rem2>=10:
	print(int(rem2/10), '10 pound notes')
else:
	print("no note")
rem3= rem2%10
if rem3>=5:
	print(int(rem3/5), '5 pound notes')
else:
	print("no note")
rem4= rem3%5
if rem4>=2:
	print(int(rem4/2), '2 pound coins')
else:
	print("no coin")
rem5= rem4%2
if rem5>=1:
	print(int(rem5/1), '1 pound coins')
else:
	print("no coin")



