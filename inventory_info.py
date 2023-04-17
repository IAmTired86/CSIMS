from tkinter import *
from tkinter import messagebox
from db import clothes_database
from clock import Clock

db = clothes_database('CSIMS.db')

def populate_list():
    clothes_list.delete(0, END)
    for row in db.fetch():
        clothes_list.insert(END, row)

def add_item():
    if name_text.get() == '' or color_text.get() == '' or size_text.get() == '' or stock_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Not Enough Fields', 'Please type in all fields')
        return
    db.insert (name_text.get(),color_text.get(),
              size_text.get(), stock_text.get(), price_text.get())
    clothes_list.delete(0, END)
    clothes_list.insert(END, (name_text.get(), color_text.get(), size_text.get(), stock_text.get(), price_text.get()))
    clear_text()
    populate_list()
    messagebox.showinfo('Success', 'Item added successfully')

def select_item(event):
    try:
        global selected_item
        index = clothes_list.curselection()[0]
        selected_item = clothes_list.get(index)
        name_entry.delete(0, END)
        name_entry.insert(END, selected_item[1])
        color_entry.delete(0, END)
        color_entry.insert(END, selected_item[2])
        size_entry.delete(0, END)
        size_entry.insert(END, selected_item[3])
        stock_entry.delete(0, END)
        stock_entry.insert(END, selected_item[4])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[5])
    except IndexError:
        pass

def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()
    messagebox.showinfo('Success', 'Item removed successfully')

def update_item():
    db.update(selected_item[0], name_text.get(), color_text.get(), size_text.get(), stock_text.get(), price_text.get())
    populate_list()
    messagebox.showinfo('Success', 'Item updated successfully')

def clear_text():
    name_entry.delete(0, END)
    color_entry.delete(0, END)
    size_entry.delete(0, END)
    stock_entry.delete(0, END)
    price_entry.delete(0, END)

# Create window object
inv = Tk()

# Name
name_text = StringVar()
name_label = Label(inv, text='Name', font=('Bahnschrift', 20), padx=20, pady=40, bg = '#3D3D3D', fg = 'gold')
name_label.grid(row=0, column=0, sticky=W)
name_entry = Entry(inv, textvariable=name_text, bg = 'lightgray')
name_entry.grid(row=0, column=1)
# Color
color_text = StringVar()
color_label = Label(inv, text='Color', font=('Bahnschrift', 20), padx=20, pady=40, bg = '#3D3D3D', fg = 'gold')
color_label.grid(row=0, column=2, sticky=W)
color_entry = Entry(inv, textvariable=color_text, bg = 'lightgray')
color_entry.grid(row=0, column=3)
# Size
size_text = StringVar()
size_label = Label(inv, text='Size', font=('Bahnschrift', 20), padx=20, pady=40, bg = '#3D3D3D', fg = 'gold')
size_label.grid(row=1, column=0, sticky=W)
size_entry = Entry(inv, textvariable=size_text, bg = 'lightgray')
size_entry.grid(row=1, column=1)
# Stock
stock_text = StringVar()
stock_label = Label(inv, text='Stock', font=('Bahnschrift', 20), padx=20, pady=40, bg = '#3D3D3D', fg = 'gold')
stock_label.grid(row=1, column=2, sticky=W)
stock_entry = Entry(inv, textvariable=stock_text, bg = 'lightgray')
stock_entry.grid(row=1, column=3)
# Price
price_text = StringVar()
price_label = Label(inv, text='Price', font=('Bahnschrift', 20), padx=20, pady=40, bg = '#3D3D3D', fg = 'gold')
price_label.grid(row=2, column=0, sticky=W)
price_entry = Entry(inv, textvariable=price_text, bg = 'lightgray')
price_entry.grid(row=2, column=1)
# Clothes List 
clothes_list = Listbox(inv, height=27, width=70, border=0, bg ='lightgray')
clothes_list.grid(row=0, column=4, columnspan=3, rowspan=6, padx=20, pady=20)
# Bind select
clothes_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(inv, text='Add', width = 12, height=3, command=add_item)
add_btn.grid(row=3, column=0)

remove_btn = Button(inv, text='Remove', width = 12, height=3,command=remove_item)
remove_btn.grid(row=3, column=1)

update_btn = Button(inv, text='Update Info', width = 12, height=3, command=update_item)
update_btn.grid(row=3, column=2)

clear_btn = Button(inv, text='Clear Input', width = 12, height=3, command=clear_text)
clear_btn.grid(row=3, column=3)

inv.title('Clothes Store Inventory Management')
inv.geometry('950x480')
inv.configure(bg='#3D3D3D')

clockLabel = Label(inv, font=('Haettenschweiler', 28, 'bold'), bg='#3D3D3D', fg='gold')
clockLabel.grid(row = 0, column = 8)
digital_clock = Clock(inv, clockLabel)

# Populate data
populate_list()

inv.mainloop()


