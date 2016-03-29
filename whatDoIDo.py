from random import randint, choice
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class Application(Frame):

    # Initialize app
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    # TODO: Build method to house all app widgets
    def createWidgets(self):

        # TODO: Create frame for widgets
        self.whatDoFrame = Frame(self)

        # TODO: Create label for "flavor" above dynmic label
        self.flavorLabel = Label(self.whatDoFrame,
                                 text="What about...")

        # TODO: Create dynamic label widget to display result
        self.resultText = StringVar()
        self.resultLabel = Label(self.whatDoFrame,
                                 relief="sunken",
                                 justify=CENTER,
                                 textvariable=self.resultText)

        # TODO: Create button to generate result


    # TODO: Create file bar to load a text file to use as results list and quit


    # TODO: Load text file for result choices and close text file


# Run app
if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("What Do I Do?!")
    root.mainloop()
