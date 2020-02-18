bill= int(input("what is the bill? "))
paid= int(input("what was paid? "))
change= paid-bill
if change>=50:
	print(int(change/50), '50 pound notes')
	change= change%50
if change>=20:
	print(int(change/20), '20 pound notes')
	change= change%20
if change>=10:
	print(int(change/10), '10 pound notes')
	change= change%10
if change>=5:
	print(int(change/5), '5 pound notes')
	change= change%5
if change>=2:
	print(int(change/2), '2 pound coins')
	change= change%2
if change>=1:
	print(int(change/1), '1 pound coins')



