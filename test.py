file = open("filename.txt", "w")

for n in ("lakers", "clippers", "rockets", "kings", "sixers"):
    newline = str(n) + "\n"
    file.write(newline)

file.close()

file = open("filename.txt", "r")

print(file.readline())
file.readline()
print(file.readline())
file.seek(0)
print(file.readline())

file.close()