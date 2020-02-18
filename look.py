n=0
msg = input("Enter message ")
look = input("What are you looking for ")
i=0

while i <len(msg):
		if msg[i] == look[0]:
			if msg[i: i+len(look)] == look:
				n=n+1

		i=i+1




print("found", n, look) 