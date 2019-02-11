import sqlite3

conn = sqlite3.connect('company.db')

cursor = conn.execute('''SELECT job_id, MAX(salary) FROM employees
						GROUP BY job_id
						HAVING MAX(salary) >=4000;''')

print 'Job IDs Where maximum salary is >=4000'
for i in cursor:
	print ("{:10s} | {:5.0f} |".format(i[0],i[1]))

conn.close()