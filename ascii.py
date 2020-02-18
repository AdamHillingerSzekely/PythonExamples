alpha = input("Enter sequence ")
i=0
string=""
while i<len(alpha):
	if ord(alpha[i])>=65 and ord(alpha[i])<=90:
		string= string+chr(ord(alpha[i])+32)

	elif ord(alpha[i])>=97 and (ord(alpha[i])) <= 122:
		string= string+chr(ord(alpha[i])-32)

	elif ord(alpha[i])>=48 and ord(alpha[i])<=57:
		string= string+str(int(alpha[i])*2)

	else:
		string = string +alpha[i]
	i=i+1
print(string)