import tkinter as tk
from tkinter import messagebox

total = 0
def compute():
    global total
    
    try:
        num = int(entry.get())
        total = total + num
        messagebox.showinfo("Total", f"Total sum is {total}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

root = tk.Tk()
root.title("Total Sum Display")

label = tk.Label(root, text="Enter a number:")
label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

button = tk.Button(root, text="Compute")
button.grid(row=1, column=1, padx=10, pady=10)

button_1 = tk.Button(root, text="Clear")
button_1.grid(row=1, column=2, padx=10, pady=10)