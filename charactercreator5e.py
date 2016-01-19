from random import randint, choice
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Application(Frame):

# initialize app
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.classSelect('<<ComboboxSelected>>')
        self.raceSelect('<<ComboboxSelected>>')

# create widgets in separate function
    def createWidgets(self):

# create 4 frames
        self.raceClassFrame = Frame(self)
        self.radioDiceFrame = Frame(self)
        self.statsFrame = Frame(self)
        self.textFrame = Frame(self)

# create menubutton for File, Help, About
        self.menubar = Menu(root)

        self.filemenu = Menu(self.menubar,
                             tearoff=0)
        self.filemenu.add_command(label="Create",
                                 command=self.rollAbilities)
        self.filemenu.add_command(label="Save",
                                 command=self.saveCharacter)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quit",
                                 command=root.quit)
        self.menubar.add_cascade(label="File",
                                 menu=self.filemenu)
        self.menubar.add_command(label="About",
                                 command=self.about)
        self.menubar.add_command(label="Help",
                                 command=self.help)
        root.config(menu=self.menubar)

# create 16 labels
        self.raceLabel = Label(self.raceClassFrame,
                               text="Race")
        self.classLabel = Label(self.raceClassFrame,
                                text="Class")
        self.abilitiesLabel = Label(self.statsFrame,
                                text="Abilities")
        self.raceBonusLabel = Label(self.statsFrame,
                                    text="Racial\nBonus")
        self.strLabel = Label(self.statsFrame,
                              text="Str",
                              fg="white",
                              bg="black",
                              relief="ridge")
        self.dexLabel = Label(self.statsFrame,
                              text="Dex",
                              fg="white",
                              bg="black",
                              relief="ridge")
        self.conLabel = Label(self.statsFrame,
                              text="Con",
                              fg="white",
                              bg="black",
                              relief="ridge")
        self.intLabel = Label(self.statsFrame,
                              text="Int",
                              fg="white",
                              bg="black",
                              relief="ridge")
        self.wisLabel = Label(self.statsFrame,
                              text="Wis",
                              fg="white",
                              bg="black",
                              relief="ridge")
        self.chaLabel = Label(self.statsFrame,
                              text="Cha",
                              fg="white",
                              bg="black",
                              relief="ridge")
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

# create 6 entry fields
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

# store each entry variable in array for calculation purposes
        self.abilityList = [self.strEntryVar, self.dexEntryVar, self.conEntryVar,
                            self.intEntryVar, self.wisEntryVar, self.chaEntryVar]

# create 2 drop-downs
        self.raceDropMenuVar = StringVar()
        self.raceDropMenu = ttk.Combobox(self.raceClassFrame,
                                         state="readonly",
                                         textvariable=self.raceDropMenuVar)
        self.raceDropMenu["values"] = ('Aasimar', 'Dragonborn', 'Hill Dwarf',
                                       'Mountain Dwarf', 'High Elf', 'Wood Elf',
                                       'Forest Gnome', 'Rock Gnome', 'Half-Elf',
                                       'Half-Orc', 'Lightfoot Halfling', 'Stout Halfling',
                                       'Human', 'Tiefling')
        self.raceDropMenu.current(10)
        self.raceDropMenu.bind('<<ComboboxSelected>>',
                               self.raceSelect)
        self.classDropMenuVar = StringVar()
        self.classDropMenu = ttk.Combobox(self.raceClassFrame,
                                          state="readonly",
                                          textvariable=self.classDropMenuVar)
        self.classDropMenu["values"] = ('Barbarian', 'Bard', 'Cleric', 'Druid',
                                        'Fighter', 'Monk', 'Paladin', 'Ranger',
                                        'Rogue', 'Sorcerer', 'Warlock', 'Wizard')
        self.classDropMenu.current(1)
        self.classDropMenu.bind('<<ComboboxSelected>>',
                                self.classSelect)

# create 3 radio buttons
        self.rollMasterVar = IntVar()
        self.roll1Radio = Radiobutton(self.radioDiceFrame,
                                      variable=self.rollMasterVar,
                                      anchor=W,
                                      value=1,
                                      text='3 of 4d6 x 6, reroll lowest',
                                      justify=LEFT)
        self.roll2Radio = Radiobutton(self.radioDiceFrame,
                                      variable=self.rollMasterVar,
                                      anchor=W,
                                      value=2,
                                      text='3 of 4d6 x 6',
                                      justify=LEFT)
        self.roll3Radio = Radiobutton(self.radioDiceFrame,
                                      variable=self.rollMasterVar,
                                      anchor=W,
                                      value=3,
                                      text='3d6 x 6',
                                      justify=LEFT)
        self.roll1Radio.select()

