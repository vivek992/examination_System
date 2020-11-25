import mysql.connector


def Admin(sid,name,add,gender,dob,age,email,con_1,con_2) :
	mydb = mysql.connector.connect(host="localhost",user="root",passwd="v@run",database="Exam")
	mycursor = mydb.cursor()
	mycursor = mydb.cursor()
	sql = "INSERT INTO students (Sid, Name, Address , Gender, DOB , Age, Email, Contact,Contact_2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)"
	val = (sid,name,add,gender,dob,age,email,con_1,con_2);
	mycursor.execute(sql, val)
	mydb.commit()
	mydb.close();
	print(mycursor.rowcount, "Record Inserted.")


def examform(student_name,sid,course,examst,exame,comment) :
	mydb = mysql.connector.connect(host="localhost",user="root",passwd="v@run",database="Exam")
	mycursor = mydb.cursor()
	mycursor = mydb.cursor()
	sql = "INSERT INTO exam_registartion_form1 (StdName,Std_Reg_No,Reg_Course,Exam_Start,Exam_End,Comment) VALUES (%s, %s, %s, %s, %s, %s)"
	val = (student_name,sid,course,examst,exame,comment);
	mycursor.execute(sql, val)
	mydb.commit()
	mydb.close();
	print(mycursor.rowcount, "Record Inserted.")

def KT(name,roll,college,result,center,fathername,sem,course):
	mydb = mysql.connector.connect(host="localhost",user="root",passwd="v@run",database="Exam")
	mycursor = mydb.cursor()
	mycursor = mydb.cursor()
	sql = "INSERT INTO revalution (Name,Father_Name,Roll_No ,ExamCourse,Result,SemYear,ExamCenter,College) VALUES (%s, %s, %s, %s, %s, %s,%s,%s)"
	val = (name,fathername,roll,course,result,sem,center,college);
	mycursor.execute(sql, val)
	mydb.commit()
	mydb.close();
	print(mycursor.rowcount, "Record Inserted.")

def big(Sid,name,address,gender,dob,age,email,contact,course,course_id,year,ssc,cet,hsc,jee,diploma,sem_1,sem_2,sem_3,sem_4,sem_5,sem_6,sem_7,sem_8) :
	mydb = mysql.connector.connect(host="localhost",user="root",passwd="v@run",database="Exam")
	mycursor = mydb.cursor()
	mycursor = mydb.cursor()
	sql = "INSERT INTO result  (Sid,Name,Address,Gender,DOB,Age,Email,Contact,Course,Course_Id,Year,SSC,CET,HSC,JEE,DIPLOMA,SEM_1,SEM_2,SEM_3,SEM_4,SEM_5,SEM_6,SEM_7,SEM_8)VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)"
	val = (Sid,name,address,gender,dob,age,email,contact,course,course_id,year,ssc,cet,hsc,jee,diploma,sem_1,sem_2,sem_3,sem_4,sem_5,sem_6,sem_7,sem_8);
	mycursor.execute(sql, val)
	mydb.commit()
	mydb.close();
	print(mycursor.rowcount, "Record Inserted.")


def big_2(Sid,name,address,gender,dob,age,email,contact,course,course_id,year,ssc,cet,hsc,jee,diploma,sem_1,sem_2,sem_3,sem_4,sem_5,sem_6,sem_7,sem_8) :
	mydb = mysql.connector.connect(host="localhost",user="root",passwd="v@run",database="Exam")
	mycursor = mydb.cursor()
	mycursor.execute("DELETE FROM result where Sid= %(sid)s",{'sid':Sid})
	sql = "INSERT INTO result  (Sid,Name,Address,Gender,DOB,Age,Email,Contact,Course,Course_Id,Year,SSC,CET,HSC,JEE,DIPLOMA,SEM_1,SEM_2,SEM_3,SEM_4,SEM_5,SEM_6,SEM_7,SEM_8)VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)"
	val = (Sid,name,address,gender,dob,age,email,contact,course,course_id,year,ssc,cet,hsc,jee,diploma,sem_1,sem_2,sem_3,sem_4,sem_5,sem_6,sem_7,sem_8);
	mycursor.execute(sql, val)
	mydb.commit()
	mydb.close();
	print(mycursor.rowcount, "Record Inserted.")








