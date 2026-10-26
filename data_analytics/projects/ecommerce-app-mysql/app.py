import mysql.connector
from mysql.connector import Error
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
                    created_at date
                    
                )
                
                """)
    
    cur.execute("""
                    create table if not exists state(
                        sid int primary key auto_increment,
                        sname varchar(255),
                        cid int,
                        foreign key(cid) references country(cid),
                        created_at date
                        
                    )
                    
                    """)
    
    
    cur.execute("""
                        create table if not exists city(
                            ctid int primary key auto_increment,
                            ctname varchar(255),
                            sid int,
                            foreign key(sid) references state(sid),
                            created_at date
                            
                        )
                        
                        """)
    # save query
    print("table successfully created")
    conn.commit()    
    conn.close()
    
    
except Exception as e:
    print("something went wrong",e)
