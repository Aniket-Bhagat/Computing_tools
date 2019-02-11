import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.execute("SELECT * from EMPLOYEES ORDER BY SALARY ASC;")


print "EID	    Name	 Salary\n---------------------------------"
for i in cursor:
	print ("{:3d} | {:17s} | {:5.0f} |".format(i[0],i[1]+' '+i[2],i[7]))


conn.close()
