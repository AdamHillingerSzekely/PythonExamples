class First:
	A=0
	B=0

ref1=First()
ref2=First()
ref1.A=15
ref2.B=24
ref1.B=10
ref2.A=15
print(ref1.A + ref2.B +ref1.B +ref2.A)