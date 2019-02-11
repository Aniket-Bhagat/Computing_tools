import sqlite3

conn = sqlite3.connect('company.db')

cursor = conn.execute('''SELECT JOB_ID, AVG(SALARY), COUNT(*) FROM EMPLOYEES
						GROUP BY DEPT_ID HAVING COUNT(*) > 10;''')

print "Job ID  Avg. Salary  no. employees\n--------------------------"
for i in cursor:
	print ("{:9s} | {:7.2f} | {:2d} |".format(i[0],i[1],i[2]))

conn.close()