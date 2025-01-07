from tkinter import *
from tkinter import simpledialog

prod = ["Onion Ring","Moby Choco","VCut Small","Nova Big","Coke Sakto", "Mineral Water 500"]
price = [10.00,10.00,15.00,35.00,20.00,25.00]

r = Tk()
l = Listbox(width=50, font=('Courier New',12))
l.pack()
l.insert(END, f"{'No':<10} {'Product':<28} {'Price':<10}")

for x,y in enumerate(prod,start=0):
    l.insert(END, f"{x+1:<10} {y:<29}{price[x]:.2f}")
ask = simpledialog.askinteger("","How many items purchase:")
s1 = []
s2 = []

for x in range(ask):
    a = simpledialog.askinteger("",f"Enter selected Item No.{x+1}")
    s1.append(prod[a-1])
    s2.append(price[a-1])
purch = Listbox(width=50, font=('Courier New',12))
purch.pack()
purch.insert(END, "Items Purchase:")
sum = 0

for x,y in enumerate(s1,start=0):
    purch.insert(END, f"{y:<28} {s2[x]:.2f}")
    sum+=s2[x]
    
vat = sum*.12
purch.insert(END, f"{'Vat 12%:':<28} {vat}")
purch.insert(END, f"{'Net:':<28} {sum-vat}")
purch.insert(END, f"{'Total Amount:':<28} {sum}")

r.mainloop()