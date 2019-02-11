import sqlite3

conn = sqlite3.connect('company.db')

cursor = conn.execute('''SELECT LOCATION_ID, STREET_ADD, CITY, STATE_PRO, COUNTRY_NAME
						FROM LOCATIONS
						NATURAL JOIN COUNTRIES;''')

print "LID 	Street Add. 		City   	      State 		Country"
print "----------------------------------------------------------------------------"
for i in cursor:
	print ('{:4d} | {:20s} | {:10s} | {:14s} | {:14s} |'.format(i[0],i[1],i[2],i[3],i[4]))

conn.close()
