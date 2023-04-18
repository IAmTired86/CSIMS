import tkinter as tk
from tkinter import *
from subprocess import call
from tkinter import Entry, Label, Tk, messagebox
from tkinter.ttk import Button


root = tk.Tk()

root.geometry("600x400")
root.title("Clothes Store Management App")
root.configure(bg = '#383838')
root.resizable(False, False)


def log_out():
    root.destroy()
    call(["python","login.py"])

def product_info():
    root.destroy()
    call(["python","inventory_info.py"])

def employee_info():
    root.destroy()
    call(["python","employees_info.py"])

def order():
    root.destroy()
    call(["python","order.py"])

label = tk.Label(root, text="Clothes Store Management", bg = '#383838', fg = 'gold', font=('Aharoni',30), anchor = "center")
label.pack()

btn = tk.Button(root, text = "Products Information", bg = '#383838', fg = 'gold', font = ("Bahnschrift", 20),command= product_info, relief=GROOVE)
btn.place(x = 170, y = 70)


btn2 = tk.Button(root, text = "Employees Information", bg = '#383838', fg = 'gold', font = ("Bahnschrift", 20),command = employee_info, relief=GROOVE)
btn2.place(x = 160, y = 150)


btn3 = tk.Button(root, text = "Make Orders", bg = '#383838', fg = 'gold', font = ("Bahnschrift", 20), command = order, relief=GROOVE)
btn3.place(x = 220, y = 230)

bt4 = tk.Button(root, text = "Log out", bg = '#383838', fg = 'gold', font = ("Bahnschrift", 20), command = log_out, relief=GROOVE)
bt4.place(x = 250, y = 310)

root.mainloop()