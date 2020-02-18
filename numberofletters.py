 # counting number of letters in a word

upperalpha = [0]*26
loweralpha = [0]*26
msg = input("Enter Message ")
x = 0

while x < len(msg):
 	if ord(msg[x]) >= 65 and ord(msg[x]) <= 90:
 		upperalpha[ord(msg[x])-65] += 1
 	if ord(msg[x]) >= 97 and ord(msg[x]) <= 122:
 		loweralpha[ord(msg[x])-97] += 1
 	x += 1

 x = 0
 while x < len(loweralpha):
 	if loweralpha[x] != 0:
 		print(chr(x+97), "=", loweralpha[x])
 	if upperalpha[x] != 0:
 		print(chr(x+65), "=", upperalpha[x])
 	x += 1
