import pyodbc

# SQL Server Connection
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-39P3H52\\SQLEXPRESS;"
    "Database=LibraryManagementSystem;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()


# 1. Add Book
def add_book():
    bookid = int(input("Enter Book ID: "))
    bookname = input("Enter Book Name: ")
    author = input("Enter Author: ")
    quantity = int(input("Enter Quantity: "))

    cursor.execute(
        "INSERT INTO Books VALUES (?, ?, ?, ?)",
        (bookid, bookname, author, quantity)
    )

    conn.commit()
    print("Book Added Successfully!")


# 2. View Books
def view_books():
    cursor.execute("SELECT * FROM Books")

    print("\n===== All Books =====")

    for row in cursor:
        print(row)


# 3. Search Book
def search_book():
    bookid = int(input("Enter Book ID to search: "))

    cursor.execute(
        "SELECT * FROM Books WHERE BookID = ?",
        (bookid,)
    )

    row = cursor.fetchone()

    if row:
        print("\nBook Found:")
        print(row)
    else:
        print("Book Not Found")


# 4. Update Book Quantity
def update_book():
    bookid = int(input("Enter Book ID: "))
    quantity = int(input("Enter New Quantity: "))

    cursor.execute(
        "UPDATE Books SET Quantity = ? WHERE BookID = ?",
        (quantity, bookid)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Book Updated Successfully!")
    else:
        print("Book Not Found")


# 5. Delete Book
def delete_book():
    bookid = int(input("Enter Book ID to delete: "))

    cursor.execute(
        "DELETE FROM Books WHERE BookID = ?",
        (bookid,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Book Deleted Successfully!")
    else:
        print("Book Not Found")


# Main Menu
while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book Quantity")
    print("5. Delete Book")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_book()

    elif choice == 2:
        view_books()

    elif choice == 3:
        search_book()

    elif choice == 4:
        update_book()

    elif choice == 5:
        delete_book()

    elif choice == 6:
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid Choice")


conn.close()