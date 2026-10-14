# sqlite is a database 
# sqlite is open source database 
# sqlite is inbuilt module in python 
# sqlite3 is default module support in python 
import sqlite3 
# create a connection with database sqlite3
conn=sqlite3.connect("students_management_systems")
# print("database connected successfully")
# create a schema of tables 
cur=conn.cursor()
# create a table users
cur.execute(
    """ 
    create table if not exists users(
        uid integer primary key autoincrement,
        username text,
        password text,
        mobile integer,
        gender text,
        hobby text,
        pincode integer,
        created_date text
    )
    
    """
)
# create a table country
cur.execute(
    """ 
    create table if not exists country(
        cid integer primary key autoincrement,
        cname text,
        created_date text
    )
        
    """
)

# create a table state
cur.execute(
    """ 
    create table if not exists state(
        sid integer primary key autoincrement,
        sname text,
        created_date text
    )
    
    """
)

# create a table city
cur.execute(
    """ 
    create table if not exists city(
        ctid integer primary key autoincrement,
        ctname text,
        created_date text
    )
    
    """
)

# create a normalization type of task based tables of category | subcategory | customers | colors | size | products | cart | orders

# ==============category===============
# catid(pk)      catname   created_date


# create a table category
cur.execute(
    """ 
    create table if not exists category(
        catid integer primary key autoincrement,
        catname text,
        created_date text
    )
    
    """
)

# create a table subcategory
cur.execute(
    """ 
    create table if not exists subcategory(
        subcatid integer primary key autoincrement,
        subcatname text,
        catid integer,
        foreign key(catid) references category(catid)
       
    )
    
    """
)


# ==============subcategory===============
# subcatid(pk)    catid(fk)  subcatname   created_date


# ==============colors===============
# colorid(pk)    colorname   created_date


# ==============size===============
# sizeid(pk)    sizename   created_date


# ==============customers===============
# customerid(pk)   name email password    age   mobile  address  

# ==============products===============

# pid(pk)  catid(fk)  subcatid(fk)  colorid(fk)  sizeid(fk) pname  qty  oldprice   offerprice  descriptions   created_at


# ==============cart===============

# cartid(pk)  pid(fk)  customerid(fk)   qty  subtotal     created_at
  
  
# ==============orders===============

# orderid(pk)  cartid(fk)  customerid(fk)   qty  subtotal  ordercode(uk)  status  created_at
  

# save table 
conn.commit()
print("table created successfully")
# closed connection 
conn.close()

