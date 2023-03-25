import tkinter as tk
from tkinter import messagebox
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hand Bow")
        self.root.geometry("600x400")
        
        label = tk.Label(self.root, text="Hand Bow", padx=10, pady=10)
        label.pack()

        self.textbox = tk.Text(self.root, height=5)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.BooleanVar()
        check = tk.Checkbutton(self.root, text="Quanasacmaidich", variable=self.check_state)
        check.pack(padx=10, pady=10)

        button = tk.Button(self.root, text="Click Me", command=self.show_message)
        button.pack(padx=10, pady=10)

        self.root.mainloop()
    
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get("1.0", tk.END))
        else:
            messagebox.showinfo("Message", self.textbox.get("1.0", tk.END))

GUI()

    