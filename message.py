message = input("Enter any message: ")
space=0
i=0
while i <len(message):
	if message[i]==" ":
		space+=1
	i+=1
print("in the message we have", (space+1), "words.")