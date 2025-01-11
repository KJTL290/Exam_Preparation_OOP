import tkinter as tk
from tkinter import messagebox

def generate_pattern():
    try:
        user_input = int(entry.get())

        if 1 <= user_input <= 10:
            pattern = ""
            for i in range(1, user_input + 1):
                pattern += "*" * i + "\n"
            result_label.config(text=pattern)
        else:
            messagebox.showerror("Invalid Input", "Please enter a number between 1 and 10.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

root = tk.Tk()
root.title("Asterisk Pattern")
root.geometry("200x300")
root.config(bg="lightgray")

label = tk.Label(root, text="Enter a number from 1-10:", bg="lightgray")
label.pack(pady=20)

entry = tk.Entry(root)
entry.pack(pady=20)

submit_button = tk.Button(root, text="Generate Pattern", command=generate_pattern)
submit_button.pack(pady=10)

result_label = tk.Label(root, text="", justify="left", bg="lightgray")
result_label.pack(pady=10)

root.mainloop() #low-big
