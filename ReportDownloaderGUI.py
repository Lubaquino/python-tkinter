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

# Something to bear in mind when/if you want to dynamically add/remove widgets
# http://stackoverflow.com/questions/14804735/tkinter-how-can-i-dynamically-create-a-widget-that-can-then-be-destroyed-or-rem

class Application(Frame):

    # initialize app
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    # create the widgets
    def createWidgets(self):
        # add frames
        self.masterFrame = Frame(self)
        # this is a temporary pack, this will be cleaned up later
        self.masterFrame.pack()

        # on button press, add a new report line
        self.addReportButton = Button(self.masterFrame,
                                      text="Add Report",
                                      command=self.addReportLine)
        # this is a temporary pack, this will be cleaned up later
        self.addReportButton.pack()

        # create button to run the search and download on what is in the entry fields
        self.runButton = Button(self.masterFrame,
                                text="Run",
                                command=self.findAndSaveAttachment)

    # add new line to window to search and dl another file
    def addReportLine(self):
        # create frame to house the newly added widgets
        self.newReportFrame = Frame(self.masterFrame)
        self.newReportFrame.pack()

        # create label to indicate what entry widget is used for
        self.label1 = Label(self.newReportFrame,
                            text="Report file name: ")
        self.label1.grid(row=0, column=0)

        # create entry widget to take user input for filename and extension
        self.entry1 = Entry(self.newReportFrame)
        # clear any contents that might be in the entry widget and put placeholder text
        self.entry1.delete(0, END)
        self.entry1.insert(0, "Type filename and extension here")
        self.entry1.grid(row=0, column=1)

        # create button that deletes all widgets in new frame and self
        self.dButton = Button(self.newReportFrame,
                              text="Click to delete this line")
        self.dButton.config(command=self.newReportFrame.destroy)
        self.dButton.grid(row=0, column=2)

    def findAndSaveAttachment(self, k, v):
        # find and save email attachment using key-value pair
        self.findAttachment(k, v)
        self.saveAttachment(k, v)

    def findAttachment(self, k, v):
        # find the attachment using key-value pair

    def saveAttachment(self, k, v):
        # save the attachment using key-value pair

    def changeFileName(self, k, v):
        # change filename of attachment before saving using key-value pair

    def createDictionary(self):
        # create dictionary containing key-value pairs
            # key   = filename of picture + extension
            # value = full save path + save as name

    def saveProfile(self):
        # save all settings, filenames, file paths, etc to a text file

    def loadProfile(self):
        # load all settings, filenames, file paths, etc from a text file

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("Download attachments from Email")
    root.mainloop()
