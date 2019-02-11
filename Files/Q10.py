import sqlite3

conn = sqlite3.connect('company.db')

cursor = conn.execute("SELECT COUNT(*) FROM EMPLOYEES;")
i = next(cursor)
print 'Number of employees working with company : ',i[0]

conn.close()