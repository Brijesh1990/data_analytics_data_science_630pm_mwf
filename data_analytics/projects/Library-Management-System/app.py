import sqlite3
import matplotlib.pyplot as plt 
import pandas as pd 
import openpyxl
# connection 
conn=sqlite3.connect("lms-app-db")
print("connection success")
# make choice 
print("---------press : 1 for add books category----------")
print("---------press : 2 for add Authers ----------")
print("---------press : 3 for add books ----------")
print("---------press : 4 for check books issued details ----------")
print("---------press : 5 for display all books----------")
print("---------press : 6 for delete books ----------")
print("---------press : 7 for update books details----------")
print("---------press : 0 for exit from proggrames----------")


while True :
    choice=int(input("enter your choice : "))
    