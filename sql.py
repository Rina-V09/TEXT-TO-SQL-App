import sqlite3

##Connect to sqlite
connection=sqlite3.connect("student.db")

##  Create a cursor object to insert record, create table and retrieve
cursor=connection.cursor()

table_info=""" 
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

## Insert some more records 

cursor.execute('''Insert Into STUDENT values('Krish', 'Data Science', 'A', 90)''')
cursor.execute('''Insert Into STUDENT values('Aryan', 'Computer Science', 'B', 85)''')
cursor.execute('''Insert Into STUDENT values('Neha', 'Mathematics', 'A', 92)''')
cursor.execute('''Insert Into STUDENT values('Rohan', 'Physics', 'C', 78)''')
cursor.execute('''Insert Into STUDENT values('Simran', 'Biotechnology', 'B', 88)''')
cursor.execute('''Insert Into STUDENT values('Vikram', 'Electronics', 'A', 80)''')
cursor.execute('''Insert Into STUDENT values('Priya', 'Mechanical', 'C', 95)''')
cursor.execute('''Insert Into STUDENT values('Karan', 'Data Science', 'B', 89)''')
cursor.execute('''Insert Into STUDENT values('Meera', 'Information Technology', 'A', 91)''')
cursor.execute('''Insert Into STUDENT values('Arjun', 'Civil Engineering', 'C', 84)''')
cursor.execute('''Insert Into STUDENT values('Sneha', 'Artificial Intelligence', 'B', 87)''')

##Display all the records
print("The inserted records are: ")

data=cursor.execute(''' Select * from STUDENT''')

for row in data:
    print(row)

## Close connection

connection.commit()
connection.close()
