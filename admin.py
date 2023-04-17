# import tkinter library as tk and some of its other modules
import tkinter as tk
from tkinter import *
from subprocess import call
from tkinter import Entry, Label, Tk, messagebox
from tkinter.ttk import Button

# create an instance of Tkinter as root window
root = tk.Tk()

# set the dimensions of the window
root.geometry("600x400")

# set the title of the window
root.title("Clothes Store Management App")

# set the background color of the window
root.configure(bg = '#383838')

# make the window size fixed
root.resizable(False, False)

# function that destroys the current window and calls the login.py file
def log_out():
    root.destroy()
    call(["python","login.py"])

# function that destroys the current window and calls the inventory_info.py file
def product_info():
    root.destroy()
    call(["python","inventory_info.py"])

# function that destroys the current window and calls the employees_info.py file
def employee_info():
    root.destroy()
    call(["python","employees_info.py"])

# function that destroys the current window and calls the order.py file
def order():
    root.destroy()
    call(["python","order.py"])

# create a label with specified text, font, foreground/background color and anchor position
label = tk.Label(root, text="Clothes Store Management", bg = '#383838', fg = 'gold', font=('Aharoni',30), anchor = "center")
label.pack()

# create button with specified text, foreground/background color, font, command to execute on click and relief style
btn = tk.Button(root, text = "Products Information", bg = '#383838', fg = 'gold', font = ("Bahnschrift", 20),command= product_info, relief=GROOVE)
btn.place(x = 170, y = 70)

# create button with specified text, foreground/background color, font, command to execute on click and relief style
btn2 = tk.Button(root, text = "Employees Information", bg = '#383838', fg = 'gold', font = ("Bahnschrift", 20),command = employee_info, relief=GROOVE)
btn2.place(x = 160, y = 150)

# create button with specified text, foreground/background color, font, command to execute on click and relief style
btn3 = tk.Button(root, text = "Make Orders", bg = '#383838', fg = 'gold', font = ("Bahnschrift", 20), command = order, relief=GROOVE)
btn3.place(x = 220, y = 230)

# create button with specified text, foreground/background color, font, command to execute on click and relief style
bt4 = tk.Button(root, text = "Log out", bg = '#383838', fg = 'gold', font = ("Bahnschrift", 20), command = log_out, relief=GROOVE)
bt4.place(x = 250, y = 310)

# keep the window running until it is closed
root.mainloop()
