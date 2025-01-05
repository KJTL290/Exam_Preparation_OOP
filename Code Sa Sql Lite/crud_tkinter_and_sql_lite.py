import tkinter as tk
from tkinter import messagebox
import sqlite3


conn = sqlite3.connect('crud_app.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL)''')
conn.commit()


def add_user():
    name = name_entry.get()
    age = age_entry.get()
    if name and age:
        c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        messagebox.showinfo("Success", "User added successfully")
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        display_users()
    else:
        messagebox.showwarning("Input Error", "Please enter both name and age")

def display_users():
    c.execute("SELECT * FROM users")
    records = c.fetchall()
    listbox.delete(0, tk.END)
    for record in records:
        listbox.insert(tk.END, f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}")

def delete_user():
    selected_user = listbox.get(tk.ACTIVE)
    if selected_user:
        user_id = selected_user.split(",")[0].split(":")[1].strip()
        c.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()
        messagebox.showinfo("Success", "User deleted successfully")
        display_users()
    else:
        messagebox.showwarning("Selection Error", "Please select a user to delete")


root = tk.Tk()
root.title("CRUD Application")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=10)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add User", command=add_user)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

listbox = tk.Listbox(root, width=50)
listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete User", command=delete_user)
delete_button.grid(row=4, column=0, columnspan=2, pady=10)

display_users()

root.mainloop()


conn.close()