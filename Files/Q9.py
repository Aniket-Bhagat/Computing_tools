import sqlite3

conn = sqlite3.connect('company.db')

cursor = conn.execute("SELECT AVG(SALARY) AS SALARY, COUNT(EMPLOYEE_ID) FROM EMPLOYEES;")
i = next(cursor)
print 'Average Salary :',i[0]
print 'Total number of employees :',i[1]

conn.close()