import sqlite3

conn = sqlite3.connect('company.db')

x=raw_input('Employees having alphabets in there First Name\nAlphabet1 : ')
y=raw_input('Alphabet2 : ')

cursor = conn.execute('''SELECT F_NAME FROM EMPLOYEES
						WHERE F_NAME LIKE '%{}%' AND F_NAME LIKE '%{}%';'''.format(x,y))

# print "First name of all employees having both an \"b\" and \"c\" :"
print ''
for i in cursor:
	print i[0]

conn.close()