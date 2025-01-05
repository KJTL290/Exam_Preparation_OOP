import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Retrieving all data from the table
cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()
for user in all_users:
    print(user)

# Retrieving specific columns from the table
cursor.execute("SELECT name, age FROM users")
names_and_ages = cursor.fetchall()
for name, age in names_and_ages:
    print(name, age)

# Retrieving data with a condition (e.g., age greater than 30)
cursor.execute("SELECT * FROM users WHERE age > 30")
users_over_30 = cursor.fetchall()
for user in users_over_30:
    print(user)

conn.close()