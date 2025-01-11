import tkinter as tk
from tkinter import messagebox

def generate_pattern():
    try:
        user_input = int(entry.get())

        if 1 <= user_input <= 10:
            pattern = ""
            for i in range(user_input, 0, -1):
                pattern += "*" * i + "\n"
            result_label.config(text=pattern)
        else:
            messagebox.showerror("Invalid Input", "Please enter a number between 1 and 10.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


root = tk.Tk()
root.title("Asterisk Pattern")

label = tk.Label(root, text="Enter a number from 1-10:")
label.pack()

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Generate Pattern", command=generate_pattern)
submit_button.pack()

result_label = tk.Label(root, text="", justify="left")# you guuys can change this if sa right or center ninyo butang pero left man naa sample
result_label.pack()

root.mainloop()