__author__ = 'cbartel'

# import relevant modules - random, tkinter
from random import randint
import tkinter as tk
from tkinter import ttk

# initialize app
class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

# create widgets in separate function
    def createWidgets(self):

        # create 3 labels
        self.rollLabel = tk.Label(self, text="Roll ")
        self.dLabel = tk.Label(self, text=" d ")
        self.resultsVar = tk.StringVar()
        self.resultsLabel = tk.Label(self, textvariable=self.resultsVar)

        # create 2 combo boxes
        self.numDiceVar = tk.StringVar()
        self.numDiceCombo = ttk.Combobox(self, state="readonly",
                                         justify="center",
                                         textvariable=self.numDiceVar)
        self.numDiceCombo["values"] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.numDiceCombo.current(0)
        self.dieSizeVar = tk.StringVar()
        self.dieSizeCombo = ttk.Combobox(self, state="readonly",
                                         justify="center",
                                         textvariable=self.dieSizeVar)
        self.dieSizeCombo["values"] = (4, 6, 8, 10, 12, 20, 100)
        self.dieSizeCombo.current(5)

        # create one button to roll the dice
        self.rollButton = tk.Button(self, text="Roll!",
                                    command=self.diceRolls(self.dieSizeVar, self.numDiceVar))

        # TODO: arrange each widget in the window
        self.rollLabel.grid(row=0, column=0)
        self.numDiceCombo.grid(row=0, column=1)
        self.dLabel.grid(row=0, column=2)
        self.dieSizeCombo.grid(row=0, column=3)
        self.rollButton.grid(row=2, column=2)
        self.resultsLabel.grid(row=0, column=4, rowspan=3)

# create dice rolling function
    def rollDie(self, dieSize):
        # roll one die with randint
        return randint(1, dieSize)

    def diceRolls(self, dieSize, diceNum):
        # roll 'diceNum' dice of size 'dieSize'
        rollDict = {}
        rollTotal = 0
        i = 0
        while i < int(diceNum):
            rollDict[i] = self.rollDie(int(dieSize))
            rollTotal += rollDict[i]
        self.resultsVar.set(self.dictToString(rollDict) + "\nTotal = " + rollTotal)

    def dictToString(self, dict):
        results = ""
        results.join('Roll {}: {}\n'.format(k, v) for k, v in sorted(dict.items()))
        return results

# create instance, launch window
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
