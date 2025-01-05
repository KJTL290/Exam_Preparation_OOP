import tkinter as tk
from tkinter import messagebox

attempts = 3

def verify_login():
    global attempts
    try:
        username = entry_username.get()
        password = entry_password.get()
        
        if username == "admin" and password == "password":
            messagebox.showinfo("Login", "Login Successful")
            root.destroy()  
        else:
            attempts -= 1
            if attempts > 0:
                messagebox.showerror("Login", f"Invalid Username or Password. {attempts} attempts left.")
            else:
                messagebox.showerror("Login", "No attempts left.")
                root.destroy() 
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


root = tk.Tk()
root.title("Login Verification")

label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)


label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)


button_login = tk.Button(root, text="Login", command=verify_login)
button_login.pack(pady=20)


root.mainloop()
