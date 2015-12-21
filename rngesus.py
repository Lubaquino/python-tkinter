__author__ = 'cbartel'

# Here we import tkinter
from tkinter import *
from tkinter import ttk
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
        # Create frame widget to house buttons
        self.buttonFrame = ttk.Frame(self)
        # Declare our string variable to be connected to our label
        self.numText = StringVar()
        # Give our string var a default value when initialized
        self.numText.set("0")
        # Create button to generate random number
        self.numberGen = Button(self.buttonFrame)
        # Overlay some text over the number generator button
        self.numberGen["text"] = "Generate"
        # Define what numberGen will do when clicked
        self.numberGen["command"] = self.generateNum
        # Create label to display number
        self.numberLabel = Label(self)
        # Hook our label up to our string variable
        self.numberLabel["textvariable"] = self.numText
        # Create a quit button that closes the window, make the text red
        self.QUIT = Button(self.buttonFrame, text="Quit", command=root.destroy)

        self.numberLabel.grid(sticky=N+E+S+W)
        self.buttonFrame.grid(padx=5, pady=5)
        self.numberGen.grid(padx=3, sticky=W+E)
        self.QUIT.grid(padx=3, sticky=W+E)

    # Create the number generate function
    def generateNum(self):
        self.numText.set(str(randint(1, 10)))

# Create a tkinter class object
# This object is needed for a Frame to be created
root = Tk()
# Create the application, make it the parent object
app = Application(master=root)
# Start the program
app.mainloop()
