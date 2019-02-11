import sqlite3

conn = sqlite3.connect('company.db')


uplimit = input('Print employees whose salary is not in the range :\nUpper limit: ')
lowlimit = input('Lower limit :')
upid = input('And dept. id between :\nUpperID: ')
lowid = input('LowerID: ')

cursor = conn.execute('''SELECT F_NAME,L_NAME,SALARY,DEPT_ID
						FROM EMPLOYEES
						WHERE SALARY NOT BETWEEN %d AND %d
						AND DEPT_ID IN (%d,%d);'''%(lowlimit,uplimit,lowid,upid))


print "\n	Name       Salary  Dep.ID\n---------------------------------"
for i in cursor:
	print ("{:17s} | {:5.0f} | {:3d} |".format(i[0]+' '+i[1],i[2],i[3]))

conn.close()