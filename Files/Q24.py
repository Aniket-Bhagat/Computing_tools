import sqlite3

conn = sqlite3.connect('company.db')

cursor = conn.execute('''SELECT e.EMPLOYEE_ID 'Emp_Id', e.L_NAME 'Employee', 
						m.EMPLOYEE_ID 'Mgr_Id', m.L_NAME 'Manager' 
						FROM EMPLOYEES e 
						join EMPLOYEES m 
						ON (e.manager_id = m.employee_id);''')

print "EID   Employee     MID   Manager\n------------------------------------"
for i in cursor:
	print ("{:3d} | {:10s} | {:3d} | {:9s} |".format(i[0],i[1],i[2],i[3]))

conn.close()