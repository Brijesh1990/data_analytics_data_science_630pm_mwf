import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 
import openpyxl 
import mysql.connector
from mysql.connector import Error 
# create a database connection 
try:
    conn=mysql.connector.connect(
        
        host='127.0.0.1',
        port=3306,
        user='root',
        password='admin',
        database='crud_app_db' 
    )
    if conn.is_connected():
        print("database connection successfully")
        
        #create a table in database users
        cur=conn.cursor()
        cur.execute("""
                create table if not exists users(
                uid int primary key auto_increment,
                name varchar(255),
                age int,
                address text    
                    
                )
                """) 
        conn.commit()
        print('table successfully created')
    
        # insert data in tables
        insertData=[
        (1,'jay',24,'150 feet ring road rjt'),
        (2,'noori',25,'150 feet ring road rjt'),
        (3,'khusali',26,'150 feet ring road rjt'),
        (4,'rajesh',27,'150 feet ring road rjt'),
        (5,'mitesh',27,'150 feet ring road rjt'),
        (6,'kalpit',25,'150 feet ring road rjt')
        
        ] 
    
        cur.executemany("""
                    insert IGNORE INTO users values(%s,%s,%s,%s)
                    
                    """,insertData)
        conn.commit()
        print('data successfully added')
        
except Error as e:
    print("something went wrong while database connection",e)
     
