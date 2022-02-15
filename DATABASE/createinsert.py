import sqlite3
from sqlite3 import Error
def sql_connection():
    try:
        conn=sqlite3.connect('Sales3.db')
        return conn
    except Error:
        print(Error)

def sql_table(conn):
    cursorObj=conn.cursor()
    cursorObj.execute("CREATE TABLE salesman(salesman_id n(5),name char(30),city char(20),commission decimal(7,2));")
    cursorObj.executescript("""
    INSERT INTO salesman VALUES(2001,'Vishu','Bangalore',0.15);
    INSERT INTO salesman VALUES(2002,'Mahi','Chennai',0.16);
    INSERT INTO salesman VALUES(2003,'SRK','Mumbai',0.17);
    INSERT INTO salesman VALUES(2004,'Dan','Wuhan',0.18);
    """)
    conn.commit()
    cursorObj.execute("SELECT * FROM salesman")
    rows=cursorObj.fetchall()
    print('Agent details:')
    for row in rows:
        print(row)

sqllite_conn=sql_connection()
sql_table(sqllite_conn)
if(sqllite_conn):
    sqllite_conn.close()
    print('\nSQLite connection is cosed')



# UPDATE

# import sqlite3
# from sqlite3 import Error
# def sql_connection():
#     try:
#       conn = sqlite3.connect('Sales1.db')
#       return conn
#     except Error:
#       print(Error)
# def sql_table(conn):
#     cursorObj = conn.cursor()  #Sales.db
#     #Current records in salesman table
#     cursorObj.execute("SELECT * FROM salesman")
#     rows = cursorObj.fetchall()
#     print("Agent details:")
#     for row in rows:
#         print(row)
#     print("\nUpdate commission .17 to .45 where id is 2003:")
#     sql_update_query = """Update salesman set commission = .45 where salesman_id = 2003"""
#     cursorObj.execute(sql_update_query)
#     conn.commit()
#     print("Record Updated successfully ")
#     cursorObj.execute("SELECT * FROM salesman")
#     rows = cursorObj.fetchall()
#     print("\nAfter updating Agent details:")
#     for row in rows:
#         print(row)
# sqllite_conn = sql_connection()
# sql_table(sqllite_conn)
# if (sqllite_conn):
#   sqllite_conn.close()
#   print("\nThe SQLite connection is closed.")



#DELETE

import sqlite3
from sqlite3 import Error
def sql_connection():
    try:
      conn = sqlite3.connect('Sales3.db')
      return conn
    except Error:
      print(Error)
def sql_table(conn):
    cursorObj = conn.cursor()  #Sales.db
    #Current records in salesman table
    cursorObj.execute("SELECT * FROM salesman")
    rows = cursorObj.fetchall()
    print("Agent details:")
    for row in rows:
        print(row)
    print("\nDelete name 'Dan' where salesman_id=2004:")
    sql_delete_query = """DELETE FROM salesman WHERE salesman_id = 2004"""
    cursorObj.execute(sql_delete_query)
    conn.commit()
    print("Record Deleted successfully ")
    cursorObj.execute("SELECT * FROM salesman")
    rows = cursorObj.fetchall()
    print("\nAfter deleting salesman details:")
    for row in rows:
        print(row)
sqlite_conn = sql_connection()
sql_table(sqlite_conn)
if (sqllite_conn):
  sqlite_conn.close()
  print("\nThe SQLite connection is closed.")

# COUNT ROWS
# import sqlite3
# from sqlite3 import Error
#
#
# def sql_connection():
#     try:
#         conn = sqlite3.connect('Sales2.db')
#         return conn
#     except Error:
#         print(Error)
#
#
# def sql_table(conn):
#     cursorObj = conn.cursor()
#
#     cursor = cursorObj.execute('select * from salesman;')
#     print(len(cursor.fetchall()))
#     # Insert records
#     cursorObj.executescript("""
#      INSERT INTO salesman VALUES(2001,'Vishu','Bangalore',0.15);
#     INSERT INTO salesman VALUES(2002,'Mahi','Chennai',0.16);
#     INSERT INTO salesman VALUES(2003,'SRK','Mumbai',0.17);
#     INSERT INTO salesman VALUES(2004,'Dan','Wuhan',0.18);
#     """)
#     conn.commit()
#     print("\nNumber of records after inserting rows:")
#     cursor = cursorObj.execute('select * from salesman;')
#     print(len(cursor.fetchall()))
#
#
# sqllite_conn = sql_connection()
# sql_table(sqllite_conn)
#
# if (sqllite_conn):
#     sqllite_conn.close()
#     print("\nThe SQLite connection is closed.")
