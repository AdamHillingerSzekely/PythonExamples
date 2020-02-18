an1=input("Give the name of an animal ")
an2=input("Give the name of another animal ")
letters=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
countone=0
counttwo=0
for i in letters:
	countone=countone+1
	if an1[0]== i:
		break
for j in letters:
	counttwo=counttwo+1		
	if an2[0]== j:
		break
if countone>counttwo:
	print(an2, an1)
else:
	print(an1,an2)