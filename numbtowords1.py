def ones(num):
	word=""
	if num==1:
		word="one"
	elif num==2:
		word="two"
	elif num==3:
		word="three"	
	elif num==4:
		word="four"
	elif num==5:
		word="five"
	elif num==6:
		word="six"
	elif num==7:
		word="seven"
	elif num==8:
		word="eight"
	elif num==9:
		word="nine"
	elif num==10:
		word="ten"
	elif num==11:
		word="eleven"
	elif num==12:
		word="twelve"
	elif num==13:
		word="thirteen"
	elif num==14:
		word="fourteen"
	elif num==15:
		word="fifteen"
	elif num==16:
		word="sixteen"
	elif num==17:
		word="seventeen"
	elif num==18:
		word="eighteen"
	elif num==14:
		word="nineteen"


	return word

def ty(num):
	word=""
	if num==20:
		word=" twenty "
	elif num==30:
		word=" thirty"
	elif num==40:
		word=" forty "
	elif num==50:
		word=" fifty "
	elif num==60:
		word=" sixty "
	elif num==70:
		word=" seventy "
	elif num==80:
		word=" eighty "
	elif num==90:
		word=" ninety "

	return word

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
	answer+=ones(no)
print(answer)

	