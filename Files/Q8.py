import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.execute("SELECT SALARY FROM EMPLOYEES ORDER BY SALARY ASC;")

i = next(cursor)
print 'Minimum salary :',i[0]

for i in cursor:
	maxs=i
print 'Maximum salary :',maxs[0]

conn.close()