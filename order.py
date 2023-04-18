import tkinter as tk
from tkinter import *
from subprocess import call
from tkinter import Entry, Label, Tk, messagebox
from tkinter.ttk import Button
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter import Text
import os
from os import startfile
import sqlite3
from datetime import date
import random


day = date.today()


con = sqlite3.connect('CSIMS.db')
cur = con.cursor()

product_id = []
product_name = []
product_color = []
product_size = []
product_price = []
product_quantity = []



window = Tk()
window.title("Clothes Store")
window.geometry("645x500")
window.configure(bg = '#3D3D3D')
window.resizable(False, False)
#background image
bgimg = tk.PhotoImage(file = 'Image\hidden.png')
limg = Label(window, i = bgimg)
limg.pack()

output_text = StringVar()

#populate list
global get_price

#Log out
def log_out():
    window.destroy()
    call(["python","admin.py"])


#Add to cart
def atc():
    global data_color, data_quantity, data_size, data_type, get_price, get_stock, get_id, get_name, get_color, get_size, get_price, total, pc
    data_quantity = int(quantity_sb.get())
    data_color = color.get()
    data_size = size.get()
    data_type = output_text.get("1.0","end-1c").strip()   
    query = "SELECT * from clothes where name = ? and color = ? and size = ?"
    result = cur.execute(query, (data_type, data_color, data_size))
    pc = result.fetchall()
    length = len(pc)
    if data_type == '':
        messagebox.showerror('Required Fields', 'Please choose an item')
        return
    if length == 0:
        messagebox.showerror('Not in stock', 'We do not have this item in stock')
        return
    for r in pc:
        get_id = r[0]
        get_name = r [1]
        get_color = r [2]
        get_size = r [3]
        get_stock = r[4]
        get_price = r[5]
 
    if data_quantity > get_stock: 
        messagebox.showerror('Not enough stock', 'We do not have enough stock for this item')       
    else:
        cart_list.insert(END, (data_quantity, data_type, data_size, data_color))
        price = int(get_price) * int(data_quantity)
        product_id.append(get_id)
        product_price.append(price)
        product_name.append(get_name)
        product_color.append(get_color)
        product_size.append(get_size)
        product_quantity.append(data_quantity)
        total = sum(product_price)
        total_price_text.config(state=NORMAL)
        total_price_text.delete("1.0","end")
        total_price_text.insert(END, total)
        total_price_text.config(state=DISABLED)
    
    


#Reset outputbox after add to cart
def reset_output():
    output_text.config(state=NORMAL)
    output_text.delete("1.0","end")
    output_text.insert(END, '')
    output_text.config(state=DISABLED)
    size.current(0)
    color.current(0)

#Selecting item
def selected_item(event):
    try:
        global selected_item
        global index 
        index = cart_list.curselection()[0]
        selected_item = cart_list.get(index)
        tshirt_entry.delete(0, END)
        tshirt_entry.insert(END, selected_item[1])
        pants_entry.delete(0, END)
        pants_entry.insert(END, selected_item[2])
        dress_entry.delete(0, END)
        dress_entry.insert(END, selected_item[3])
        skirt_entry.delete(0, END)
        skirt_entry.insert(END, selected_item[4])
        sweater_entry.delete(0, END)
        sweater_entry.insert(END, selected_item[5])
        jacket_entry.delete(0, END)
        jacket_entry.insert(END, selected_item[6])
    except IndexError:
        pass

#Remove clothes from cart
def remove_cart():
    global selected_item
    selected_item = cart_list.curselection()
    if len(selected_item) == 0:
        messagebox.showerror('No item selected', 'Please select an item to remove')
    elif len(selected_item) > 1:
        messagebox.showerror('Too many items selected', 'Please select only one item to remove')
    else:
        for selected_checkbox in selected_item[::-1]:
            cart_list.delete(selected_checkbox)
        for i in range (0, len(selected_item)):
            product_id.pop(selected_item[i])
            product_price.pop(selected_item[i])
            product_name.pop(selected_item[i])
            product_color.pop(selected_item[i])
            product_size.pop(selected_item[i]) 
            product_quantity.pop(selected_item[i])
    total = sum(product_price)
    total_price_text.config(state=NORMAL)
    total_price_text.delete("1.0","end")
    total_price_text.insert(END, total)
    total_price_text.config(state=DISABLED)
    


