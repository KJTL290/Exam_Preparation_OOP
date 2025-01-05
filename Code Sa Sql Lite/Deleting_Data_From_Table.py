import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Deleting a single row
cursor.execute("DELETE FROM users WHERE name = 'Alice'")

# Deleting multiple rows at once
names_to_delete = [('Bob',), ('Charlie',)]
cursor.executemany("DELETE FROM users WHERE name = ?", names_to_delete)

conn.commit()
conn.close()