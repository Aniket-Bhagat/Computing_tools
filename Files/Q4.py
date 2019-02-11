import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.execute("SELECT * from EMPLOYEES ORDER BY F_NAME DESC;")

print "EID	  Name 		  email 	contact     Hire date     Job ID      Salary  Comm%  MID Dept. ID"
print "--------------------------------------------------------------------------------------------------------" 
for i in cursor:
	print ('{:3d} | {:17s} | {:8s} | {:12s} | {:10s} | {:10s} | {:5.0f} | {:4s} | {:3s} | {:3s} |'
		.format(i[0],i[1]+' '+i[2],i[3],i[4],i[5],i[6],i[7],str(i[8]),str(i[9]),str(i[10])))

conn.close()
