import sqlite3

conn = sqlite3.connect('company.db')

cursor = conn.execute("SELECT DISTINCT JOB_ID FROM EMPLOYEES;")

count = 0
for i in cursor:
	# print i[0]
	count += 1

print 'Number of jobs available : ',count

conn.close()