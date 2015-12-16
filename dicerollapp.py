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
        # create one button to roll the dice
        self.rollDice = tk.Button(self)
        self.rollDice["text"] = "Roll!"

        # create frame to house text output
        self.outputFrame = tk.Frame(self)

        # create 4 labels
        self.rollLabel = tk.Label(self, text="Roll ")
        self.dLabel = tk.Label(self, text=" d ")
        self.timesLabel = tk.Label(self, text=" times.")
        self.resultsVar = tk.StringVar()
        self.resultsLable = tk.Label(self, textvariable=self.resultsVar)

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

        # TODO: arrange each widget in the window

# create dice rolling function
    def rollDie(self, dieSize):
        # roll one die with randint
        return randint(1, dieSize)

    def diceRolls(self, dieSize, diceNum):
        # roll 'diceNum' dice of size 'dieSize'
        rollDict = {}
        rollTotal = 0
        for i in diceNum:
            rollDict[i] = self.rollDie(dieSize)
            rollTotal += rollDict[i]
        return self.dictToString(rollDict) + "\nTotal = " + rollTotal

    def dictToString(self, dict):
        results = ""
        results.join('Roll {}: {}\n'.format(k, v) for k, v in sorted(dict.items()))
        return results

# TODO: specify size of window, create instance, launch window
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
