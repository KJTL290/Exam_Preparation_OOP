import tkinter as tk
from tkinter import messagebox

def pass_or_fail():
    try:
        score = entry.get()
        
        score = int(score)
        if not (1 <= score <= 20):
            raise ValueError("Score out of range")

        message = ["I passed the exam" for _ in range(score)]

        messagebox.showinfo("Result", "\n".join(message))
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number between 1 and 20.")

#tkinter area kamo na bahala butangan pa ninyo designs or centered ba chuchuness basic rani akoa
root = tk.Tk()
root.title("Score App")

label = tk.Label(root, text="Enter your score (1 - 20):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Submit", command=pass_or_fail)
button.pack(pady=10)

root.mainloop()