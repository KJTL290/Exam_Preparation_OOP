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

# Create the main window
root = tk.Tk()
root.title("Login Verification")

# Create and place the username label and entry
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Create and place the password label and entry
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Create and place the login button
button_login = tk.Button(root, text="Login", command=verify_login)
button_login.pack(pady=20)

# Run the application
root.mainloop()
# Without GUI - Console-based login verification
while attempts > 0:
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username == "admin" and password == "password":
            print("Login Successful")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Invalid Username or Password. {attempts} attempts left.")
            else:
                print("No attempts left. Exiting.")
    except Exception as e:
        print(f"An error occurred: {e}")
        attempts -= 1