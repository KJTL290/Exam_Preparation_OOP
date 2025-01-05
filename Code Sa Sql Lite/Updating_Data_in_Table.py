import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Updating a single row
cursor.execute("UPDATE users SET age = 35 WHERE name = 'Alice'")

# Updating multiple rows at once
new_ages_data = [('Bob', 30), ('Charlie', 45)]
cursor.executemany("UPDATE users SET age = ? WHERE name = ?", new_ages_data)

conn.commit()
conn.close()