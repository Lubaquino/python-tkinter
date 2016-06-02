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

# ~~~~~~~~~~~~~~~~~~~~ ALTERNATE EXAMPLE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from tkinter import *

class Application(Frame):

    # initialize app
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # create the widgets
        self.masterFrame = Frame(self)
        self.masterFrame.pack()
        self.newReportFrame = Frame(self.masterFrame)
        self.newReportFrame.pack()

        # on button press, add a new report line
        self.addReportButton = Button(self.masterFrame,
                                      text="Add Report",
                                      command=self.addReportLine)
        self.addReportButton.pack()

    def addReportLine(self):
        # add new line to window to search and dl another file
        self.newReportFrame = Frame(self.masterFrame)
        self.newReportFrame.pack()
        self.label1 = Label(self.newReportFrame,
                            text="Report file name: ")
        self.label1.grid(row=0, column=0)
        self.entry1 = Entry(self.newReportFrame,
                            text="Type filename and extension here")
        self.entry1.grid(row=0, column=1)
        self.dButton = Button(self.newReportFrame,
                              text="Click to delete a line")
        self.dButton.config(command=self.newReportFrame.destroy)
        self.dButton.grid(row=0, column=2)

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("Download attachments from Email")
    root.mainloop()
