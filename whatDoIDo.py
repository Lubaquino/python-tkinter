from random import choice
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class Application(Frame):

    # Initialize app
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    # TODO: Build method to house all app widgets
    def createWidgets(self):

        # Create frames for widgets
        self.whatDoFrame = Frame(self)
        self.textFrame = Frame(self)

        # TODO: Create 'File' and 'Quit' on menubar
        self.menubar = Menu(root)

        self.filemenu = Menu(self.menubar,
                             tearoff=0)
        self.filemenu.add_command(label="Save",
                                  command=self.saveFile)
        self.filemenu.add_command(label="Load",
                                  command=self.loadFile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit",
                                  command=root.quit)
        self.menubar.add_cascade(label="File",
                                 menu=self.filemenu)
        self.menubar.add_command(label="Help",
                                 command=self.help)
        root.config(menu=self.menubar)

        # TODO: Create label for "flavor" above dynamic label
        self.flavorLabel = Label(self.whatDoFrame,
                                 text="What about...")

        # TODO: Create dynamic label widget to display result
        self.resultText = StringVar()
        self.resultLabel = Label(self.whatDoFrame,
                                 relief="sunken",
                                 justify=CENTER,
                                 width=25,
                                 textvariable=self.resultText)

        # TODO: Create button to generate result
        self.resultButton = Button(self.whatDoFrame,
                                   text="I'm Bored!",
                                   command=self.chooseResult)

        # TODO: Create text widget for displaying/creating text files
        self.textBox = Text(self.textFrame,
                            wrap=WORD,
                            width=15,
                            height=10)

        # TODO: Create Y-scrollbar for text widget
        self.scrollY = Scrollbar(self.textFrame)
        self.textBox.config(yscrollcommand=self.scrollY.set)
        self.scrollY.config(command=self.textBox.yview)

        # TODO: Arrange widgets in frame
        self.whatDoFrame.grid(row=0, column=0)
        self.flavorLabel.grid(row=0, column=0, sticky=W+E)
        self.resultLabel.grid(row=1, column=0, sticky=W+E)
        self.resultButton.grid(row=2, column=0)

        self.textFrame.grid(row=0, column=1)
        self.textBox.grid(row=0, column=0)
        self.scrollY.grid(row=0, column=1, sticky=N+S)

    # TODO: Load text file for result choices and close text file
    def loadFile(self):
        self.loadPath = filedialog.askopenfilename()
        self.textBox.delete(1.0, END)
        self.loadTxt = open(self.loadPath, 'r')
        self.textBox.insert(1.0, str(self.loadTxt.read()).strip())
        self.loadTxt.close()
        return self.loadPath

    # TODO: Save text widget contents for results choices
    def saveFile(self):
        self.savePath = filedialog.asksaveasfilename()
        self.saveTxt = open(self.savePath + ".txt", 'w')
        self.saveTxt.write(str(self.textBox.get(1.0, END)).strip())
        self.saveTxt.close()
        return self.savePath

    # TODO: Build method to choose a result from the text file
    def chooseResult(self):
        # Check to see if a list has been loaded
        if str(self.textBox.get(1.0, END)) == "\n":
            messagebox.showinfo("Whoops!",
                                "Please load a text file from the file menu or "
                                "start making a list of stuff to do in the "
                                "blank space on the right!")
        else:
            self.buildList()
            self.resultText.set(choice(self.resultList))

    # TODO: Take each line in text widget and store it in a list
    def buildList(self):
        # Split the string in text box by a newline and save it
        self.resultList = str(self.textBox.get(1.0, END)).split('\n')
        # Remove any newlines/whitespace from list
        for r in self.resultList:
            if r == "" or r == "\n":
                self.resultList.remove(r)
        return self.resultList

    # TODO: Create pop-up for "Help" menubutton
    def help(self):
        messagebox.showinfo("Help",
                            "'Save' - Click this if you would like to save the "
                            "contents contained in the text widget on the right side "
                            "of the program as a text file.\n\n"
                            "'Load' - Click this if you would like to load a text "
                            "file with items separated by newlines.\n\n"
                            "'Quit' - Click this to quit the program!")

# Run app
if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("What Do I Do?!")
    root.mainloop()
