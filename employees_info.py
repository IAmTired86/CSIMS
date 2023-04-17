from tkinter import *
from tkinter import messagebox
from db import employees_database
from clock import Clock

db = employees_database('CSIMS.db')

def populate_list():
    employees_list.delete(0, END)
    for row in db.fetch():
        employees_list.insert(END, row)

def add_item():
    if name_text.get() == '' or age_text.get() == '' or email_text.get() == '' or address_text.get() == '' or phone_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(name_text.get(), age_text.get(),
              email_text.get(), address_text.get(), phone_text.get())
    employees_list.delete(0, END)
    employees_list.insert(END, (name_text.get(), age_text.get(), email_text.get(), address_text.get(), phone_text.get()))
    clear_text()
    populate_list()
    messagebox.showinfo('Success', 'Employee added successfully')

def select_item(event):
    try:
        global selected_item
        index = employees_list.curselection()[0]
        selected_item = employees_list.get(index)
        name_entry.delete(0, END)
        name_entry.insert(END, selected_item[1])
        age_entry.delete(0, END)
        age_entry.insert(END, selected_item[2])
        email_entry.delete(0, END)
        email_entry.insert(END, selected_item[3])
        address_entry.delete(0, END)
        address_entry.insert(END, selected_item[4])
        phone_entry.delete(0, END)
        phone_entry.insert(END, selected_item[5])
    except IndexError:
        pass

def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()
    messagebox.showinfo('Success', 'Employee removed successfully')

def update_item():
    db.update(selected_item[0], name_text.get(), age_text.get(), email_text.get(), address_text.get(), phone_text.get())
    populate_list()
    messagebox.showinfo('Success', 'Employee updated successfully')

def clear_text():
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)
    phone_entry.delete(0, END)

# Create window object
emp = Tk()

# Name
name_text = StringVar()
name_label = Label(emp, text='Name', font=('Bahnschrift', 20), padx=20, pady=40, bg='#383838', fg='gold')
name_label.grid(row=0, column=0, sticky=W)
name_entry = Entry(emp, textvariable=name_text, bg = 'lightgrey')
name_entry.grid(row=0, column=1)
# Age
age_text = StringVar()
age_label = Label(emp, text='Age', font=('Bahnschrift', 20), padx=20, pady=40, bg='#383838', fg='gold' )
age_label.grid(row=0, column=2, sticky=W)
age_entry = Entry(emp, textvariable=age_text, bg = 'lightgrey')
age_entry.grid(row=0, column=3)
# Email
email_text = StringVar()
email_label = Label(emp, text='Email', font=('Bahnschrift', 20), padx=20, pady=40, bg='#383838', fg='gold')
email_label.grid(row=1, column=0, sticky=W)
email_entry = Entry(emp, textvariable=email_text, bg = 'lightgrey')
email_entry.grid(row=1, column=1)
# Address
address_text = StringVar()
address_label = Label(emp, text='Address', font=('Bahnschrift', 20), padx=20, pady=40, bg='#383838', fg='gold')
address_label.grid(row=1, column=2, sticky=W)
address_entry = Entry(emp, textvariable=address_text, bg = 'lightgrey')
address_entry.grid(row=1, column=3)
# Phone
phone_text = StringVar()
phone_label = Label(emp, text='Phone', font=('Bahnschrift', 20), padx=20, pady=40, bg='#383838', fg='gold')
phone_label.grid(row=2, column=0, sticky=W)
phone_entry = Entry(emp, textvariable=phone_text, bg = 'lightgrey')
phone_entry.grid(row=2, column=1)
# Clothes List 
employees_list = Listbox(emp, height=27, width=70, border=0, bg='lightgrey')
employees_list.grid(row=0, column=4, columnspan=3, rowspan=6, padx=20, pady=20)
# Bind select
employees_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(emp, text='Add', width=12, height=3, command=add_item)
add_btn.grid(row=3, column=0)

remove_btn = Button(emp, text='Remove', width=12, height=3, command=remove_item)
remove_btn.grid(row=3, column=1)

update_btn = Button(emp, text='Update Info', width=12, height=3, command=update_item)
update_btn.grid(row=3, column=2)

clear_btn = Button(emp, text='Clear Input', width=12, height=3, command=clear_text)
clear_btn.grid(row=3, column=3)

emp.title('Clothes Store Employees Management')
emp.geometry('1000x500')
emp.configure(bg='#383838')

# Clock
clockLabel = Label(emp, font=('Haettenschweiler', 28, 'bold'), bg='#383838', fg='gold')
clockLabel.grid(row = 0, column = 8)
digital_clock = Clock(emp, clockLabel)

# Populate data
populate_list()

emp.mainloop()

