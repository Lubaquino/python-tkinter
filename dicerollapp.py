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
        # TODO: create one button to roll the dice
        self.rollDice = tk.Button(self)
        self.rollDice["text"] = "Roll!"
        # TODO: create frame to house text output
        self.outputFrame = tk.Frame(self)
        # TODO: create 4 labels
        self.rollLabel = tk.Label(self, text="Roll ")
        self.dLabel = tk.Label(self, text=" d ")
        self.timesLabel = tk.Label(self, text=" times.")
        self.resultsVar = tk.StringVar()
        self.resultsLable = tk.Label(self)
        # TODO: create 2 combo boxes
        self.numDiceVar = tk.StringVar()
        self.numDiceCombo = ttk.Combobox(self, state="readonly", textvariable=self.numDiceVar)
        self.diceSizeVar = tk.StringVar()
        self.diceSizeCombo = ttk.Combobox(self, state="readonly", textvariable=self.diceSizeVar)
        # TODO: create 1 text fields for input
        self.rollTimesVar = tk.IntVar()
        self.rollTimes = tk.Entry(self, textvariable=self.rollTimesVar)

# TODO: create dice rolling function
    def rollDie(self, dieSize):
        # TODO: roll one die with randint
        return randint(1, dieSize)

    def diceRolls(self, dieSize, diceNum):
        # TODO: roll 'diceNum' dice of size 'dieSize'
        rollDict = {}
        for i in diceNum:
            rollDict[i] = randint(1, dieSize)
        return rollDict

# TODO: create data validation for the entry widget

# TODO: error handlers

# TODO: specify size of window, create instance, launch window

