import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.execute("SELECT DISTINCT DEPT_ID FROM EMPLOYEES ORDER BY DEPT_ID ASC;")

print 'Unique Department ID\'s are following :'
for i in cursor:
	print i[0]

conn.close()
