from pyautogui import *
from tkinter import *
from tkinter import ttk
from time import sleep
from datetime import date

FAILSAFE = True
PAUSE = 2.5

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.reportEmailDict = {}
        self.stringVarsA = []
        self.stringVarsB = []
        self.lineCount = 0
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.masterFrame = Frame(self)
        self.frame1 = Frame(self.masterFrame)
        self.frame5 = Frame(self.masterFrame)
        self.frame2 = Frame(self.masterFrame)
        self.frame4 = Frame(self.masterFrame)
        self.frame3 = Frame(self.masterFrame)

        self.screenshotLabel = Label(self.frame1,
                                     text="Path to screenshots: ")
        self.appendDateLabel = Label(self.frame2,
                                     text="Include date on filename(s)? ")

        self.screenshotEntryVar = StringVar()
        self.screenshotEntry = Entry(self.frame1,
                                     textvariable=self.screenshotEntryVar)
        self.screenshotEntryVar.set("C:\\docs\\pics\\")

        self.liveText = Text(self.frame5,
                             wrap=WORD,
                             width=40,
                             height=20)
        self.liveText.insert(END,
                             "Live feed of program activity.\n")

        self.addReportButton = Button(self.frame2,
                                      text="Add",
                                      command=self.addReportLine)
        self.deleteReportButton = Button(self.frame2,
                                         text="Delete",
                                         command=self.deleteReportLine)
        self.runButton = Button(self.frame2,
                                text="Print",
                                command=self.printStuff)

        self.masterFrame.grid(row=0, column=0)
        self.frame1.grid(row=0, column=0)
        self.frame5.grid(row=1, column=0)
        self.frame2.grid(row=2, column=0)
        self.frame4.grid(row=2, column=1)
        self.frame3.grid(row=3, column=0)

        self.screenshotLabel.grid(row=0, column=0)
        self.appendDateLabel.grid(row=0, column=0)

        self.screenshotEntry.grid(row=0, column=1)

        self.liveText.grid(row=0, column=0)

        self.addReportButton.grid(row=0, column=1)
        self.deleteReportButton.grid(row=0, column=2)
        self.runButton.grid(row=0, column=3)

    def addReportLine(self):
        self.lineCount += 1

        self.liveText.insert(END, "New line added.\n")

        self.newReportFrame = Frame(self.frame3)

        self.label1 = Label(self.newReportFrame,
                            text="A: ")

        self.entry1Var = StringVar()
        self.entry1 = Entry(self.newReportFrame,
                            textvariable=self.entry1Var)
        self.entry1Var.set("a")
        self.stringVarsA.insert(self.lineCount, self.entry1Var)

        self.label2 = Label(self.newReportFrame,
                            text="B: ")

        self.entry2Var = StringVar()
        self.entry2 = Entry(self.newReportFrame,
                            textvariable=self.entry2Var)
        self.entry2Var.set("b")
        self.stringVarsB.insert(self.lineCount, self.entry2Var)

        self.newReportFrame.grid(row=self.lineCount, column=0)

        self.label1.grid(row=0, column=0)
        self.entry1.grid(row=0, column=1)

        self.label2.grid(row=0, column=2)
        self.entry2.grid(row=0, column=3)

    def deleteReportLine(self):

        try:
            self.stringVarsA.remove(self.stringVarsA[self.lineCount - 1])
            self.stringVarsB.remove(self.stringVarsB[self.lineCount - 1])
            self.liveText.insert(END, "Report line deleted.\n")
        except:
            self.liveText.insert(END, "Nothing to delete!\n")

        for child in self.frame3.grid_slaves():
            if int(child.grid_info()["row"]) == self.lineCount:
                child.destroy()

        self.lineCount -= 1

        if self.lineCount < 0:
            self.lineCount = 0

    def printStuff(self):
        self.liveText.insert(END, "Data printed to console.\n")
        for i in range(self.lineCount):
            print(self.stringVarsA[i], ", ", self.stringVarsB[i])
            print(self.stringVarsA[i].get(), ", ", self.stringVarsB[i].get())
        print(list(self.stringVarsA))
        print(list(self.stringVarsB))

    def createDictionary(self):
        return None

    def findAndSaveAttachment(self, k, v):
        self.findAttachment(k, v)
        self.saveAttachment(k, v)

    def findAttachment(self, k, v):
        return k, v

    def saveAttachment(self, k, v):
        return k, v

    def changeFileName(self, k, v):
        return k, v

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("Download attachments from email")
    root.mainloop()
