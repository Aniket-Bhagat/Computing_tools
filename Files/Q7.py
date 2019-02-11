import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.execute("SELECT SUM(SALARY) from EMPLOYEES;")

print 'Total Salaries payable to employees :'
print cursor.next()[0]

conn.close()
