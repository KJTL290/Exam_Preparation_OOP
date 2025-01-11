import tkinter as tk
from tkinter import messagebox

def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter an item.")

def delete_item():
    try:
        selected_item_index = listbox.curselection()[0]
        listbox.delete(selected_item_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select an item to delete.")

app = tk.Tk()
app.title("Listbox Add/Delete Demo")
app.geometry("300x400")

# Create and pack the listbox at the top
listbox = tk.Listbox(app, width=40, height=15)
listbox.pack(pady=10)

# Create bottom frame for entry and buttons
bottom_frame = tk.Frame(app)
bottom_frame.pack(pady=10)

# Create and pack the entry field
entry = tk.Entry(bottom_frame, width=30)
entry.pack(pady=5)

# Create and pack the buttons
add_button = tk.Button(bottom_frame, text="Add Item", command=add_item)
add_button.pack(pady=2)

delete_button = tk.Button(bottom_frame, text="Delete Item", command=delete_item)
delete_button.pack(pady=2)

app.mainloop()