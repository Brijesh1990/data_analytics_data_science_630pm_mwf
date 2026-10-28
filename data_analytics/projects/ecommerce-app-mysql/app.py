import mysql.connector
import pandas as pd
from mysql.connector import Error
import openpyxl
# create a database 
try:
    # conn=mysql.connector.connect(
    # host="localhost",
    # user="root",
    # password="admin",
    # database="ecommerce-app-db"
    # )
    # print("database connect successfully")
    
    conn=mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",    
        password="admin",
        database="ecommerce-app-db"
        )
    print("database connect successfully")
    
    cur=conn.cursor()
    # create a table 
    cur.execute("""
                create table if not exists country(
                    cid int primary key auto_increment,
                    cname varchar(255),
                    created_at timestamp default current_timestamp
                    
                )
                
                """)
    
    cur.execute("""
                    create table if not exists state(
                        sid int primary key auto_increment,
                        sname varchar(255),
                        cid int,
                        foreign key(cid) references country(cid),
                        created_at timestamp default current_timestamp
                        
                    )
                    
                    """)
    
    
    cur.execute("""
                        create table if not exists city(
                            ctid int primary key auto_increment,
                            ctname varchar(255),
                            sid int,
                            foreign key(sid) references state(sid),
                            created_at timestamp default current_timestamp
                            
                        )
                        
                        """)
    
    
    cur.execute("""
                            create table if not exists students(
                                studentid int primary key auto_increment,
                                name varchar(255),
                                age int,
                                mobile bigint,
                                address text,
                                
                                cid int,
                                foreign key(cid) references country(cid),
                                
                                sid int,
                                foreign key(sid) references state(sid),
                                
                                ctid int,
                                foreign key(ctid) references city(ctid),
                                                                                            
                                created_at timestamp default current_timestamp
                                
                            )
                            
                            """)
    # save query
    print("table successfully created")
  
    # create a case based question 
    print("----Press 1 for add Students :------")
    print("----Press 2 for display all data :-----")
    print("----Press 3 for generate data in excel :-----")
    while True:
        choice=int(input("Enter your choice :"))
        if choice==1:
            
            name=input("Enter your Name :")
            age=int(input("Enter your Age :"))
            mobile=input("Enter your Mobile :")
            address=input("Enter your Address :")
            cid=int(input("Enter your country :"))
            sid=int(input("Enter your state :"))
            ctid=int(input("Enter your City :"))
           
            #insert a data
            data=(name,age,mobile,address,cid,sid,ctid)
            cur.execute("""
                        insert into students(name,age,mobile,address,cid,sid,ctid) values(%s,%s,%s,%s,%s,%s,%s)
                        """,data)
            conn.commit()   
            print("students added successfully")
            
            
        elif choice==2:
            # select="select * from students"
            # df=pd.read_sql_query(select,conn)
            
            select="select students.*,cname,sname,ctname from students join country on students.cid=country.cid join state on students.sid=state.sid join city on students.ctid=city.ctid"
            df=pd.read_sql_query(select,conn)
            print("=======================================================================")
            print(df)
        elif choice==3:
             select="select students.*,cname,sname,ctname from students join country on students.cid=country.cid join state on students.sid=state.sid join city on students.ctid=city.ctid"
             df=pd.read_sql_query(select,conn)
            
             generate_excels=df.to_excel("students_data.xlsx", engine="openpyxl", index=False)
             print("excels generated successfully",generate_excels)    
        else: 
            break
        conn.close()
            
except Exception as e:
    print("something went wrong",e)
