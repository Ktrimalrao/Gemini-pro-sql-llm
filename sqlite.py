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
cursor.execute('''Insert into STUDENT values('Alex', 'Data Science', 'D', 94)''')
cursor.execute('''Insert into STUDENT values('John', 'Data Engineering', 'D', 93)''')
cursor.execute('''Insert into STUDENT values('Mike', 'ML Engineering', 'D', 87)''')
cursor.execute('''Insert into STUDENT values('David', 'Data Science', 'C', 90)''')
cursor.execute('''Insert into STUDENT values('Chris', 'ML Engineering', 'A', 81)''')
cursor.execute('''Insert into STUDENT values('Sam', 'Data Engineering', 'B', 75)''')
cursor.execute('''Insert into STUDENT values('Jack', 'Data Science', 'C', 92)''')
cursor.execute('''Insert into STUDENT values('Daniel', 'ML Engineering', 'D', 88)''')

## Print all record
print("Data Inserted in table : ")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit change in the database
connection.commit()
connection.close()