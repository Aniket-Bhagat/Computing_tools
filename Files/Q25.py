import sqlite3

conn = sqlite3.connect('company.db')

cursor = conn.execute('''SELECT d.DEPT_NAME, e.F_NAME, l.CITY 
						FROM DEPARTMNETS d, EMPLOYEES e 
						JOIN LOCATIONS l USING (LOCATION_ID)
						WHERE (d.manager_id = e.employee_id);''') 

print " Dept. Name        Manager     City\n-----------------------------------------"
for i in cursor:
	print ("{:16s} | {:9s} | {:9s} |".format(i[0],i[1],i[2]))

conn.close()