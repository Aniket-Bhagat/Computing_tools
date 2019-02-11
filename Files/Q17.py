import sqlite3

conn = sqlite3.connect('company.db')

cursor = conn.execute('''SELECT L_NAME FROM EMPLOYEES
						WHERE L_NAME LIKE '__e%';''')

print "Last Names of employees having 'e' as the third character :"
for i in cursor:
	print i[0]

conn.close()