import tkinter as tk 
from tkinter import messagebox


def calculate():
    try:
        number = int(entry.get())
        arr = []
        
        if number < 1 or number > 30:
            answer.config(text='out of range')
            entry.delete(0,tk.END)
            return
        else:
            arr = [i for i in range(number,0,-1)]
            # kung baliktaron napud,  arr = [i for i in range(1,number+1)]
        answer.config(text=arr)
        entry.delete(0,tk.END)
    except ValueError:
        messagebox.showerror('error','only numbers are allowed')
        entry.delete(0,tk.END)

root = tk.Tk()
root.geometry('500x500')
root.title('reverse from range something2')


label = tk.Label(root,text='Enter number from 1-30')
label.pack(pady=50)

entry = tk.Entry(root,width=10,justify = 'center')
entry.pack(pady=10)

button = tk.Button(root,text = 'touch me0', command = calculate)
button.pack()


answer = tk.Label(root,text='')
answer.pack(pady=50)

root.mainloop()