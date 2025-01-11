import tkinter as tk
from tkinter import messagebox

def start_countdown():
    try:
        countdown_time = int(entry.get())
        if countdown_time < 0:
            raise ValueError("Please enter a non-negative integer.")

        start_button.config(state=tk.DISABLED)

        while countdown_time >= 0:
            label.config(text=f"Time Left: {countdown_time}")
            root.update()
            root.after(1000)
            countdown_time -= 1

        label.config(text="Times Up!")
        messagebox.showinfo("Countdown Finished", "Times Up!")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    finally:
        start_button.config(state=tk.NORMAL)
        
root = tk.Tk()
root.title("Countdown Timer")

tk.Label(root, text="Enter a number for countdown:").pack()

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="Start", command=start_countdown)
start_button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()