# TODO: create text field to display class/race information

# arrange the frames within the window
        self.raceClassFrame.grid(row=0, column=0)
        self.raceLabel.grid(row=0, column=0)
        self.classLabel.grid(row=1, column=0)
        self.raceDropMenu.grid(row=0, column=1)
        self.classDropMenu.grid(row=1, column=1)

        self.radioDiceFrame.grid(row=1, column=0)
        self.roll1Radio.grid(row=0, column=0, sticky=W+E)
        self.roll2Radio.grid(row=1, column=0, sticky=W+E)
        self.roll3Radio.grid(row=2, column=0, sticky=W+E)

        self.statsFrame.grid(row=0, column=1, rowspan=3)
        self.abilitiesLabel.grid(row=0, column=0, columnspan=2)
        self.raceBonusLabel.grid(row=0, column=2)
        self.strLabel.grid(row=1, column=0, sticky=W+E)
        self.strEntry.grid(row=1, column=1)
        self.dexLabel.grid(row=2, column=0, sticky=W+E)
        self.dexEntry.grid(row=2, column=1)
        self.conLabel.grid(row=3, column=0, sticky=W+E)
        self.conEntry.grid(row=3, column=1)
        self.intLabel.grid(row=4, column=0, sticky=W+E)
        self.intEntry.grid(row=4, column=1)
        self.wisLabel.grid(row=5, column=0, sticky=W+E)
        self.wisEntry.grid(row=5, column=1)
        self.chaLabel.grid(row=6, column=0, sticky=W+E)
        self.chaEntry.grid(row=6, column=1)
        self.strBonusLabel.grid(row=1, column=2)
        self.dexBonusLabel.grid(row=2, column=2)
        self.conBonusLabel.grid(row=3, column=2)
        self.intBonusLabel.grid(row=4, column=2)
        self.wisBonusLabel.grid(row=5, column=2)
        self.chaBonusLabel.grid(row=6, column=2)

        self.infoText.grid(row=2, column=0)
        self.infoText.grid(row=0, column=0)

