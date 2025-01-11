import tkinter as tk
from tkinter import messagebox

def start_countdown():
    try:
        seconds = max(0, int(entry.get()))
        while seconds >= 0:
            label.config(text=f"Time: {seconds}s")
            root.update()
            root.after(1000)
            seconds -= 1
            seconds == 10 and messagebox.showwarning("Warning", "10s left!")
        messagebox.showinfo("Done", "Time's up!")
    except ValueError:
        messagebox.showerror("Error", "Enter valid number!")

root = tk.Tk()
root.title("Timer")
label = tk.Label(root, font=("Arial", 12))
entry = tk.Entry(root)
tk.Button(root, text="Start", command=start_countdown).pack()
[w.pack() for w in (label, entry)]
root.mainloop()