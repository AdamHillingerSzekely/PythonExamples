import pymysql as mysql
db = mysql.connect("localhost","root", "", "QA")
C= db.cursor()
regno=int(input("Registration"))
name=input("The Name")
marks=int(input("Your marks"))
C.execute("insert into school values(regno, name, marks)")
db.commit()