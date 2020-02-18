ones=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
ty=["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

no= int(input(" Enter number "))
answer=""
if no>=1000:
	answer=ones(int(no/1000))+ " thousand "
	no=no%1000
if no>=100:
	answer+=ones(int(no/100))+ " hundred and"
	no=no%100
if no>=20:
	answer+=ty(int(no/10)*10)
	no=no%10
if no<=19:
	if no==0 and len(answer)==0:
		answer="zero"
	elif:
		answer+=ones(no)
print(answer)

	