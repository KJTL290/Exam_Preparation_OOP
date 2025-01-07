import tkinter as tk
from tkinter import messagebox

grocery_list = []

def create_window():
    window = tk.Tk()
    window.title("Grocery List Manager")
    return window

def add_item(entry, listbox):
    item = entry.get()
    if item:
        grocery_list.append(item)
        update_listbox(listbox)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter an item")

def delete_item(listbox):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        grocery_list.pop(index)
        update_listbox(listbox)

def update_listbox(listbox):
    listbox.delete(0, tk.END)
    for item in grocery_list:
        listbox.insert(tk.END, item)

# Create main window and widgets
window = create_window()

entry = tk.Entry(window)
entry.pack(pady=10)

listbox = tk.Listbox(window)
listbox.pack(pady=10)

add_button = tk.Button(window, text="Add Item", 
                      command=lambda: add_item(entry, listbox))
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Item", 
                         command=lambda: delete_item(listbox))
delete_button.pack(pady=5)

window.mainloop()