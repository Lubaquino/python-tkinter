import tkinter as tk

root = tk.Tk()

def add_new():
    b = tk.Button(root,text="Click to destroy")
    b.pack()
    b.config(command=b.pack_forget)

b = tk.Button(root,text="Add_new",command=add_new)
b.pack()
root.mainloop()
