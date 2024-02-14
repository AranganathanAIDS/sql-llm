import sqlite3

#connect
connection=sqlite3.connect("student.db")

#create a cursor
cursor=connection.cursor()

#create table

table="""
Create table STUDENT(NAME VARCHAR(20),CLASS VARCHAR(20),SEC VARCHAR(25),MARKS INT)
"""

cursor.execute(table)

#insert record

cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A',90)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Darius', 'Data Science', 'B',100)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudhanshu', 'Devops', 'C',55)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikash', 'Data Science', 'C',35)''') 

print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 

connection.commit()
connection.close()