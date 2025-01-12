import tkinter as tk
from tkinter import messagebox

def find_index():
    try:
        tuple_input = tuple(map(int, entry_tuple.get().split(',')))
        element = int(entry_element.get())
        index = tuple_input.index(element)
        messagebox.showinfo("Result", f"Index: {index}")
    except ValueError:
        messagebox.showerror("Error", "Element not found or invalid input")


root = tk.Tk()
root.title("Tuple Index Finder")


label_tuple = tk.Label(root, text="Input Tuple (comma separated):")
label_tuple.pack()

entry_tuple = tk.Entry(root)
entry_tuple.pack()

label_element = tk.Label(root, text="Element to search:")
label_element.pack()

entry_element = tk.Entry(root)
entry_element.pack()

button_search = tk.Button(root, text="Search", command=find_index)
button_search.pack()


root.mainloop()