
# python3 -m pip install mysql-connector-python

# create user 'testuser1'@'localhost' identified by 'password' ;

# grant all privileges on *.* to 'testuser1'@'localhost' ;

# DROP USER 'testuser1'@'localhost';

# RUN in C:\Program Files\MySQL\MySQL Server 8.0\bin

# python3 python3_program_Game_TX.py



# -- py


import mysql.connector

#test_text = input ("Enter user testuser1 password: ")
test_text = 'password'

if test_text == 'password':
	print ('hello - start myql PY script Game deactivated_table Texas: ')

	mydb = mysql.connector.connect(
		user='testuser1',
		password=test_text,
		database='game',
		host='localhost',
		allow_local_infile='1',
		auth_plugin='mysql_native_password'
	)

	print(mydb)

	myc = mydb.cursor()

	myc.execute('set global local_infile = 1')
	
	myc.execute ('use game ;')

	myc.execute ('show tables ;')

	for x in myc:
		print(x)

	myc.execute('drop table if exists Deactivated_User ;')

	myc.execute("""
		create table Deactivated_User (
		d_id int NOT NULL,
		name varchar(40) NOT NULL,
		email varchar(60) NOT NULL,
		ssn varchar(11),
		birthdate date,
		address varchar(120),
		city varchar(80),
		state varchar(30),
		zipcode varchar(10),
		ipv4 varchar(30),
		card_info varchar(120),
		Primary Key (d_id)
	) ;
	""")

	# count User table
	myc.execute("""
		SELECT count(*) 
		from User U ;
	""")
	for x in myc:
		print(x)

	
	# copy TX users to Deactivated_User table
	
	myc.execute("""
		INSERT INTO Deactivated_User (d_id, name, email, ssn, birthdate, address, city, state, zipcode, ipv4, card_info)
		SELECT U.u_id, U.name, U.email, U.ssn, U.birthdate, U.address, U.city, U.state, U.zipcode, U.ipv4, U.card_info
		from User U
		where U.state like '%TX%' ;
	""")

	

	# remove TX users from lobbys and game instances and User table
	myc.execute("""
		DELETE E
		from enter_lobby E 
		LEFT JOIN User U on U.u_id
		where U.u_id = E.u_id and U.state like '%TX%';
	""")

	myc.execute("""
		DELETE J
		from join_instance J 
		LEFT JOIN User U on U.u_id
		where U.u_id = J.u_id and U.state like '%TX%';
	""")

	myc.execute("""
		DELETE U
		from User U
		where U.state like '%TX%' ;
	""")

	# count Deactivated_User table
	myc.execute("""
		SELECT count(*) 
		from Deactivated_User ;
	""")
	for x in myc:
		print('deact users.')
		print(x)

	# count User table
	myc.execute("""
		SELECT count(*) 
		from User ;
	""")
	for x in myc:
		print('users.')
		print(x)


	mydb.commit()	
	mydb.close()


	'''

	select * from Deactivated_User ;

	SELECT *
	from enter_lobby E 
	LEFT JOIN User U on U.u_id
	where U.u_id = E.u_id and U.state like '%TX%';

	SELECT *
	DELETE join_instance
	from join_instance J 
	LEFT JOIN User U on U.u_id
	where U.u_id = J.u_id and U.state like '%WY%';

	SELECT *
	from join_instance J 
	LEFT JOIN User U on U.u_id
	where U.u_id = J.u_id and U.state like '%TX%';

	DELETE
	from enter_lobby E 
	LEFT JOIN User U on U.u_id
	where U.u_id = E.u_id and U.state like '%TX%';




for x in myc:

	# remove TX users from lobbys and game instances and User table
	myc.execute("""

		DELETE
		from enter_lobby E 
		LEFT JOIN User U on U.u_id
		where U.u_id = E.u_id and U.state like '%TX%';

		DELETE
		from join_instance J 
		LEFT JOIN User U on U.u_id
		where U.u_id = J.u_id and U.state like '%TX%';
		
		DELETE
		from User U
		where U.state like '%TX%' ;

	""")

	
	# count Deactivated_User table
	myc.execute("""
		SELECT count(*) 
		from Deactivated_User D ;
	""")
	for x in myc:
		print(x)

	# count User table
	myc.execute("""
		SELECT count(*) 
		from User U ;
	""")
	for x in myc:
		print(x)


	mydb.commit()
	mydb.close()

'''
'''
row = myc.fetchone()
while row is not None:
	print(row)
	row = myc.fetchone()

cursor.execute("SELECT * FROM employees")
row = cursor.fetchone()
while row is not None:
  print(row)
  row = cursor.fetchone()

#myc.execute("""
	#	load data local infile 'data_sailors.txt' 
	#	into table Sailors
	#	fields terminated by ','
	#	lines terminated by '\n' ;
	#""")

'''




		






