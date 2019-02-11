import sqlite3

conn = sqlite3.connect('company.db')

cursor = conn.execute("SELECT MIN(SALARY) AS SALARY FROM EMPLOYEES;")
i = next(cursor)
print "Minimum Salary :",i[0]

conn.close()
