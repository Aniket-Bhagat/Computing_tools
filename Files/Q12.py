import sqlite3

conn = sqlite3.connect('company.db')

cursor = conn.execute("SELECT SUBSTR(F_NAME,1,3) FROM EMPLOYEES;")

for i in cursor:
	print i[0]

conn.close()