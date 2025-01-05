import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Mathematical Calculator")


def calculate():
    first_number = int(entry.get())
    second_number = int(entry_1.get())
    operation = str(entry_2.get())

    try:
        if operation == "+":
            result = first_number + second_number
            messagebox.showinfo("Result", f"The result is {result}")
        elif operation == "-": 
            result = first_number - second_number
            messagebox.showinfo("Result", f"The result is {result}")
        elif operation == "*":
            result = first_number * second_number
            messagebox.showinfo("Result", f"The result is {result}")
        elif operation == "/":
            if second_number == 0:
                messagebox.showerror("Error", "Division by zero is not allowed")
            else:
                result = first_number / second_number
                messagebox.showinfo("Result", f"The result is {result}")
        else:
            messagebox.showerror("Error", "Invalid Operation")
    
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")




label = tk.Label(root, text="First Number: ")
label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

label_1 = tk.Label(root, text="Second Number: ")
label_1.grid(row=1, column=0, padx=10, pady=10)

entry_1 = tk.Entry(root)
entry_1.grid(row=1, column=1, padx=10, pady=10)

label_2 = tk.Label(root, text="Chose Operation (+, -, *, /): ")
label_2.grid(row=2, column=0, padx=10, pady=10)

entry_2 = tk.Entry(root)
entry_2.grid(row=2, column=1, padx=10, pady=10)


button = tk.Button(root, text="Calculate" , command=calculate)
button.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()