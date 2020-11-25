import mysql.connector

def login(username,password) :
	mydb = mysql.connector.connect(host="localhost",user="root",passwd="v@run",database="Exam")
	mycursor = mydb.cursor()
	imp=password;
	mycursor.execute("SELECT* FROM login where username= %(username)s and password= %(password)s",{'username':username,'password':password})
	rows=mycursor.fetchone();
	mydb.close();
	return(rows);

def result(password) :
	mydb = mysql.connector.connect(host="localhost",user="root",passwd="v@run",database="Exam")
	mycursor = mydb.cursor()
	sid=password;
	mycursor.execute("SELECT* FROM result where Sid= %(sid)s",{'sid':sid})
	rows=mycursor.fetchone();
	mycursor.close();
	return(rows);

def admin(username,password) :
	mydb = mysql.connector.connect(host="localhost",user="root",passwd="v@run",database="Exam")
	mycursor = mydb.cursor()
	imp=password;
	mycursor.execute("SELECT* FROM admin where username= %(username)s and password= %(password)s",{'username':username,'password':password})
	rows=mycursor.fetchone();
	mydb.close();
	return(rows);


def regular():
	mydb = mysql.connector.connect(host="localhost",user="root",passwd="v@run",database="Exam")
	mycursor = mydb.cursor()
	mycursor.execute("SELECT Sid FROM students")
	myresult = mycursor.fetchall()	
	print(myresult);
	mydb.close();
	return(myresult);
	#for x in myresult:
	#print(x)

def KT():
	mydb = mysql.connector.connect(host="localhost",user="root",passwd="v@run",database="Exam")
	mycursor = mydb.cursor()
	mycursor.execute("SELECT Roll_No FROM revalution")
	myresult = mycursor.fetchall()	
	print(myresult);
	mycursor.close();
	mydb.close();
	return(myresult);
	#for x in myresult:
	#print(x)

def li (sid) :
	mydb = mysql.connector.connect(host="localhost",user="root",passwd="v@run",database="Exam")
	mycursor = mydb.cursor()
	mycursor = mydb.cursor()
	mycursor.execute("SELECT* FROM students where Sid= %(sid)s",{'sid':sid})
	rows=mycursor.fetchone();
	mydb.close();
	return(rows);
