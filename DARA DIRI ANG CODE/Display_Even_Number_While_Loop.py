import tkinter as tk
from tkinter import messagebox

def display_numbers():
    try:
        num = int(entry.get())
        choice = int(choice_var.get())
        if num < 1 or num > 20:
            raise ValueError("Number out of range")
        if choice not in [0, 1]:
            raise ValueError("Invalid choice")
        
        result = []
        if choice == 0:
            result = [i for i in range(1, num + 1) if i % 2 == 0]
        else:
            result = [i for i in range(1, num + 1) if i % 2 != 0]
        
        result_label.config(text="Output: " + " ".join(map(str, result)))
    except ValueError as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("Display Even or Odd Numbers")

tk.Label(app, text="Enter a number from 1-20:").pack()
entry = tk.Entry(app)
entry.pack()

tk.Label(app, text="Select 1-ODD or 0-EVEN:").pack()
choice_var = tk.StringVar()
choice_entry = tk.Entry(app, textvariable=choice_var)
choice_entry.pack()

tk.Button(app, text="Display", command=display_numbers).pack()

result_label = tk.Label(app, text="Output: ")
result_label.pack()

app.mainloop()