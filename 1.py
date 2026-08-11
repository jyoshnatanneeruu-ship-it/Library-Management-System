print("Library Management System")
import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-39P3H52\\SQLEXPRESS;"
    "Database=LibraryManagementSystem;"
    "Trusted_Connection=yes;"
)

print("Connected Successfully!")

import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-39P3H52\\SQLEXPRESS;"
    "Database=LibraryManagementSystem;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM Books")

for row in cursor:
    print(row)

conn.close()

import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-39P3H52\\SQLEXPRESS;"
    "Database=LibraryManagementSystem;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

bookid = int(input("Enter Book ID to delete: "))

cursor.execute(
    "DELETE FROM Books WHERE BookID=?",
    (bookid,)
)

conn.commit()

print("Book Deleted Successfully!")

conn.close()