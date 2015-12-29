__author__ = 'cbartel'

# import relevant modules - random, tkinter
from random import randint
from tkinter import *
from tkinter import ttk

class Application(Frame):

    # initialize app
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    # create widgets in separate function
    def createWidgets(self):

        # create frames
        self.buttonFrameFrame = Frame(self)
        self.labelComboFrame = Frame(self.buttonFrameFrame)

        # create labels
        self.rollLabel = Label(self.labelComboFrame,
                               text="Roll ")
        self.dLabel = Label(self.labelComboFrame,
                            text=" d ")

        # create entry widget
        self.numDiceVar = IntVar()
        self.numDiceEntry = Entry(self.labelComboFrame,
                                  width=3,
                                  textvariable=self.numDiceVar)
        # TODO: hook up validate entry class to entry widget
        
        self.numDiceEntry.delete(0, END)
        self.numDiceEntry.insert(0, 1)

        # create combo box and link variable
        self.dieSizeVar = IntVar()
        self.dieSizeCombo = ttk.Combobox(self.labelComboFrame,
                                         state="readonly",
                                         justify="center",
                                         width=3,
                                         textvariable=self.dieSizeVar)
        self.dieSizeCombo["values"] = (4, 6, 8, 10, 12, 20, 100)
        self.dieSizeCombo.current(5)

        # create one button to roll the dice
        self.rollButton = Button(self.buttonFrameFrame,
                                 text="Roll!",
                                 command=self.diceRolls)

        # Create a quit button that closes the window
        self.QUIT = Button(self.buttonFrameFrame, text="Quit", command=root.destroy)

        # Create listbox for each roll
        self.resultsList = Listbox(self)

        # Create scrollbar widget for new text field
        self.scrollbar = Scrollbar(self)

        # attach listbox to scrollbar
        self.resultsList.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.resultsList.yview)

        # arrange each widget in the window
        self.rollLabel.pack(side="left")
        self.numDiceEntry.pack(side="left")
        self.dLabel.pack(side="left")
        self.dieSizeCombo.pack(side="left")
        self.labelComboFrame.pack(side="top")
        self.rollButton.pack(fill="both", padx=3, pady=3)
        self.QUIT.pack(fill="both", padx=3, pady=3)
        self.buttonFrameFrame.pack(side="left")
        self.resultsList.pack(side="left", padx=5, pady=5)
        self.scrollbar.pack(side="left", fill=Y)

    # create dice rolling function
    def rollDie(self, dieSize):
        # roll one die with randint
        return randint(1, dieSize)

    def diceRolls(self):
        # clear previous values from rollList
        self.resultsList.delete(0, END)
        # roll 'diceNum' dice of size 'dieSize'
        dieSize = int(self.dieSizeCombo.get())
        diceNum = int(self.numDiceEntry.get())
        for i in range(diceNum):
            self.resultsList.insert(END, self.rollDie(dieSize))

# validate entry widget
class ValidatingEntry(Entry):

    def __init__(self, master, value="", **kw):
        Entry.__init__(self, master, **kw)
        self.__value = value
        self.__variable = StringVar()
        self.__variable.set(value)
        self.__variable.trace("w", self.__callback)
        self.config(textvariable=self.__variable)
        self.results = StringVar()
        if self.__value is None:
            self.results.set(None)
        else:
            self.results.set(self.__value)

    def __callback(self, *dummy):
        value = self.__variable.get()
        newvalue = self.validate(value)
        if newvalue is None:
            self.__variable.set(self.__value)
        elif newvalue != value:
            self.__value = newvalue
            self.__variable.set(newvalue)
        else:
            self.__value = value

    def validate(self, value):
        # override: return value, new value, or None if invalid
        self.results.set(value)
        return value

    def getresults(self, value):
        # override: return value, or chopped value in the case of ChopLengthEntry
        return self.results.get()

class IntegerEntry(ValidatingEntry):
    def validate(self, value):
        try:
            if value:
                v = int(value)
                self.results.set(value)
            return value
        except ValueError:
            return None

# create instance, launch window
if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    root.mainloop()
