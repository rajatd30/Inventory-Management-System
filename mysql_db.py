import mysql.connector
def create_db():
    con=mysql.connector.connect(host="localhost", username="root", password="1234", database="lims")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid int NOT NULL PRIMARY KEY AUTO_INCREMENT,name varchar(20), email varchar(30), gender varchar(6), contact varchar(10), dob varchar(10), doj varchar(10), pass varchar(20), utype varchar(10), address varchar(30), salary varchar(8))")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice int NOT NULL PRIMARY KEY AUTO_INCREMENT,name varchar(20), contact int(10), description varchar(40))")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS category(cid int NOT NULL PRIMARY KEY AUTO_INCREMENT,name varchar(20))")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS product(pid int NOT NULL PRIMARY KEY AUTO_INCREMENT,Category varchar(20), Supplier varchar(30), name varchar(20), price varchar(10), qty varchar(10), status varchar(10))")
    con.commit()
    
create_db()