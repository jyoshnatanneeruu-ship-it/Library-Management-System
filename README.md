# Library Management System

A database-driven Library Management System developed using Python and SQL Server.

## Project Overview

This project is a menu-driven application designed to manage library book records efficiently. It uses Python for the application logic and SQL Server for storing and managing book data.

## Features

- Add new books
- View all books
- Search books by Book ID
- Update book quantity
- Delete book records
- Menu-driven interface
- SQL Server database integration

## Technologies Used

- Python
- SQL Server
- PyODBC
- Visual Studio Code

## Database

The project uses SQL Server with a `Books` table containing:

- BookID
- BookName
- Author
- Quantity

## CRUD Operations

- **Create** – Add new book records
- **Read** – View and search book records
- **Update** – Update book quantity
- **Delete** – Delete book records

## How to Run

1. Install Python.
2. Install PyODBC using:

   `pip install pyodbc`

3. Set up SQL Server.
4. Create the `LibraryManagementSystem` database.
5. Create the `Books` table.
6. Configure the SQL Server connection in the Python file.
7. Run the application using:

   `python library_management.py`

## Sample Menu

```text
===== Library Management System =====
1. Add Book
2. View Books
3. Search Book
4. Update Book Quantity
5. Delete Book
6. Exit
``` 
## Learning Outcomes

- Python programming and application development
- SQL Server and database management
- CRUD operations and database connectivity
- Git and GitHub version control

## Author

**Jyoshna Tanneeru**

Computer Science Student  
Interested in Python, SQL and Machine Learning