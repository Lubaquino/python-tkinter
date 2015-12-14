__author__ = 'cbartel'

# Here we import tkinter
import tkinter as ttk
from random import randint

# Build the window using tkinter
class Application(ttk.Frame):

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
        # Declare our string variable to be connected to our label
        self.numText = ttk.StringVar()
        # Give our string var a default value when initialized
        self.numText.set("0")
        # Create button to generate random number
        self.numberGen = ttk.Button(self)
        # Overlay some text over the number generator button
        self.numberGen["text"] = "Generate"
        # Define what numberGen will do when clicked
        self.numberGen["command"] = self.generateNum
        # Create label to display number
        self.numberLabel = ttk.Label(self)
        # Hook our label up to our string variable
        self.numberLabel["textvariable"] = self.numText
        # Create a quit button that closes the window, make the text red
        self.QUIT = ttk.Button(self, text="Quit", command=root.destroy)

        # TODO: use .grid geometry to pack widgets

        self.numberLabel.pack(side="top")
        self.numberGen.pack()
        self.QUIT.pack(side="bottom")

    # Create the number generate function
    def generateNum(self):
        self.numText.set(str(randint(1, 10)))

root = ttk.Tk()

root.geometry("300x200")

app = Application(master=root)

app.mainloop()
