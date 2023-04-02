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

f = open("cart_list.txt", "w")


window = Tk()
window.title("Clothes Store")
window.geometry("645x500")
window.configure(bg = '#3D3D3D')
window.resizable(False, False)

output_text = StringVar()

#populate list


#Log out
def log_out():
    window.destroy()
    call(["python","manager.py"])


#Add to cart
def atc():
    global data_color, data_quantity, data_size, data_type
    data_color = color.get()
    data_quantity = quantity_sb.get()
    data_size = size.get()
    data_type = output_text.get("1.0","end-1c").strip()
    if data_type == '':
        messagebox.showerror('Required Fields', 'Please choose an item')
        return
    cart_list.insert(END, (data_quantity, data_type, data_size, data_color))

    L = [data_quantity, " [",data_type, "]", "[",data_size, "]", "[",data_color, "]\n"]
    f.writelines(L)


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
    for selected_checkbox in selected_item[::-1]:
        cart_list.delete(selected_checkbox)


#Clear cart
def clear_text():
    tshirt_entry.delete(0, END)
    pants_entry.delete(0, END)
    dress_entry.delete(0, END)
    skirt_entry.delete(0, END)
    sweater_entry.delete(0, END)
    jacket_entry.delete(0, END)


#Cash out               ##k quit sau khi cash out, chỉ renew listbox
def cashout():
    os.startfile('cart_list.txt')
    f.close()
    quit()


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

tshirt_image = tk.PhotoImage(file = 'Images\shirt.png')
tshirt_button = Button(window, image=tshirt_image, command = take_tshirt)
tshirt_button.place(x = 20, y = 100)
tshirt_entry = Entry(window, textvariable=output_text)

#Pants image button
def choose_pants():
    pants_button = Button(window, image = pants_image)
    pants_button.place(x = 120, y = 100)

pants_image = tk.PhotoImage(file = 'Images\pants.png')
pants_button = Button(window, image=pants_image, command = take_pants)
pants_button.place(x = 125, y = 100)
pants_entry = Entry(window, textvariable = output_text)

#Shoes image button
def choose_dress():
    dress_button = Button(window, image = dress_image)
    dress_button.place(x = 220, y = 100)

dress_image = tk.PhotoImage(file = 'Images\dress.png')
dress_button = Button(window, image=dress_image, command = take_dress)
dress_button.place(x = 220, y = 100)
dress_entry = Entry(window, textvariable = output_text)

#Skirt image button
def choose_skirt():
    skirt_button = Button(window, image = skirt_image)
    skirt_button.place(x = 220, y = 235)

skirt_image = tk.PhotoImage(file = 'Images\skirt.png')
skirt_button = Button(window, image=skirt_image, command = take_skirt)
skirt_button.place(x = 220, y = 235)
skirt_entry = Entry(window, textvariable = output_text)

#Sweater image button
def choose_sweater():
    sweater_button = Button(window, image = sweater_image)
    sweater_button.place(x = 125, y = 235)

sweater_image = tk.PhotoImage(file = 'Images\sweater.png')
sweater_button = Button(window, image=sweater_image, command = take_sweater)
sweater_button.place(x = 125, y = 235)
sweater_entry = Entry(window, textvariable = output_text)

#Jacket image button
def choose_jacket():
    jacket_button = Button(window, image = jacket_image)
    jacket_button.place(x = 20, y = 235)

jacket_image = tk.PhotoImage(file = 'Images\jacket.png')
jacket_button = Button(window, image=jacket_image, command = take_jacket)
jacket_button.place(x = 20, y = 235)
jacket_entry = Entry(window, textvariable = output_text)

#Interface
cs_name = Label(text = 'Welcome to Clothes Store', bg = '#3D3D3D', fg = '#edb1fc', font = ("Lobster", 20, "bold"), anchor = "center")
cs_name.grid(column = 2, row = 0)

clothes_label = Label(text = 'Choose The Products', bg = '#3D3D3D', fg = '#ffffff',font =("Times New Roman", 16, "normal"))
clothes_label.grid(column = 1, row = 1)

#Quantity
quantity_sb = Spinbox(from_=1, to =10, width=5)
quantity_sb.place(x=50, y=455)
quantity_label = Label(window, text="Quantity:", bg = "#3D3D3D", fg = '#ffffff', font=("Times New Roman", 10)).place(x =45, y=435)

#size
tk.Label(window, text="Size:", bg = "#3D3D3D", fg = '#ffffff', font=("Times New Roman", 10)).place(x =125, y=435)
n = tk.StringVar()
m = tk.StringVar()
size = ttk.Combobox(window, width=5, textvariable=n)

# Adding combobox drop down list
size['values'] = (' XS', ' S', ' M', ' L', ' XL', ' XXL')
size.place(x = 125, y = 455)
size.current(0)

#color
tk.Label(window, text="Color:", bg = "#3D3D3D", fg = '#ffffff', font=("Times New Roman", 10)).place(x =200, y=435)
color = ttk.Combobox(window, width=5, textvariable=m)

# Adding combobox drop down list
color['values'] = (' Red', ' Green', ' Blue', ' Gray', ' Black', ' White')
color.place(x = 200, y = 455)
color.current(0)


#Button
logout_btn = tk.Button(window, text = "Log out", bg = '#3D3D3D', fg = '#ffffff', font = ("Arial", 8), width = 5, height = 1, command = log_out)
logout_btn.place(x = 605, y = 475)

cashout_btn = tk.Button(window, text = "Cash out!", bg = '#3D3D3D', fg = '#ffffff', font = ("Lobster", 14), width = 8, height = 1, command = cashout)
cashout_btn.place(x = 435, y = 395)
    #add to cart
atc_btn = tk.Button(window, text = "Add to cart", bg = '#3D3D3D', fg = '#ffffff', font = ("Times New Roman", 14), width = 10, height = 1, command = lambda: (atc(),reset_output()))
atc_btn.place(x = 275, y = 399)
    #remove from cart
remcart_btn = tk.Button(window, text = "Remove\nfrom cart", bg = '#3D3D3D', fg = '#ffffff', font = ("Times New Roman", 12), width = 11, height = 2, command = remove_cart)
remcart_btn.place(x = 275, y = 445)

#Output pressed button
output_label = Label(window, text = "Item chosen: ", bg = '#3D3D3D', fg = "#ffffff", font = ("Times New Roman", 14), width = 10, height = 1).place(x=45, y = 375)
output_text = Text(window, height = 1, width = 25, border = 1)
output_text.place(x = 50, y = 400)
output_text.config(state=DISABLED)

#Total Price Text"box"
total_price_label = Label(window, text = "Total Price: ", bg = '#3D3D3D', fg = "#ffffff", font = ("Times New Roman", 10), width = 10, height = 1).place(x = 530, y = 390)
total_price_text = Text(window, height = 1, width = 10, border = 1)
total_price_text.place(x = 530, y = 415)
total_price_text.config(state=DISABLED)

#Cart list(Listbox)
cart_list = Listbox(window, height = 20, width = 30, border = 1, selectmode = MULTIPLE)
cart_list.place(x = 435, y = 50)

#Bind
cart_list.bind('<<ListboxSelect>>', selected_item)

window.mainloop()

