import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute a SQL command to create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS usersp (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER
                )''')

# Insert data into the table
cursor.execute("INSERT INTO usersp (name, age) VALUES (?, ?)", ('John', 30))
cursor.execute("INSERT INTO usersp (name, age) VALUES (?, ?)", ('Jane', 25))

# Commit the transaction
conn.commit()

# Query data from the table
cursor.execute("SELECT * FROM usersp")
rows = cursor.fetchall()

# Print the retrieved data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
