import sqlite3

conn = sqlite3.connect('company.db')

x=raw_input('Employees having Job in following Department Options:(input as \'IT_PROG\',\'SH_CLERK\')\nOption1 : ')
y=raw_input('Option2 : ')
n1=input('\nAnd Salaries as:\nSalary1 : ')
n2=input('Salary2 : ')
n3=input('Salary3 : ')


cursor = conn.execute('''SELECT L_NAME,JOB_ID,SALARY FROM EMPLOYEES
						WHERE JOB_ID IN ('{}', '{}')
						AND SALARY NOT IN ({},{},{});'''.format(x,y,n1,n2,n3))


print "\nLast Name     Job ID    Salary\n--------------------------------"
for i in cursor:
	print ("{:10s} | {:9s} | {:5.0f} |".format(i[0],i[1],i[2]))

conn.close()