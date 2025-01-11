import tkinter as tk
import time as t
from tkinter import messagebox

def count_down():
    if not ent_input.get():
        messagebox.showwarning("Empty Input", "Input field is blank. Please enter an input.")
              
    try: 
        time = int(ent_input.get())

        if time <= 0:
            raise ValueError

        while time != 0: # or [while time]
            t.sleep(1)
            time -= 1
        
        messagebox.showinfo("Finished", "Time's Up!")
    except:
        messagebox.showerror("Invalid Input", "Please enter a valid integer (positive whole numbers only).")

root = tk.Tk()

ent_input = tk.Entry(root)
btn_start = tk.Button(root, text="Start", command=count_down)

ent_input.pack()
btn_start.pack()

root.mainloop()