#Clear cart
def clear_text():
    tshirt_entry.delete(0, END)
    pants_entry.delete(0, END)
    dress_entry.delete(0, END)
    skirt_entry.delete(0, END)
    sweater_entry.delete(0, END)
    jacket_entry.delete(0, END)


#Cash out               
def cashout():
    #Generate bill
    directory = "C:/Users/Wallow/Desktop/CSIMS/Bill/" + str(day) + "/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    company = "\t\t\tClothes Store Company\n"
    address = "\t\t\tAddress: Ba Dinh, Ha Noi\n"
    phone = "\t\t\tPhone: 0123456789\n"
    sample = "\t\t\t\tInvoice\n"
    date = "\t\t\t" + str(day)
    header = "\n\n\t--------------------------------------------------------\n\tNo.\tProducts\tColor\tSize\tQty\tPrice\n\t--------------------------------------------------------"
    
    final = company + address + phone + sample + date + header
    file_name = str(directory) + str(random.randint(1000,1999)) + ".txt"
    f = open(file_name, "w")
    f.write(final)
    i = 1
    k = 0
    for t in product_name:
        f.write("\n\t" + str(i) + "\t" + str(product_name[k]) + "\t\t" + str(product_color[k]) + "\t" + str(product_size[k]) + "\t" + str(product_quantity[k]) + "\t" + str(product_price[k]))
        i += 1
        k += 1
    total = sum(product_price)
    f.write("\n\n\t\t\tTotal: $" + str(total) + "\n\t\t\tThank you for shopping with us!")
    f.close
    f = open(file_name, "r")
    call(["notepad.exe", file_name])

    #Update stock
    x = 0
    initial = "SELECT * from clothes where id=?"
    result = cur.execute(initial, (product_id[x],))
    for i in product_name:
        for r in result:
            old_stock = r[4]
        new_stock = int(old_stock) - int(product_quantity[x])
        sql = "UPDATE clothes SET stock=? WHERE id=?"
        cur.execute(sql, (new_stock, product_id[x]))
        con.commit()
        x += 1




#Take clothes
def take_tshirt():
    output_text.config(state=NORMAL)
    output_text.delete("1.0","end")
    output_text.insert(END, 'Shirt')
    output_text.config(state=DISABLED)

def take_pants():
    output_text.config(state=NORMAL)
    output_text.delete("1.0","end")
    output_text.insert(END, 'Pants')
    output_text.config(state=DISABLED)

def take_dress():
    output_text.config(state=NORMAL)
    output_text.delete("1.0","end")
    output_text.insert(END, 'Dress')
    output_text.config(state=DISABLED)

def take_skirt():
    output_text.config(state=NORMAL)
    output_text.delete("1.0","end")
    output_text.insert(END, 'Skirt')
    output_text.config(state=DISABLED)

def take_sweater():
    output_text.config(state=NORMAL)
    output_text.delete("1.0","end")
    output_text.insert(END, 'Sweater')
    output_text.config(state=DISABLED)

def take_jacket():
    output_text.config(state=NORMAL)
    output_text.delete("1.0","end")
    output_text.insert(END, 'Jacket')
    output_text.config(state=DISABLED)

#Shirt image button
def choose_tshirt():
    tshirt_button = Button(window, image = tshirt_image)
    tshirt_button.place(x = 20, y = 100)



tshirt_image = tk.PhotoImage(file = 'Image\shirt.png')
tshirt_button = Button(window, image=tshirt_image, command = take_tshirt)
tshirt_button.place(x = 20, y = 100)
tshirt_entry = Entry(window, textvariable=output_text)

#Pants image button
def choose_pants():
    pants_button = Button(window, image = pants_image)
    pants_button.place(x = 120, y = 100)

pants_image = tk.PhotoImage(file = 'Image\pants.png')
pants_button = Button(window, image=pants_image, command = take_pants)
pants_button.place(x = 125, y = 100)
pants_entry = Entry(window, textvariable = output_text)

#Shoes image button
def choose_dress():
    dress_button = Button(window, image = dress_image)
    dress_button.place(x = 220, y = 100)

dress_image = tk.PhotoImage(file = 'Image\dress.png')
dress_button = Button(window, image=dress_image, command = take_dress)
dress_button.place(x = 220, y = 100)
dress_entry = Entry(window, textvariable = output_text)

#Skirt image button
def choose_skirt():
    skirt_button = Button(window, image = skirt_image)
    skirt_button.place(x = 220, y = 235)

