__author__ = 'cbartel'

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

        # TODO: create 4 frames
        self.raceClassFrame = Frame(self)
        self.radioDiceFrame = Frame(self)
        self.buttonFrame = Frame(self)
        self.statsFrame = Frame(self)

        # TODO: create 19 labels
        self.raceLabel = Label(self.raceClassFrame,
                               text="Race")
        self.classLabel = Label(self.raceClassFrame,
                                text="Class")
        self.roll1Label = Label(self.radioDiceFrame,
                                text="3 of 4d6 x 6, reroll lowest")
        self.roll2Label = Label(self.radioDiceFrame,
                                text="3 of 4d6 x 6")
        self.roll3Label = Label(self.radioDiceFrame,
                                text="3d6 x 6")
        self.statsLabel = Label(self.statsFrame)
        self.raceBonusLabel = Label(self.statsFrame)
        self.strLabel = Label(self.statsFrame)
        self.dexLabel = Label(self.statsFrame)
        self.conLabel = Label(self.statsFrame)
        self.intLabel = Label(self.statsFrame)
        self.wisLabel = Label(self.statsFrame)
        self.chaLabel = Label(self.statsFrame)
        self.strBonusLabel = Label(self.statsFrame)
        self.dexBonusLabel = Label(self.statsFrame)
        self.conBonusLabel = Label(self.statsFrame)
        self.intBonusLabel = Label(self.statsFrame)
        self.wisBonusLabel = Label(self.statsFrame)
        self.chaBonusLabel = Label(self.statsFrame)

        # TODO: create 6 text fields
        self.strText = Text(self.statsFrame)
        self.dexText = Text(self.statsFrame)
        self.conText = Text(self.statsFrame)
        self.intText = Text(self.statsFrame)
        self.wisText = Text(self.statsFrame)
        self.chaText = Text(self.statsFrame)

        # TODO: create 2 drop-downs
        self.raceDropMenu = ttk.Combobox(self.raceClassFrame)
        self.classDropMenu = ttk.Combobox(self.raceClassFrame)

        # TODO: create 3 buttons
        self.createButton = Button(self.buttonFrame,
                                   text="Create")
        self.saveButton = Button(self.buttonFrame,
                                 text="Save")
        self.quitButton = Button(self.buttonFrame,
                                 text="Quit")

        # TODO: create 3 radio buttons
        self.roll1Radio = Radiobutton(self.radioDiceFrame)
        self.roll2Radio = Radiobutton(self.radioDiceFrame)
        self.roll3Radio = Radiobutton(self.radioDiceFrame)

        # TODO: arrange the frames within the window
        self.raceClassFrame.grid(row=0, column=0)
        self.raceLabel.grid(row=0, column=0)
        self.classLabel.grid(row=1, column=0)
        self.raceDropMenu.grid(row=0, column=1)
        self.classDropMenu.grid(row=1, column=1)

        self.radioDiceFrame.grid(row=1, column=0)
        self.roll1Radio.grid(row=0, column=0)
        self.roll1Label.grid(row=0, column=1)
        self.roll2Radio.grid(row=1, column=0)
        self.roll2Label.grid(row=1, column=1)
        self.roll3Radio.grid(row=2, column=0)
        self.roll3Label.grid(row=2, column=1)

        self.buttonFrame.grid(row=2, column=0)
        self.createButton.grid(row=0, column=0, sticky=W+E)
        self.saveButton.grid(row=1, column=0, sticky=W+E)
        self.quitButton.grid(row=2, column=0, sticky=W+E)

        self.statsFrame.grid(row=0, column=1)

    # TODO: function to determine racial bonus

    # TODO: function to export character to .txt file

    # TODO: function to roll stats

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("Create A Character!")
    root.mainloop()
