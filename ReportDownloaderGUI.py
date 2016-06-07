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
        self.reportEmailDict = {}
        self.lineCount = 0
        self.pack()
        self.createWidgets()

    # create the widgets
    def createWidgets(self):
        # add frames
        self.masterFrame = Frame(self)
        self.masterFrame.grid(row=0, column=0)
        # frame for full file path of all screenshots and appending date on file save
        self.frame1 = Frame(self.masterFrame)
        self.frame1.grid(row=0, column=0)
        # frame for live text widget
        self.frame5 = Frame(self.masterFrame)
        self.frame5.grid(row=1, column=0)
        # frame for label and add report button
        self.frame2 = Frame(self.masterFrame)
        self.frame2.grid(row=2, column=0)
        # frame to contain run button below attachment lines
        self.frame4 = Frame(self.masterFrame)
        self.frame4.grid(row=2, column=1)
        # frame to house all attachment lines
        self.frame3 = Frame(self.masterFrame)
        self.frame3.grid(row=3, column=0)

        # add labels
        self.screenshotLabel = Label(self.frame1,
                                     text="Path to screenshots: ")
        self.screenshotLabel.grid(row=0, column=0)
        self.appendDateLabel = Label(self.frame2,
                                     text="Include date on filename(s)? ")
        self.appendDateLabel.grid(row=0, column=0)

        # add screenshot path entry widget
        self.screenshotEntryVar = StringVar()
        self.screenshotEntry = Entry(self.frame1,
                                     textvariable=self.screenshotEntryVar)
        self.screenshotEntryVar.set("C:\\docs\\pics\\")
        self.screenshotEntry.grid(row=0, column=1)

        # text widget to display live updates
        self.liveText = Text(self.frame5,
                             wrap=WORD,
                             width=40,
                             height=20)
        self.liveText.insert(END,
                             "This is where you'll see the live activity feed from the program.\n")
        self.liveText.grid(row=0, column=0)

        # add buttons
        # add button to create attachment lines
        self.addReportButton = Button(self.frame2,
                                      text="Add Report",
                                      command=self.addReportLine)
        self.addReportButton.grid(row=0, column=1)
        # create button to run the search and download on what is in the entry fields
        self.runButton = Button(self.frame4,
                                text="Run",
                                command=self.createDictionary)
        self.runButton.grid(row=0, column=2)

    # add new line to window to search and dl another file
    def addReportLine(self):
        # increase our count of the number of lines on the GUI
        self.lineCount += 1

        # create frame to house the newly added widgets
        self.newReportFrame = Frame(self.frame3)
        self.newReportFrame.pack()

        # create label to indicate what entry widget is used for
        self.label1 = Label(self.newReportFrame,
                            text="Email subject screenshot: ")
        self.label1.grid(row=0, column=0)

        # create entry widget to take user input for filename and extension
        self.entry1Var = StringVar()
        self.entry1 = Entry(self.newReportFrame,
                            textvariable=self.entry1Var)
        self.entry1Var.set("Enter screenshot filename and extension here")
        self.entry1.grid(row=0, column=1)

        # create entry widget to take user input for full save path and new file name
        self.label2 = Label(self.newReportFrame,
                            text="Report save path: ")
        self.label2.grid(row=0, column=2)

        # create entry widget to take save path and new file name
        self.entry2Var = StringVar()
        self.entry2 = Entry(self.newReportFrame,
                            textvariable=self.entry2Var)
        self.entry2Var.set("Enter full save path and new file name")
        self.entry2.grid(row=0, column=3)

        # create button that deletes all widgets in new frame and self
        self.dButton = Button(self.newReportFrame,
                              text="Click to delete this line")
        self.dButton.config(command=self.newReportFrame.destroy)
        self.dButton.bind("<Button-1>", lambda e: self.reduceLineCount())
        self.dButton.grid(row=0, column=4)

    def reduceLineCount(self):
        self.lineCount -= 1

    def createDictionary(self):
        # create dictionary containing key-value pairs
            # key   = filename of picture + extension
            # value = full save path + save as name
        return None

    def saveProfile(self):
        # save all settings, filenames, file paths, etc to a text file
        return None

    def loadProfile(self):
        # load all settings, filenames, file paths, etc from a text file
        return None

    def findAndSaveAttachment(self, k, v):
        # find and save email attachment using key-value pair
        self.findAttachment(k, v)
        self.saveAttachment(k, v)

    def findAttachment(self, k, v):
        # find the attachment using key-value pair
        return k, v

    def saveAttachment(self, k, v):
        # save the attachment using key-value pair
        return k, v

    def changeFileName(self, k, v):
        # change filename of attachment before saving using key-value pair
        return k, v

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("Download attachments from email")
    root.mainloop()
