import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Creating the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Inserting a single row
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")

# Inserting multiple rows at once
users_data = [('Bob', 25), ('Charlie', 40)]
cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users_data)

conn.commit()
conn.close()