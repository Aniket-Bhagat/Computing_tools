import sqlite3,csv

db_name='company'
try:
	conn = sqlite3.connect(db_name+'.db')
	c = conn.cursor()
	
	c.execute('''DROP TABLE IF EXISTS 'EMPLOYEES';''')
	c.execute('''CREATE TABLE EMPLOYEES
			(EMPLOYEE_ID	INT		PRIMARY KEY		NOT NULL,
			F_NAME			TEXT					NOT NULL,
			L_NAME			TEXT					NOT NULL,
			EMAIL			TEXT					NOT NULL,
			PHONE			TEXT					NOT NULL,
			H_DATE			TEXT					NOT NULL,
			JOB_ID			TEXT					NOT NULL,
			SALARY			REAL					NOT NULL,
			COM_PCT			REAL					DEFAULT NULL,
			MANAGER_ID		INT,
			DEPT_ID			INT);''')
	
	c.execute('''DROP TABLE IF EXISTS 'DEPARTMNETS';''')
	c.execute('''CREATE TABLE DEPARTMNETS
			(DEPT_ID		INT		PRIMARY KEY		NOT NULL,
			DEPT_NAME		TEXT					NOT NULL,
			MANAGER_ID		INT,
			LOCATION_ID		INT						NOT NULL,
			FOREIGN KEY(DEPT_ID) REFERENCES EMPLOYEES(DEPT_ID),
			FOREIGN KEY(MANAGER_ID) REFERENCES EMPLOYEES(MANAGER_ID));''')
	
	
	c.execute('''DROP TABLE IF EXISTS 'LOCATIONS';''')
	c.execute('''CREATE TABLE LOCATIONS
			(LOCATION_ID	INT		PRIMARY KEY		NOT NULL,
			STREET_ADD		TEXT					NOT NULL,
			POSTAL_CODE		TEXT					NOT NULL,
			CITY			TEXT					NOT NULL,
			STATE_PRO		TEXT,
			COUNTRY_ID		TEXT					NOT NULL,
			FOREIGN KEY(LOCATION_ID) REFERENCES DEPARTMNETS(LOCATION_ID));''')
	
	c.execute('''DROP TABLE IF EXISTS 'COUNTRIES';''')
	c.execute('''CREATE TABLE COUNTRIES
			(COUNTRY_ID		TEXT					NOT NULL,
			COUNTRY_NAME	TEXT					NOT NULL,
			REGION_ID		INT						NOT NULL,
			FOREIGN KEY(COUNTRY_ID) REFERENCES LOCATIONS(COUNTRY_ID));''')
	
	
	print 'Database','\''+db_name+'.db\'','created successfully'
	
	with open('employees.csv') as file:
		for row in csv.DictReader(file):
			c.execute('''INSERT INTO EMPLOYEES
				VALUES(:employee_id,:first_name,:last_name,:email,:phone_number
						,:hire_date,:job_id,:salary,:commission_pct,:manager_id,:department_id)''',row)
	
	
	with open('department.csv') as file:
		for row in csv.DictReader(file):
			c.execute('''INSERT INTO DEPARTMNETS
				VALUES(:DEPARTMENT_ID,:DEPARTMENT_NAME,:MANAGER_ID,:LOCATION_ID)''',row)

	with open('location.csv') as file:
		for row in csv.DictReader(file):
			c.execute('''INSERT INTO LOCATIONS
				VALUES(:location_id,:street_address,:postal_code,:city,:state_province,:country_id)''',row)
	
	with open('countries.csv') as file:
		for row in csv.DictReader(file):
			c.execute('''INSERT INTO COUNTRIES
				VALUES(:country_id,:country_name,:region_id)''',row)
	
	conn.commit()
	# conn.close()
	
except sqlite3.OperationalError:
	print "Table already exist in database "
	conn.rollback()

finally:
    conn.close()