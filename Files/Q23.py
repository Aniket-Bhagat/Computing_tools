import sqlite3

conn = sqlite3.connect('company.db')

cursor = conn.execute('''SELECT F_NAME, L_NAME, DEPT_ID, DEPT_NAME 
						FROM EMPLOYEES 
						JOIN DEPARTMNETS USING (DEPT_ID);''')

print "	Name	  Dep. ID    Dep. Name\n--------------------------------------------"
for i in cursor:
	print ("{:17s} | {:3d} | {:16s} |".format(i[0]+' '+i[1],i[2],i[3]))

conn.close()