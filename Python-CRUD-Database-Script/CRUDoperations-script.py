import sqlite3

# Connect to the database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   department TEXT NOT NULL,
                   salary REAL NOT NULL)''')

# Create record
def create_record(name, department, salary):
    cursor.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", (name, department, salary))
    conn.commit()
    print("Record created successfully")

# Read all records
def read_records():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Department:", row[2])
        print("Salary:", row[3])
        print("------------------------")

# Update record
def update_record():
    id = int(input("Enter the ID of the record you want to update: "))
    name = input("Enter the new name: ")
    department = input("Enter the new department: ")
    salary = float(input("Enter the new salary: "))
    cursor.execute("UPDATE employees SET name = ?, department = ?, salary = ? WHERE id = ?", (name, department, salary, id))
    conn.commit()
    print("Record updated successfully")

# Delete record
def delete_record():
    id = int(input("Enter the ID of the record you want to delete: "))
    cursor.execute("DELETE FROM employees WHERE id = ?", (id,))
    conn.commit()
    print("Record deleted successfully")

# Usage examples
create_record("John Doe", "IT", 5000)
create_record("Jane Smith", "Marketing", 6000)
read_records()
update_record()
read_records()
delete_record()
read_records()

# Close the connection
conn.close()
