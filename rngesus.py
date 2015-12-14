__author__ = 'cbartel'

# Here we import tkinter
from tkinter import *
from tkinter import ttk
from random import randint

# Build the window using tkinter
class Application(ttk.Frame):


    # We need to declare our number variable
    numText = StringVar()
    numText.set('NULL')

    # When the program is executed:
    #   1. Create the window
    #   2. Run the .pack() function on self
    #   3. Run the .createWidgets() function on self
    # master=None means this is the parent object
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    # We want buttons and text box, so we need a .createWidgets function
    def createWidgets(self):
        # Create button to generate random number
        self.numberGen = ttk.Button(self)
        # Overlay some text over the number generator button
        self.numberGen["text"] = "Generate a number"
        # Define what numberGen will do when clicked
        self.numberGen["command"] = self.generateNum
        # Create label to display number
        self.numberLabel = ttk.Label(self, textvariable=self.numText)
        self.numberLabel.bind(self.numText)

        # TODO: use .grid geometry to pack widgets

        self.numberGen.pack()
        self.numberLabel.pack()

    # Create the number generate function
    def generateNum(self):
        self.numText = randint(1, 10).__str__()

    # Create text update event function
    def updateText(event):
        self.numberLabel.set(self.numText.get())
        root.update_idletasks()

root = Tk()

root.geometry("300x200")

app = Application(master=root)

app.mainloop()
