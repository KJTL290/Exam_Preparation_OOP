import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Display Even Number")

def display_input():
    try:

        num = int(entry.get())
        x = 1
        result = ""
        while x <= num:
            if x % 2 == 0:
                result = str(result) + str(x) + "\n"
                x += 1
        messagebox.showinfo("Result", f"{result}")
            
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid whole number")

def clear():
    entry.delete(0, tk.END) 


label = tk.Label(root, text="Enter a whole number:")
label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

button = tk.Button(root, text="Compute", command=display_input)
button.grid(row=1, column=1, padx=10, pady=10)

button_1 = tk.Button(root, text="Clear", command=clear)
button_1.grid(row=1, column=2, padx=10, pady=10)    

root.mainloop()