skirt_image = tk.PhotoImage(file = 'Image\skirt.png')
skirt_button = Button(window, image=skirt_image, command = take_skirt)
skirt_button.place(x = 220, y = 235)
skirt_entry = Entry(window, textvariable = output_text)

#Sweater image button
def choose_sweater():
    sweater_button = Button(window, image = sweater_image)
    sweater_button.place(x = 125, y = 235)

sweater_image = tk.PhotoImage(file = 'Image\sweater.png')
sweater_button = Button(window, image=sweater_image, command = take_sweater)
sweater_button.place(x = 125, y = 235)
sweater_entry = Entry(window, textvariable = output_text)

#Jacket image button
def choose_jacket():
    jacket_button = Button(window, image = jacket_image)
    jacket_button.place(x = 20, y = 235)

jacket_image = tk.PhotoImage(file = 'Image\jacket.png')
jacket_button = Button(window, image=jacket_image, command = take_jacket)
jacket_button.place(x = 20, y = 235)
jacket_entry = Entry(window, textvariable = output_text)

#Interface
cs_name = Label(text = 'Welcome to Clothes Store', fg = '#f06eff', font = ("Aharoni", 20, "bold"), anchor = "center")
cs_name.place(x = 20, y = 10)

clothes_label = Label(text = 'Choose The Products', fg = '#f06eff',font =("Bahnschrift", 16, "normal"))
clothes_label.place(x = 20, y = 65)

#Quantity
quantity_sb = Spinbox(from_=1, to =20, width=5)
quantity_sb.place(x=50, y=455)
quantity_label = Label(window, text="Quantity:", fg = '#f06eff', font=("Bahnschrift", 10)).place(x =45, y=435)

#size
tk.Label(window, text="Size:", fg = '#f06eff', font=("Bahnschrift", 10)).place(x =125, y=435)
n = tk.StringVar()
m = tk.StringVar()
size = ttk.Combobox(window, width=5, textvariable=n)

# Adding combobox drop down list
size['values'] = ('S', 'M', 'L', 'XL')
size.place(x = 125, y = 455)
size.current(0)

#color
tk.Label(window, text="Color:", fg = '#f06eff', font=("Bahnschrift", 10)).place(x =200, y=435)
color = ttk.Combobox(window, width=5, textvariable=m)

# Adding combobox drop down list
color['values'] = ('Red', 'Green', 'Blue', 'White')
color.place(x = 200, y = 455)
color.current(0)


#Go back Button
logout_btn = tk.Button(window, text = "Back", fg = '#f06eff', font = ("Arial", 8), width = 5, height = 1, command = log_out)
logout_btn.place(x = 605, y = 475)

cashout_btn = tk.Button(window, text = "Cash out!", fg = '#f06eff', font = ("Forte", 13), width = 8, height = 2, command = cashout)
cashout_btn.place(x = 435, y = 390)
    #add to cart
atc_btn = tk.Button(window, text = "Add to cart", fg = '#f06eff', font = ("Bahnschrift", 14), width = 10, height = 1, command = lambda: (atc(),reset_output()))
atc_btn.place(x = 275, y = 399)
    #remove from cart
remcart_btn = tk.Button(window, text = "Remove\nfrom cart", fg = '#f06eff', font = ("Bahnschrift", 12), width = 11, height = 2, command = remove_cart)
remcart_btn.place(x = 275, y = 445)

#Output pressed button
output_label = Label(window, text = "Item chosen: ", fg = "#f06eff", font = ("Bahnschrift", 14), width = 10, height = 1).place(x=45, y = 375)
output_text = Text(window, height = 1, width = 25, border = 1)
output_text.place(x = 50, y = 400)
output_text.config(state=DISABLED)

#Total Price Text"box"
total_price_label = Label(window, text = "Total Price: ", fg = "#f06eff", font = ("Bahnschrift", 10), width = 10, height = 1).place(x = 530, y = 390)
total_price_text = Text(window, height = 1, width = 10, border = 1,)
total_price_text.place(x = 530, y = 415)
total_price_text.config(state=DISABLED)

#Cart list(Listbox)
cart_list = Listbox(window, height = 20, width = 30, border = 1, selectmode = MULTIPLE)
cart_list.place(x = 435, y = 50)

#Bind
cart_list.bind('<<ListboxSelect>>', selected_item)

window.mainloop()

