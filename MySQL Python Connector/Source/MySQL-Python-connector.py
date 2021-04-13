import mysql.connector
# 1. Establishing connection
mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="lm10barcelona", database="school")
print(mydb)
mycursor = mydb.cursor()

# 2. Creating a new DATABASE school
mycursor.execute("CREATE DATABASE school ")

# 3. To check all databases present using python
mycursor.execute(" SHOW DATABASES")
for x in mycursor:
    print(x)

# 4. To create a database using python interface
mycursor.execute(
    "CREATE TABLE student(Rollno int(3) Primary key,Name varchar(15),age integer ,city char(8))")

# 5. To check whether created table exists
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

# 6. To add a new column marks in the table
mycursor.execute("Alter table student add(marks int(3))")

# 7. To view the structure of the table using python interface
mycursor.execute("DESC student")
for x in mycursor:
    print(x)

# 8. To insert a new record into table
mycursor.execute("INSERT INTO student VALUES( 1 ,'Tarun',23,'Mumbai',398)")
mydb.commit()
print(mycursor.rowcount, "Record Inserted ")

# 9. Inserting multiple records into the table
mycursor.execute("INSERT INTO student VALUES( 2 ,'Pooja',21,'Mumbai',390)")
mycursor.execute("INSERT INTO student VALUES( 3 ,'Radhika',18,'Chail',388)")
mycursor.execute("INSERT INTO student VALUES( 4 ,'Sonia',24,'Goa',300)")
mycursor.execute("INSERT INTO student VALUES( 5 ,'Vinay',25,'Pune',410)")
mycursor.execute("INSERT INTO student VALUES( 10 ,'Shourya',15,'Delhi',345)")
mydb.commit()

# 10. Executing select statement using python
mycursor.execute("select * from student")
myrecords = mycursor.fetchall()
for x in myrecords:
    print(x)

# 11. To implement WHERE clause using python
mycursor.execute(" select name,age,marks from student WHERE city ='Delhi' ")
myrecords = mycursor.fetchall()
for x in myrecords:
    print(x)

# 12. Deleting records using python interface
mycursor.execute("DELETE FROM student WHERE Rollno = 1 ")
mydb.commit()
print(mycursor.rowcount, "record deleted ")

# 13. Updating records using python
mycursor.execute("UPDATE student set age = 28 WHERE Name = 'Vinay' ")
mydb.commit()
print(mycursor.rowcount, "Record updated")

# 14. To delete on the basis of name fetched
nm = input("Enter the name of the student you want to delete ")
try:
    mycursor.execute(" DELETE FROM student WHERE Name = '{}'".format(nm))
    print(mycursor.rowcount, "Record deleted")
    mydb.commit()
except:
    mydb.rollback()
mydb.close()