# function to determine racial bonus
    def raceSelect(self, event):
        try:
            if event:
                if self.raceDropMenuVar.get() == 'Aasimar':
                    self.strBonusLabelVar.set('')
                    self.dexBonusLabelVar.set('')
                    self.conBonusLabelVar.set('')
                    self.intBonusLabelVar.set('')
                    self.wisBonusLabelVar.set('')
                    self.chaBonusLabelVar.set('')
                elif self.raceDropMenuVar.get() == 'Dragonborn':
                    self.strBonusLabelVar.set('')
                    self.dexBonusLabelVar.set('')
                    self.conBonusLabelVar.set('')
                    self.intBonusLabelVar.set('')
                    self.wisBonusLabelVar.set('')
                    self.chaBonusLabelVar.set('')
                elif self.raceDropMenuVar.get() == 'Hill Dwarf':
                    self.strBonusLabelVar.set('')
                    self.dexBonusLabelVar.set('')
                    self.conBonusLabelVar.set('')
                    self.intBonusLabelVar.set('')
                    self.wisBonusLabelVar.set('')
                    self.chaBonusLabelVar.set('')
                elif self.raceDropMenuVar.get() == 'Mountain Dwarf':
                    self.strBonusLabelVar.set('')
                    self.dexBonusLabelVar.set('')
                    self.conBonusLabelVar.set('')
                    self.intBonusLabelVar.set('')
                    self.wisBonusLabelVar.set('')
                    self.chaBonusLabelVar.set('')
                elif self.raceDropMenuVar.get() == 'High Elf':
                    self.strBonusLabelVar.set('')
                    self.dexBonusLabelVar.set('')
                    self.conBonusLabelVar.set('')
                    self.intBonusLabelVar.set('')
                    self.wisBonusLabelVar.set('')
                    self.chaBonusLabelVar.set('')
                elif self.raceDropMenuVar.get() == 'Wood Elf':
                    self.strBonusLabelVar.set('')
                    self.dexBonusLabelVar.set('')
                    self.conBonusLabelVar.set('')
                    self.intBonusLabelVar.set('')
                    self.wisBonusLabelVar.set('')
                    self.chaBonusLabelVar.set('')
                elif self.raceDropMenuVar.get() == 'Forest Gnome':
                    self.strBonusLabelVar.set('')
                    self.dexBonusLabelVar.set('')
                    self.conBonusLabelVar.set('')
                    self.intBonusLabelVar.set('')
                    self.wisBonusLabelVar.set('')
                    self.chaBonusLabelVar.set('')
                elif self.raceDropMenuVar.get() == 'Rock Gnome':
                    self.strBonusLabelVar.set('')
                    self.dexBonusLabelVar.set('')
                    self.conBonusLabelVar.set('')
                    self.intBonusLabelVar.set('')
                    self.wisBonusLabelVar.set('')
                    self.chaBonusLabelVar.set('')
                elif self.raceDropMenuVar.get() == 'Half-Elf':
                    self.strBonusLabelVar.set('')
                    self.dexBonusLabelVar.set('')
                    self.conBonusLabelVar.set('')
                    self.intBonusLabelVar.set('')
                    self.wisBonusLabelVar.set('')
                    self.chaBonusLabelVar.set('')
                elif self.raceDropMenuVar.get() == 'Half-Orc':
                    self.strBonusLabelVar.set('')
                    self.dexBonusLabelVar.set('')
                    self.conBonusLabelVar.set('')
                    self.intBonusLabelVar.set('')
                    self.wisBonusLabelVar.set('')
                    self.chaBonusLabelVar.set('')
                elif self.raceDropMenuVar.get() == 'Lightfoot Halfling':
                    self.strBonusLabelVar.set('')
                    self.dexBonusLabelVar.set('')
                    self.conBonusLabelVar.set('')
                    self.intBonusLabelVar.set('')
                    self.wisBonusLabelVar.set('')
                    self.chaBonusLabelVar.set('')
                elif self.raceDropMenuVar.get() == 'Stout Halfling':
                    self.strBonusLabelVar.set('')
                    self.dexBonusLabelVar.set('')
                    self.conBonusLabelVar.set('')
                    self.intBonusLabelVar.set('')
                    self.wisBonusLabelVar.set('')
                    self.chaBonusLabelVar.set('')
                elif self.raceDropMenuVar.get() == 'Human':
                    self.strBonusLabelVar.set('')
                    self.dexBonusLabelVar.set('')
                    self.conBonusLabelVar.set('')
                    self.intBonusLabelVar.set('')
                    self.wisBonusLabelVar.set('')
                    self.chaBonusLabelVar.set('')
                else:
                    self.strBonusLabelVar.set('')
                    self.dexBonusLabelVar.set('')
                    self.conBonusLabelVar.set('')
                    self.intBonusLabelVar.set('')
                    self.wisBonusLabelVar.set('')
                    self.chaBonusLabelVar.set('')
        except:
            print('Error reading virtual event!')

