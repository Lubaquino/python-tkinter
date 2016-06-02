from pyautogui import *
from tkinter import *
from tkinter import ttk
from time import sleep
from datetime import date

# activate the failsafe just in case.
# move your cursor to the top left of the screen
# to deactivate the program
FAILSAFE = True
PAUSE = 2.5

class Application(Frame):

    # initialize app
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # create the widgets

    def findAndSaveAttachment(self, k, v):
        # find and save email attachment using key-value pair

    def findAttachment(self, k, v):
        # find the attachment using key-value pair

    def saveAttachment(self, k, v):
        # save the attachment using key-value pair

    def changeFileName(self, k, v):
        # change filename of attachment before saving using key-value pair

    def saveProfile(self):
        # save all settings, filenames, file paths, etc to a text file

    def loadProfile(self):
        # load all settings, filenames, file paths, etc from a text file

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("Download attachments from Email")
    root.mainloop()
