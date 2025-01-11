from tkinter import *
from tkinter import messagebox
def submit():
	try:
		global items
		item = e1.get().strip()
		l.insert(END, item)
		items.append(item)
	except Exception:
		messagebox.showerror("Error", "Error")

def delete():
	try:
		global items
		item = e2.get().strip()
		if item in items:
			items.remove(item)
			index = l.get(0, END).index(item)
			l.delete(index)
		else:
			messagebox.showerror("Error", " Item cannot be found")
	except Exception:
		messagebox.showerror("Error", "Error")

def search():
	try:
		item = e3.get().strip()
		if item in items:
			messagebox.showinfo("Search", "Item Found")
		else:
			messagebox.showerror("Error", " Item cannot be found")
	except Exception:
		messagebox.showerror("Error", "Error")
	
	
items = []
r = Tk()
l = Listbox(r)
l.pack()
e1 = Entry(r)
e1.pack()
Button(r, text="Submit", command=submit).pack()
e2 = Entry(r)
e2.pack()
Button(r, text="Delete", command=delete).pack()
e3 = Entry(r)
e3.pack()
Button(r, text="Search", command=search).pack()
r.mainloop()

