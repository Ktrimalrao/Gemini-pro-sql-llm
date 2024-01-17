import sqlite3

## connect to SQlite
connection = sqlite3.connect("student.db")

## Create cursor object to create table & insert record
cursor = connection.cursor()

## Create table
table_info = """
Create table STUDENT(NAME VARCHAR(20),
CLASS VARCHAR(10),SECTION VARCHAR(10),MARKS INT);
"""
cursor.execute(table_info)

## insert records
cursor.execute('''Insert into STUDENT values('Trimal','Data Science','D',94)''')
cursor.execute('''Insert into STUDENT values('Avinash','Data Engineering','D',93)''')
cursor.execute('''Insert into STUDENT values('Sai Ashish','ML Engineering','D',87)''')
cursor.execute('''Insert into STUDENT values('Hiranmahi','Data Science','C',90)''')
cursor.execute('''Insert into STUDENT values('Sagar','ML Engineering','A',81)''')
cursor.execute('''Insert into STUDENT values('Shalin','Data Engineering','B',75)''')
cursor.execute('''Insert into STUDENT values('Kartik','Data Science','C',92)''')
cursor.execute('''Insert into STUDENT values('Pavan','ML Engineering','D',88)''')

## Print all record
print("Data Inserted in table : ")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit change in the database
connection.commit()
connection.close()