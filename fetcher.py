import pymysql as mysql
tabledata=mysql.connect("localhost","root", "", "QA")
C=tabledata.cursor()
C=db.cursor()
C.execute("select * From school")
data=C.fetchall()
for rec in data:
	print(rec.regno)
	print(rec.name)
	print(rec.marks)