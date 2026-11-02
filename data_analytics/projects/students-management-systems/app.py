# connect with sqllite 
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl 

# connect with database 
conn = sqlite3.connect('sms_db')
print("Connected to database successfully")

# create a table in the database
cursor = conn.cursor()
# create a country table
cursor.execute('''CREATE TABLE IF NOT EXISTS country (
                    cid INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                    )''')

# create a state table
cursor.execute('''CREATE TABLE IF NOT EXISTS state (
                    sid INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    cid INTEGER,
                    FOREIGN KEY (cid) REFERENCES country(cid)
                    )''')

# create a city table

cursor.execute('''CREATE TABLE IF NOT EXISTS city (
                    cityid INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    sid INTEGER,
                    FOREIGN KEY (sid) REFERENCES state(sid)
                    )''')

# create a student table
cursor.execute('''CREATE TABLE IF NOT EXISTS student (
                    studentid INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    cid INTEGER,
                    sid INTEGER,
                    cityid INTEGER,
                    foreign key (cid) references country(cid),
                    foreign key (sid) references state(sid),
                    FOREIGN KEY (cityid) REFERENCES city(cityid)
                    )''')


conn.commit()
print('table created successfully')


# create to insert myltiple data in country table
insertCountry=[
    (1, 'USA'),
    (2, 'Canada'),
    (3, 'Mexico'),
    (4, 'UK')
]
cursor.executemany('''
                   insert or ignore into country(cid, name) values (?, ?)
                   
                   ''', insertCountry)

conn.commit()
print('data inserted successfully in country table')



# create to insert myltiple data in state table
insertState=[
    (1, 'California', 1),
    (2, 'Texas', 1),
    (3, 'Ontario', 2),
    (4, 'Quebec', 2),
    (5, 'Jalisco', 3),
    (6, 'Nuevo Leon', 3),
    (7, 'London', 4),
    (8, 'Manchester', 4)
]
cursor.executemany('''
                   insert or ignore into state (sid, name, cid) values (?, ?, ?)
                   
                   ''', insertState)

conn.commit()
print('data inserted successfully in state table')


# create to insert myltiple data in city table
insertCity=[
    (1, 'Los Angeles', 1),
    (2, 'San Francisco', 1),
    (3, 'Houston', 2),
    (4, 'Dallas', 2),
    (5, 'Toronto', 3),
    (6, 'Montreal', 4),
    (7, 'Guadalajara', 5),
    (8, 'Monterrey', 6),
    (9, 'London City', 7),
    (10, 'Manchester City', 8)
]
cursor.executemany('''
                   insert or ignore into city (cityid, name, sid) values (?, ?, ?)
                   
                   ''', insertCity)

conn.commit()
print('data inserted successfully in city table')



# stored data in students table

insertStudent=[
    (1, 'John Doe', 20, 1, 1, 1),
    (2, 'Jane Smith', 22, 1, 1, 2),
    (3, 'Michael Johnson', 21, 1, 2, 3),
    (4, 'Emily Davis', 23, 1, 2, 4),
    (5, 'William Brown', 19, 2, 3, 5),
    (6, 'Olivia Wilson', 20, 2, 3, 6),
    (7, 'James Taylor', 22, 2, 4, 6),
    (8, 'Sophia Anderson', 21, 3, 5, 7),
    (9, 'Benjamin Thomas', 23, 3, 6, 8),
    (10, 'Ava Martinez', 20, 4, 7, 9),
    (11, 'Ethan Lee', 21, 4, 8, 10)
    
]
cursor.executemany('''
                     insert or ignore into student (studentid, name, age, cid, sid, cityid) values (?, ?, ?, ?, ?, ?)
                     
                     ''', insertStudent)

conn.commit()
print('data inserted successfully in student table')


# display data from student table

print('==============display data from student table==============')
cursor.execute('SELECT * FROM student')
rows = cursor.fetchall()
for i in rows:
    print(i)
conn.commit()    
    
# display all data of students in dataframes  using pandas 
df=pd.read_sql("select * from student", conn)
print('==============display all data of students in dataframes  using pandas==============')
print(df)

conn.commit()


# display all data from students using join query with country, state and city table
print('==============display all data from students using join query with country, state and city table==============')
query = '''
   
   select student.*, country.name as country_name, state.name as state_name, city.name as city_name
   from student join country on student.cid = country.cid
   join state on student.sid = state.sid
   join city on student.cityid = city.cityid
   '''

df1=pd.read_sql(query, conn)
print(df1)
conn.commit()  


# generate all students data in excels file using pandas
query = '''
   
   select student.*, country.name as country_name, state.name as state_name, city.name as city_name
   from student join country on student.cid = country.cid
   join state on student.sid = state.sid
   join city on student.cityid = city.cityid
   '''
df1=pd.read_sql(query, conn)
generate_excels=df1.to_excel("students_list.xlsx", index=False, engine='openpyxl')
print('==============generate all students data in excels file using pandas==============')
print('students_list.xlsx file generated successfully')


# generate all students data in pdf file using pandas and matplotlib
query = '''

select student.*, country.name as country_name, state.name as state_name, city.name as city_name
   from student join country on student.cid = country.cid
    join state on student.sid = state.sid
    join city on student.cityid = city.cityid
   '''
   
# fetch data in pie chart using matplotlib

df2=pd.read_sql(query, conn)
# plt.pie(df2['age'], labels=df2['name'], autopct='%.1f%%', startangle=90)
plt.bar(df2['name'], df2['age'], color='skyblue')
plt.title('Students Age Distribution')
plt.xlabel('Students')
plt.ylabel('Age')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()