import tkinter as tk
from tkinter import messagebox


def display_whole_number():

    try:
        input_value = int(entry.get())
        if input_value <= 10 and input_value >= 1:
            x = 1
            result = " "
            while x <= input_value:
                result = str(result) + str(x) + " "
                x += 1
                messagebox.showinfo("Result", f"{result}")
        else:
            messagebox.showerror("Error", "Please enter a valid Input")
    except ValueError:
        messagebox.showerror("Error", "Please Enter a valid Input")




root = tk.Tk()
root.title("Display a Whole Number")

label = tk.Label(root, text="Enter a whole number from 1-10: ")
label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

button = tk.Button(root, text="Enter", command=display_whole_number)
button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()