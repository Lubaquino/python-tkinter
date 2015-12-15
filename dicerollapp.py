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
        # TODO: create 3 labels
        self.rollLabel = tk.Label(self, text="Roll ")
        self.dLabel = tk.Label(self, text=" d ")
        self.timesLabel = tk.Label(self, text=" times.")
        # TODO: create 2 combo boxes
        numDiceVar = tk.StringVar()
        self.numDiceCombo = ttk.Combobox(self, state="readonly", textvariable=numDiceVar)
        diceSizeVar = tk.StringVar()
        self.diceSizeCombo = ttk.Combobox(self, state="readonly", textvariable=diceSizeVar)
        # TODO: create 2 text fields - one for input, one for output
        rollTimesVar = tk.IntVar()
        self.rollTimes = tk.Entry(self, textvariable=rollTimesVar)

# TODO: create dice rolling function

# TODO: error handlers

# TODO: specify size of window, create instance, launch window

