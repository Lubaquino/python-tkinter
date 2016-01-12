__author__ = 'cbartel'

from tkinter import *
from tkinter import messagebox
from random import randint
import sys

class Application(Frame):

    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):

        # TODO: create 2 frames
        self.f1 = Frame(self)
        self.f2 = Frame(self)

        # TODO: create 3 radiobuttons
        self.i = IntVar()
        self.r1 = Radiobutton(self.f1,
                              variable=self.i,
                              value=1,
                              text='One')
        self.r2 = Radiobutton(self.f1,
                              variable=self.i,
                              value=2,
                              text='Two')
        self.r3 = Radiobutton(self.f1,
                              variable=self.i,
                              value=3,
                              text='Three')
        self.r3.select()

        # TODO: create button
        self.b = Button(self.f1,
                        text='Button',
                        command=self.helloGoodbye)

        # TODO: create text field
        self.t = Text(self.f2,
                      wrap=WORD,
                      height=10,
                      width=20)
        self.t.insert(INSERT, "Text field")

        # TODO: create scrollbars for text widget and attach
        self.sx = Scrollbar(self.f2,
                            orient=HORIZONTAL)
        self.sy = Scrollbar(self.f2)

        self.t.config(yscrollcommand=self.sy.set,
                      xscrollcommand=self.sx.set)

        self.sy.config(command=self.t.yview)
        self.sx.config(command=self.t.xview)

        # TODO: create menubutton for File, Help, About
        self.menubar = Menu(root)

        self.filemenu = Menu(self.menubar,
                             tearoff=0)
        self.filemenu.add_command(label="Open",
                                 command=self.helloGoodbye)
        self.filemenu.add_command(label="Save",
                                 command=self.helloGoodbye)
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

        # TODO: arrange widgets in window with grid
        self.f1.grid(row=1,
                     column=0)
        self.r1.grid(row=0,
                     column=0)
        self.r2.grid(row=1,
                     column=0)
        self.r3.grid(row=2,
                     column=0)
        self.b.grid(row=3,
                    column=0)

        self.f2.grid(row=1,
                     column=1)
        self.t.grid(row=0,
                    column=0)
        self.sy.grid(row=0,
                     column=1,
                     sticky=N+S)
        self.sx.grid(row=1,
                     column=0,
                     sticky=W+E)


    # TODO: create example functions
    def sayHello(self):
        return 'Hello!'

    def sayGoodBye(self):
        return 'Goodbye.'

    def helloGoodbye(self):
        r = randint(1, 2)
        if r < 2:
            self.t.insert(INSERT, '\n'+self.sayHello())
        else:
            self.t.insert(INSERT, '\n'+self.sayGoodBye())

    # TODO: create 2 messageboxes for about/help
    def about(self):
        messagebox.showinfo("About",
                            "Written by: Chad Bartel\n" +
                            "Using Python ver " + sys.version)

    def help(self):
        messagebox.showinfo("Help",
                            "Clicking the 'About' menu shows you info about\n" +
                            "the program and who wrote it.\n\n" +
                            "The radio buttons are decorative only.\n" +
                            "The 'Button' button randomly chooses between\n" +
                            "saying 'Hello!' or 'Goodbye.' in the text field.\n\n" +
                            "The options 'Open' and 'Save' use the same command\n" +
                            "as 'Button'. Except 'Quit' will terminate the window.\n")

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("Menubutton Example")
    root.mainloop()
