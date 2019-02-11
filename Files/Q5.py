import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.execute("SELECT F_NAME,L_NAME,SALARY,SALARY*0.12 from EMPLOYEES;")


print "	Name	    Salary   PF\n----------------------------------"
for i in cursor:
	print ("{:17s} | {:5.0f} | {:4.0f} |".format(i[0]+' '+i[1],i[2],i[3]))


conn.close()
