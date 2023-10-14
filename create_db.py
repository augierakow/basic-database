import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('db.sqlite')

# Create a table
conn.execute('''CREATE TABLE IF NOT EXISTS items
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 description TEXT NOT NULL);''')
print("Table created successfully")  # Debug print

# Insert some sample data
conn.execute("INSERT INTO items (name, description) VALUES ('Item1', 'Description1')")
conn.execute("INSERT INTO items (name, description) VALUES ('Item2', 'Description2')")
print("Sample data inserted successfully")  # Debug print

# Commit changes and close
conn.commit()
conn.close()
