import tkinter as tk

root = tk.Tk()

def add_new():
    b = tk.Button(root, text="Click to destroy")
    b.pack()
    # pack_forget doesn't destroy the widget, it saves it for later use/repacking
    # b.config(command=b.pack_forget)
    # destroy will destroy the widget and remove it from memory, preventing memory leak
    b.config(command=b.destroy)

b = tk.Button(root, text="Add_new", command=add_new)
b.pack()
root.mainloop()
