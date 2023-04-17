from tkinter import *
from subprocess import call
from tkinter import Entry, Label, Tk, messagebox
from tkinter.ttk import Button
import tkinter as tk
import os

def login(t: Tk):
    list_of_files = os.listdir('account')
    entered_user = e1.get()
    entered_pass = e2.get()
    if f'{entered_user}.txt' in list_of_files:
        filepath = f'account\\{entered_user}.txt'
        file1 = open(filepath, "r")        
        verify = file1.read().splitlines()
        if entered_pass in verify:
            messagebox.showinfo("Login succesful","Logged in as staff")
            t.destroy()
            call(["python","admin.py"])
        else:
            messagebox.showerror("Login failed","Password not regconized")
    else:
       messagebox.showerror("Login failed","Invalid user or password")

log = Tk()
log.geometry("320x190")
log.title("Clothes Store")
log.configure(bg = 'silver')
log.resizable(False, False)

label = Label(log, bg = 'silver', fg = '#000000', text = "Clothes Store", font=('Britannic Bold',28))
label.place(x = 50, y = 10)

#password show-hide icon1
def show():
    hide_button = Button(log, image = hide_image, command = hide)
    hide_button.place(x = 230, y = 97)
    e2.config(show = '')

def hide():
    show_button = Button(log, image=show_image, command=show)
    show_button.place(x = 230, y = 97)
    e2.config(show='*')

hide_image = tk.PhotoImage(file = 'image\\hide_eye.png')
show_image = tk.PhotoImage(file = 'image\\show_eye.png')

show_button = Button(log, image = show_image, command = show)
show_button.place(x = 230, y = 97)
#end1

l1 = Label(log, bg = 'silver', fg = '#000000', text="Username")
l2 = Label(log, bg = 'silver', fg = '#000000', text="Password")

e1 = Entry(log)
e2 = Entry(log, show ='*')

bt = Button(log, text="Login",command=lambda: login(log))

l1.place(x = 40, y = 70)
l2.place(x = 40, y = 100)

e1.place(x = 100, y = 72)
e2.place(x = 100, y = 101)

bt.place(x = 120, y = 130)

log.mainloop()