# function to determine class primary ability/abilities
    def classSelect(self, event):
        try:
            if event:
                if self.classDropMenuVar.get() == 'Barbarian':
                    self.strLabel["fg"] = "green"
                    self.conLabel["fg"] = "white"
                    self.dexLabel["fg"] = "white"
                    self.wisLabel["fg"] = "white"
                    self.chaLabel["fg"] = "white"
                    self.intLabel["fg"] = "white"
                elif self.classDropMenuVar.get() == 'Bard':
                    self.chaLabel["fg"] = "green"
                    self.dexLabel["fg"] = "white"
                    self.intLabel["fg"] = "white"
                    self.wisLabel["fg"] = "white"
                    self.conLabel["fg"] = "white"
                    self.strLabel["fg"] = "white"
                elif self.classDropMenuVar.get() == 'Cleric':
                    self.wisLabel["fg"] = "green"
                    self.conLabel["fg"] = "white"
                    self.chaLabel["fg"] = "white"
                    self.intLabel["fg"] = "white"
                    self.dexLabel["fg"] = "white"
                    self.strLabel["fg"] = "white"
                elif self.classDropMenuVar.get() == 'Druid':
                    self.wisLabel["fg"] = "green"
                    self.dexLabel["fg"] = "white"
                    self.strLabel["fg"] = "white"
                    self.chaLabel["fg"] = "white"
                    self.intLabel["fg"] = "white"
                    self.conLabel["fg"] = "white"
                elif self.classDropMenuVar.get() == 'Fighter':
                    self.strLabel["fg"] = "green"
                    self.dexLabel["fg"] = "green"
                    self.conLabel["fg"] = "white"
                    self.wisLabel["fg"] = "white"
                    self.chaLabel["fg"] = "white"
                    self.intLabel["fg"] = "white"
                elif self.classDropMenuVar.get() == 'Monk':
                    self.dexLabel["fg"] = "green"
                    self.wisLabel["fg"] = "white"
                    self.strLabel["fg"] = "white"
                    self.chaLabel["fg"] = "white"
                    self.intLabel["fg"] = "white"
                    self.conLabel["fg"] = "white"
                elif self.classDropMenuVar.get() == 'Paladin':
                    self.chaLabel["fg"] = "green"
                    self.strLabel["fg"] = "green"
                    self.wisLabel["fg"] = "white"
                    self.intLabel["fg"] = "white"
                    self.dexLabel["fg"] = "white"
                    self.conLabel["fg"] = "white"
                elif self.classDropMenuVar.get() == 'Ranger':
                    self.dexLabel["fg"] = "green"
                    self.strLabel["fg"] = "white"
                    self.wisLabel["fg"] = "white"
                    self.chaLabel["fg"] = "white"
                    self.intLabel["fg"] = "white"
                    self.conLabel["fg"] = "white"
                elif self.classDropMenuVar.get() == 'Rogue':
                    self.dexLabel["fg"] = "green"
                    self.intLabel["fg"] = "white"
                    self.wisLabel["fg"] = "white"
                    self.chaLabel["fg"] = "white"
                    self.conLabel["fg"] = "white"
                    self.strLabel["fg"] = "white"
                elif self.classDropMenuVar.get() == 'Sorcerer':
                    self.chaLabel["fg"] = "green"
                    self.dexLabel["fg"] = "white"
                    self.conLabel["fg"] = "white"
                    self.wisLabel["fg"] = "white"
                    self.intLabel["fg"] = "white"
                    self.strLabel["fg"] = "white"
                elif self.classDropMenuVar.get() == 'Warlock':
                    self.chaLabel["fg"] = "green"
                    self.dexLabel["fg"] = "white"
                    self.conLabel["fg"] = "white"
                    self.wisLabel["fg"] = "white"
                    self.intLabel["fg"] = "white"
                    self.strLabel["fg"] = "white"
                else:
                    self.intLabel["fg"] = "green"
                    self.dexLabel["fg"] = "white"
                    self.conLabel["fg"] = "white"
                    self.wisLabel["fg"] = "white"
                    self.chaLabel["fg"] = "white"
                    self.strLabel["fg"] = "white"
        except:
            print('Error reading virtual event!')

# function to roll stats
    def rollAbilities(self):
        v = self.rollMasterVar.get()
        try:
            if v < 3:
                for a in self.abilityList:
                    diceList = []
                    for i in range(4):
                        diceList.append(randint(1, 6))
                    diceList.remove(min(diceList))
                    a.set(sum(diceList))
            else:
                for a in self.abilityList:
                    diceList = []
                    for i in range(3):
                        diceList.append(randint(1, 6))
                    a.set(sum(diceList))
        except:
            print('Error finding RadioButton value!')


# function to export character to .txt file
    def saveCharacter(self):
        f = open(self.raceDropMenuVar.get() + ' ' +
                 self.classDropMenuVar.get() + ' ' +
                 self.fileKey() + '.txt', 'w')
        f.write(self.raceDropMenuVar.get() + '\n' +
                self.classDropMenuVar.get() + '\n' +
                'Str' + ' ' + str(self.strEntryVar.get()) + ' ' +
                str(self.strBonusLabelVar.get()) +
                '\n' +
                'Dex' + ' ' + str(self.dexEntryVar.get()) + ' ' +
                str(self.dexBonusLabelVar.get()) +
                '\n' +
                'Con' + ' ' + str(self.conEntryVar.get()) + ' ' +
                str(self.conBonusLabelVar.get()) +
                '\n' +
                'Int' + ' ' + str(self.intEntryVar.get()) + ' ' +
                str(self.intBonusLabelVar.get()) +
                '\n' +
                'Wis' + ' ' + str(self.wisEntryVar.get()) + ' ' +
                str(self.wisBonusLabelVar.get()) +
                '\n' +
                'Cha' + ' ' + str(self.chaEntryVar.get()) + ' ' +
                str(self.chaBonusLabelVar.get())
                )
        f.close()

# generate random 16 char file key
    def fileKey(self):
        keyString = ''
        return keyString.join(choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                              for i in range(8))

# create 2 messageboxes for about/help
    def about(self):
        messagebox.showinfo("About",
                            "Written by: Chad Bartel\n" +
                            "Using Python ver " + sys.version)

    def help(self):
        messagebox.showinfo("Help",
                            "Gonna add something here.")

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("Create A Character!")
    root.mainloop()
