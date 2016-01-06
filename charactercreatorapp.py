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
        self.abilitiesLabel = Label(self.statsFrame,
                                text="Abilities")
        self.raceBonusLabel = Label(self.statsFrame,
                                    text="Racial\nBonus")
        self.strLabel = Label(self.statsFrame,
                              text="Str")
        self.dexLabel = Label(self.statsFrame,
                              text="Dex")
        self.conLabel = Label(self.statsFrame,
                              text="Con")
        self.intLabel = Label(self.statsFrame,
                              text="Int")
        self.wisLabel = Label(self.statsFrame,
                              text="Wis")
        self.chaLabel = Label(self.statsFrame,
                              text="Cha")
        self.strBonusLabelVar = StringVar()
        self.strBonusLabel = Label(self.statsFrame,
                                   textvariable=self.strBonusLabelVar)
        self.dexBonusLabelVar = StringVar()
        self.dexBonusLabel = Label(self.statsFrame,
                                   textvariable=self.dexBonusLabelVar)
        self.conBonusLabelVar = StringVar()
        self.conBonusLabel = Label(self.statsFrame,
                                   textvariable=self.conBonusLabelVar)
        self.intBonusLabelVar = StringVar()
        self.intBonusLabel = Label(self.statsFrame,
                                   textvariable=self.intBonusLabelVar)
        self.wisBonusLabelVar = StringVar()
        self.wisBonusLabel = Label(self.statsFrame,
                                   textvariable=self.wisBonusLabelVar)
        self.chaBonusLabelVar = StringVar()
        self.chaBonusLabel = Label(self.statsFrame,
                                   textvariable=self.chaBonusLabelVar)

        # TODO: create 6 entry fields
        self.strEntryVar = IntVar()
        self.strEntry = Entry(self.statsFrame,
                              width=2,
                              textvariable=self.strEntryVar)
        self.dexEntryVar = IntVar()
        self.dexEntry = Entry(self.statsFrame,
                              width=2,
                              textvariable=self.dexEntryVar)
        self.conEntryVar = IntVar()
        self.conEntry = Entry(self.statsFrame,
                              width=2,
                              textvariable=self.conEntryVar)
        self.intEntryVar = IntVar()
        self.intEntry = Entry(self.statsFrame,
                              width=2,
                              textvariable=self.intEntryVar)
        self.wisEntryVar = IntVar()
        self.wisEntry = Entry(self.statsFrame,
                              width=2,
                              textvariable=self.wisEntryVar)
        self.chaEntryVar = IntVar()
        self.chaEntry = Entry(self.statsFrame,
                              width=2,
                              textvariable=self.chaEntryVar)

        # TODO: create 2 drop-downs
        self.raceDropMenuVar = StringVar()
        self.raceDropMenu = ttk.Combobox(self.raceClassFrame,
                                         state="readonly",
                                         textvariable=self.raceDropMenuVar)
        self.raceDropMenu["values"] = ('Human', 'Dwarf', 'Elf', 'Gnome',
                                       'Half-Elf', 'Half-Orc', 'Halfling')
        self.raceDropMenu.current(6)
        self.raceDropMenu.bind('<<ComboboxSelected>>',
                               self.raceSelect)
        self.classDropMenuVar = StringVar()
        self.classDropMenu = ttk.Combobox(self.raceClassFrame,
                                          state="readonly",
                                          textvariable=self.classDropMenuVar)
        self.classDropMenu["values"] = ('Barbarian', 'Bard', 'Cleric', 'Druid',
                                        'Fighter', 'Monk', 'Paladin', 'Ranger',
                                        'Rogue', 'Sorcerer', 'Wizard')
        self.classDropMenu.current(8)
        self.classDropMenu.bind('<<ComboboxSelected>>',
                                self.sayHi2)

        # TODO: create 3 buttons
        self.createButton = Button(self.buttonFrame,
                                   text="Create")
        self.saveButton = Button(self.buttonFrame,
                                 text="Save")
        self.quitButton = Button(self.buttonFrame,
                                 text="Quit",
                                 command=root.destroy)

        # TODO: create 3 radio buttons
        self.rollMasterVar = IntVar()
        self.roll1Radio = Radiobutton(self.radioDiceFrame,
                                      variable=self.rollMasterVar,
                                      value=1)
        self.roll2Radio = Radiobutton(self.radioDiceFrame,
                                      variable=self.rollMasterVar,
                                      value=2)
        self.roll3Radio = Radiobutton(self.radioDiceFrame,
                                      variable=self.rollMasterVar,
                                      value=3)

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

        self.statsFrame.grid(row=0, column=1, rowspan=3)
        self.abilitiesLabel.grid(row=0, column=0, columnspan=2)
        self.raceBonusLabel.grid(row=0, column=2)
        self.strLabel.grid(row=1, column=0)
        self.strEntry.grid(row=1, column=1)
        self.dexLabel.grid(row=2, column=0)
        self.dexEntry.grid(row=2, column=1)
        self.conLabel.grid(row=3, column=0)
        self.conEntry.grid(row=3, column=1)
        self.intLabel.grid(row=4, column=0)
        self.intEntry.grid(row=4, column=1)
        self.wisLabel.grid(row=5, column=0)
        self.wisEntry.grid(row=5, column=1)
        self.chaLabel.grid(row=6, column=0)
        self.chaEntry.grid(row=6, column=1)
        self.strBonusLabel.grid(row=1, column=2)
        self.dexBonusLabel.grid(row=2, column=2)
        self.conBonusLabel.grid(row=3, column=2)
        self.intBonusLabel.grid(row=4, column=2)
        self.wisBonusLabel.grid(row=5, column=2)
        self.chaBonusLabel.grid(row=6, column=2)

    # TODO: function to determine racial bonus
    def raceSelect(self, event):
        try:
            if event:
                if self.raceDropMenuVar.get() == 'Human':
                    print('Human')
                elif self.raceDropMenuVar.get() == 'Dwarf':
                    print('Dwarf')
                elif self.raceDropMenuVar.get() == 'Elf':
                    print('Elf')
                elif self.raceDropMenuVar.get() == 'Gnome':
                    print('Gnome')
                elif self.raceDropMenuVar.get() == 'Half-Elf':
                    print('Half-Elf')
                elif self.raceDropMenuVar.get() == 'Half-Orc':
                    print('Half-Orc')
                else:
                    print('Halfling')
        except:
            print('Error reading virtual event!')

    def sayHi2(self, event):
        try:
            if event:
                if self.classDropMenuVar.get() == 'Barbarian':
                    print('Barbarian')
                elif self.classDropMenuVar.get() == 'Bard':
                    print('Bard')
                elif self.classDropMenuVar.get() == 'Cleric':
                    print('Cleric')
                elif self.classDropMenuVar.get() == 'Druid':
                    print('Druid')
                elif self.classDropMenuVar.get() == 'Fighter':
                    print('Fighter')
                elif self.classDropMenuVar.get() == 'Monk':
                    print('Monk')
                elif self.classDropMenuVar.get() == 'Paladin':
                    print('Paladin')
                elif self.classDropMenuVar.get() == 'Ranger':
                    print('Ranger')
                elif self.classDropMenuVar.get() == 'Rogue':
                    print('Rogue')
                elif self.classDropMenuVar.get() == 'Sorcerer':
                    print('Sorcerer')
                else:
                    print('Wizard')
        except:
            print('Error reading virtual event!')

    # TODO: function to export character to .txt file

    # TODO: function to roll stats

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("Create A Character!")
    root.mainloop()
