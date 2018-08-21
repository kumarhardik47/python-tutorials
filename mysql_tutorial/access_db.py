import os
import MySQLdb


db = MySQLdb.connect(host="localhost",user="root",passwd="kiran",db="pythonspot")
#print type(db), dir(db)

cursor = db.cursor()
#print type(cursor), dir(cursor)

#for row in cursor.fetchall():
#	print row[0],":", row[1]
#print '*' * 80

cursor.execute("INSERT INTO EXAMPLES(description) values(\"python tutorial\")")
for row in cursor.fetchall():
	print row[0],":", row[1]
print '*' * 80

cursor.execute("SELECT * from EXAMPLES")
for row in cursor.fetchall():
	print row[0],":", row[1]
print '*' * 80


cursor.execute("DELETE from EXAMPLES WHERE id=2")
cursor.execute("SELECT * from EXAMPLES")
for row in cursor.fetchall():
	print row[0],":", row[1]
db.commit()
print '*' * 80

cursor.execute("SELECT * from EXAMPLES")
for row in cursor.fetchall():
	print row[0],":", row[1]
print '*' * 80
