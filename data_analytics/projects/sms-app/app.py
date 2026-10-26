import sqlite3
# connection with sqlite 
conn=sqlite3.connect("sms-db-app-sqlite")
print("connection successfully stablished")
# create table schema 
cur=conn.cursor()
cur.execute("""
            create table if not exists college(
                
                collegeid integer primary key autoincrement,
                collegename text
            )
            
            """)
cur.execute("""
            create table if not exists department(
                
                depeid integer primary key autoincrement,
                depname text
            )
            
            """)
cur.execute("""
            create table if not exists faculty(
                
                facultyid integer primary key autoincrement,
                facultyname text
            )
            
            """)

cur.execute("""
            create table if not exists students(
                sid integer primary key autoincrement,
                name text,
                age integer,
                address text,
                collegeid integer,
                depid integer,
                facultyid integer,
                foreign key(collegeid) references college(collegeid),
                foreign key(depid) references department(depid),
                foreign key(facultyid) references faculty(facultyid)
            )
            
            """)

conn.commit()
conn.close()
