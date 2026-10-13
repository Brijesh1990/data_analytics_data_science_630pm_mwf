import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import openpyxl
# used sqllite3
import sqlite3
conn=sqlite3.connect("students_management_app")
print("connection successfully",conn)

# create a tables inside of sqlite3
cur=conn.cursor()
cur.execute(
    """ 
    create table if not exists users(
        uid integer primary key autoincrement,
        name text,
        email text,
        phone integer,
        address text,
        picode integer,
        country text,
        state text,
        city text
    )
    """
)

# create students tables 
cur.execute(
    """ 
    create table if not exists students(
        sid integer primary key autoincrement,
        name text,
        email text,
        phone integer,
        address text,
        picode integer,
        collegename text,
        department text,
        country text,
        state text,
        city text
    )
    """
)

# create feedback tables 
cur.execute(
    """ 
    create table if not exists feedback(
        fid integer primary key autoincrement,
        name text,
        email text,
        phone integer,
        comment text
         )
    """
)

# create employee tables 
cur.execute(
    """ 
    create table if not exists employee(
        empid integer primary key autoincrement,
        name text,
        email text,
        phone integer,
        address text,
        salary integer,
        department text,
        picode integer,
        country text,
        state text,
        city text
    )
    """
)

# create employee tables 
cur.execute(
    """ 
    create table if not exists country(
        cid integer primary key autoincrement,
        cname text,
        created_at text
    )
    """
)

# create employee tables 
cur.execute(
    """ 
    create table if not exists state(
        sid integer primary key autoincrement,
        sname text,
        created_at text
    )
    """
)

# create employee tables 
cur.execute(
    """ 
    create table if not exists city(
        ctid integer primary key autoincrement,
        ctname text,
        created_at text
    )
    """
)


# create category tables 
cur.execute(
    """ 
    create table if not exists category(
        catid integer primary key autoincrement,
        catname text
    )
    """
)


# create category tables 
cur.execute(
    """ 
    create table if not exists subcategory(
        subcatid integer primary key autoincrement,
        subcatname text
    )
    """
)


# create products tables 
cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        pid INTEGER PRIMARY KEY AUTOINCREMENT,
        pname TEXT,
        pimage TEXT,
        qty INTEGER,
        price INTEGER,
        catid INTEGER,
        subcatid INTEGER,
        descriptions TEXT,
        added_date TEXT,
        FOREIGN KEY (catid) REFERENCES category(catid),
        FOREIGN KEY (subcatid) REFERENCES subcategory(subcatid)
    )
""")

# save query 
conn.commit()
print("table successfully created",conn)
conn.close()
