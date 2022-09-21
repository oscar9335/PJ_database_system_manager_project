import sqlite3

# Create a database or connect to one
conn = sqlite3.connect('petshop.db')

# create a cursor
cur = conn.cursor()

# create table
# do sql command in execute() 

# 以下建構所用到的5個table

cur.execute("""CREATE TABLE Animal(
            P_ID TEXT NOT NULL PRIMARY KEY,
            species TEXT NOT NULL,
            breed TEXT NOT NULL,
            age TEXT,
            gender TEXT NOT NULL,
            from_suppiler TEXT,
            in_date TEXT NOT NULL,
            out_date TEXT )""")

cur.execute("""CREATE TABLE Employee (
            ID_number TEXT NOT NULL PRIMARY KEY,
            name TEXT NOT NULL ,
            age TEXT NOT NULL,
            gender TEXT NOT NULL,
            address TEXT NOT NULL,
            salary TEXT NOT NULL,
            position TEXT NOT NULL,
            admit_date TEXT NOT NULL,
            phone TEXT NOT NULL)""")

cur.execute("""CREATE TABLE Member_Customer (
            member_ID TEXT NOT NULL PRIMARY KEY,
            name TEXT NOT NULL ,
            age TEXT NOT NULL,
            gender TEXT NOT NULL,
            address TEXT,
            pet_ID TEXT,
            phone TEXT NOT NULL,
            member_join_date TEXT NOT NULL)""")

cur.execute("""CREATE TABLE Suppiler (
            company_name TEXT NOT NULL PRIMARY KEY,
            manager TEXT NOT NULL ,
            address TEXT NOT NULL,
            phone TEXT NOT NULL)""")

cur.execute("""CREATE TABLE Product (
            product_name TEXT NOT NULL PRIMARY KEY,
            product_type TEXT NOT NULL ,
            price TEXT NOT NULL,
            suppiler_name TEXT NOT NULL,
            in_stock TEXT NOT NULL)""")



# commit change 
conn.commit()

# Close connection
conn.close()
