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

        # Create frame for widgets
        self.whatDoFrame = Frame(self)

        # TODO: Create 'File' and 'Quit' on menubar
        self.menubar = Menu(root)
        self.filemenu = Menu(self.menubar,
                             tearoff=0)
        self.filemenu.add_command(label="Open",
                                  command=self.openFile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit",
                                  command=root.quit)
        root.config(menu=self.menubar)

        # TODO: Create label for "flavor" above dynamic label
        self.flavorLabel = Label(self.whatDoFrame,
                                 text="What about...")

        # TODO: Create dynamic label widget to display result
        self.resultText = StringVar()
        self.resultLabel = Label(self.whatDoFrame,
                                 relief="sunken",
                                 justify=CENTER,
                                 textvariable=self.resultText)

        # TODO: Create button to generate result
        self.resultButton = Button(self.whatDoFrame,
                                   text="I'm Bored!",
                                   command=self.chooseResult)

        # TODO: Arrange widgets in frame
        self.whatDoFrame.grid(row=0, column=0)
        self.flavorLabel.grid(row=0, column=0, sticky=W+E)
        self.resultLabel.grid(row=1, column=0, sticky=W+E)
        self.resultButton.grid(row=2, column=0)

    # TODO: Load text file for result choices and close text file
    def openFile(self):
        pass

    # TODO: Build method to choose a result from the text file
    def chooseResult(self):
        pass

# Run app
if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("What Do I Do?!")
    root.mainloop()
