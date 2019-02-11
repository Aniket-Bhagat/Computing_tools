import sqlite3

conn = sqlite3.connect('company.db')

uplimit = input('Print employees whose salary is not in the range :\nUpper limit: ')
lowlimit = input('Lower limit :')

cursor = conn.execute('''SELECT F_NAME,L_NAME,SALARY FROM EMPLOYEES
	WHERE SALARY NOT BETWEEN %d AND %d;'''%(lowlimit,uplimit))

print ('\nAll employees whose salary is not in the range $%d to $%d :\n'%(lowlimit,uplimit))
print "  Name 		   Salary\n---------------------------"
for i in cursor:
	print ("{:17s} | {:5.0f} |".format(i[0]+' '+i[1],i[2]))

conn.close()