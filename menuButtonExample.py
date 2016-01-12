__author__ = 'cbartel'

from tkinter import *
from tkinter import ttk
from random import randint

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

        self.menubar.add_command(label="Hello!",
                                 command=self.helloGoodbye)
        self.menubar.add_command(label="Quit",
                                 command=root.quit)

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

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("Menubutton Example")
    root.mainloop()
