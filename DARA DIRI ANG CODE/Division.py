import tkinter as tk
from tkinter import messagebox

retries = 3

def divide_numbers():
    global retries  

    while retries > 0:
        try:
            num1 = float(num1_entry.get())
            num2 = float(num2_entry.get())

            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")

            result = num1 / num2
            messagebox.showinfo("Result", f"Result: {result}")
            retries = 3 
            break

        except ZeroDivisionError as e:
            retries -= 1
            messagebox.showerror("Error", f"{e}. Retries left: {retries}")
            if retries == 0:
                messagebox.showerror("Error", "No retries left.")
                divide_button.config(state=tk.DISABLED)
            return 
        
        except ValueError:
            retries -= 1
            messagebox.showerror("Invalid Input", f"Invalid input, please enter numbers. Retries left: {retries}")
            if retries == 0:
                messagebox.showerror("Error", "No retries left.")
                divide_button.config(state=tk.DISABLED)
            return  
        
        
root = tk.Tk()
root.title("Division App")

tk.Label(root, text="Enter the first number:").pack()
num1_entry = tk.Entry(root)
num1_entry.pack()

tk.Label(root, text="Enter the second number:").pack()
num2_entry = tk.Entry(root)
num2_entry.pack()

divide_button = tk.Button(root, text="Divide", command=divide_numbers)
divide_button.pack()

root.mainloop()