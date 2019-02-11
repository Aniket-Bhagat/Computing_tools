import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.execute("SELECT F_NAME,L_NAME from EMPLOYEES")


print "  First Name    Last Name\n---------------------------"
for i in cursor:
	print ("| {0:10s} | {1:10s} |".format(i[0],i[1]))

conn.close()
