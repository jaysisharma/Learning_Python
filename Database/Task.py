# Task: Create a Python script to manage a simple employee database using SQLite.

# Steps to accomplish the task:

# Create a SQLite database named employee.db with a table named employees. The table should have the following columns:
# id (INTEGER, PRIMARY KEY)
# name (TEXT)
# age (INTEGER)
# department (TEXT)
# Implement functions to perform CRUD (Create, Read, Update, Delete) operations on the employees table:
# Create a new employee record
# Read employee records
# Update employee records
# Delete employee records
# Provide a command-line interface (CLI) for users to interact with the database:
# Display a menu with options to add, view, update, or delete employee records
# Accept user input to perform the selected operation
# Implement error handling to handle invalid input and database errors gracefully.


import sqlite3 as sq

def connect_to_database(database_name):
    """Connects to the SQLite database."""
    return sq.connect(database_name)

def create_employee_table(connection):
    """Creates the 'employee' table if it doesn't exist."""
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employee (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   age INTEGER NOT NULL,
                   department TEXT NOT NULL
    )''')
    connection.commit()
    cursor.close()

def add_employee(connection, id, name, age, department):
    """Adds an employee to the database."""
    cursor = connection.cursor()
    cursor.execute("INSERT INTO employee (id, name, age, department) VALUES (?, ?, ?, ?)", (id, name, age, department))
    connection.commit()
    cursor.close()

def view_employees(connection):
    """Displays all employees in the database."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()

def update_employee(connection, emp_id, new_name, new_dept):
    """Updates the name and department of an employee."""
    cursor = connection.cursor()
    cursor.execute("UPDATE employee SET name = ?, department = ? WHERE id = ?", (new_name, new_dept, emp_id))
    connection.commit()
    cursor.close()

def delete_employee(connection, emp_id):
    """Deletes an employee from the database."""
    cursor = connection.cursor()
    cursor.execute("DELETE FROM employee WHERE id = ?", (emp_id,))
    connection.commit()
    cursor.close()

def main():
    conn = connect_to_database('employee.db')
    create_employee_table(conn)

    while True:
        print("Employee Database Management System")

        print('''
1. Add Employee
2. View Employee
3. Update Employee
4. Delete Employee
5. Exit
        ''')
        user = int(input("Select an option: "))

        if user == 1:
            print("Add Employee Details")
            id = int(input("Enter the Employee id: "))
            name = input("Enter the employee name: ")
            age = int(input("Enter the employee age: "))
            dept = input("Enter the department: ")
            add_employee(conn, id, name, age, dept)
            print("Employee added Successfully")

        elif user == 2:
            print('''
===========================================================================
              Employee list
              ''')
            view_employees(conn)
            print("===========================================================================")
        
        elif user == 3:
            print("Enter the details to update")
            emp_id = int(input("Enter the employee id "))
            up_name = input("Enter the new name: ")
            up_dept = input("Enter the new Department: ")
            update_employee(conn, emp_id, up_name, up_dept)
            print("Record Updated Successfully")
        
        elif user == 4:
            print('''
===========================================================================
              Employee list
              ''')
            view_employees(conn)
            print("===========================================================================")
            emp_id = int(input("Enter the employee id to delete: "))
            choice = input("Are you sure you want to delete the employee (y/n)? ")
            if choice.lower() == 'y':
                delete_employee(conn, emp_id)
                print("Employee Deleted Successfully")
                print('''
===========================================================================
              Updated Employee list
              ''')
                view_employees(conn)
                print("===========================================================================")
            else:
                print("Deletion Cancelled")
        
        elif user == 5:
            print("Exiting...")
            break
        
        else:
            print("Invalid Input")

    conn.close()

if __name__ == "__main__":
    main()
