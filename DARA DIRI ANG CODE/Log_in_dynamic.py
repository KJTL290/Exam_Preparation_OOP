import tkinter as tk
from tkinter import messagebox


attempts = 3

def verify_credentials():
    global attempts

    entered_username = username_entry.get()
    entered_password = password_entry.get()

    correct_username = dynamic_username_entry.get()
    correct_password = dynamic_password_entry.get()

    if entered_username == correct_username and entered_password == correct_password:
        messagebox.showinfo("Success", "Login successful!")
        submit_button.config(state=tk.DISABLED)  
    else:
        attempts -= 1
        if attempts > 0:
            messagebox.showerror("Failed", f"Invalid credentials. You have {attempts} attempt(s) left.")
        else:
            messagebox.showerror("Failed", "Invalid credentials. You have no attempts left.")
            submit_button.config(state=tk.DISABLED) 



root = tk.Tk()
root.title("Login System")

dynamic_username_label = tk.Label(root, text="Set Username:")
dynamic_username_label.pack()

dynamic_username_entry = tk.Entry(root)
dynamic_username_entry.pack()

dynamic_password_label = tk.Label(root, text="Set Password:")
dynamic_password_label.pack()

dynamic_password_entry = tk.Entry(root, show="*")
dynamic_password_entry.pack()

username_label = tk.Label(root, text="Enter Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Enter Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

submit_button = tk.Button(root, text="Login", command=verify_credentials)
submit_button.pack()

root.mainloop()