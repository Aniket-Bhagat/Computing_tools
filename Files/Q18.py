import sqlite3

conn = sqlite3.connect('company.db')

cursor = conn.execute("SELECT COUNT(DISTINCT JOB_ID) FROM EMPLOYEES;")
i = cursor.next()
print 'Number of Jobs available : ',i[0]

conn.close()