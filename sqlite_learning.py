import sqlite3

## connect to an SQLite database
connection = sqlite3.connect('example.db')
connection
cursor = connection.cursor()

## Create a Table
cursor.execute('''
Create Table if Not Exists employees(
    id Integer Primary Key,
    name Text Not Null,
    age Integer,
    deppartment text
)
''')
connection.commit()

cursor.execute('''
               Insert into employees(name,age,deppartment)
               values ('Ram',27,'QA')
               ''')
cursor.execute('''
               Insert into employees(name,age,deppartment)
               values ('Sandeep',37,'DEV')
               ''')
cursor.execute('''
               Insert into employees(name,age,deppartment)
               values ('Arun',27,'DevOps')
               ''')
cursor.execute('''
               Insert into employees(name,age,deppartment)
               values ('Prabhu',40,'Lead')
               ''')
cursor.execute('''
               Insert into employees(name,age,deppartment)
               values ('Lynn',34,'Lead')
               ''')

connection.commit()

cursor.execute('''
               Select * from employees
               ''')


rows = cursor.fetchall()

for row in rows:
    print(row)
    
    
cursor.execute('''
               Update employees
               set age=26 where name="Ram"
               ''')

connection.commit()
print("===================================================================================================================================")
cursor.execute('''
               Select * from employees
               ''')

rows = cursor.fetchall()

for row in rows:
    print(row)
    
    
connection.close()