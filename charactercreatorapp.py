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

        # TODO: create 6 text fields

        # TODO: create 2 drop-downs

        # TODO: create 3 buttons

        # TODO: create 3 radio buttons

        # TODO: arrange the frames within the window
        self.raceClassFrame.grid(row=0, column=0)
        self.radioDiceFrame.grid(row=1, column=0)
        self.buttonFrame.grid(row=2, column=0)
        self.statsFrame.grid(row=0, column=1)

    # TODO: function to determine racial bonus

    # TODO: function to export character to .txt file

    # TODO: function to roll stats

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("Create A Character!")
    root.mainloop()
