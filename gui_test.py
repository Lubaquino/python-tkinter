__author__ = 'cbartel'

# Here we import tkinter
import tkinter as tk

# Build the window using tkinter
class Application(tk.Frame):

    # When the program is executed:
    #   1. Create the window
    #   2. Run the .pack() function on self
    #   3. Run the .createWidgets() function on self
    # master=None means this is the parent object
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    # We want buttons, so we need a .createWidgets function
    def createWidgets(self):
        # Create a button called 'hi_there'
        self.hi_there = tk.Button(self)
        # Overlay the following text on button 'hi_there'
        self.hi_there["text"] = "Hello World\n(click me)"
        # When this button is clicked, run a function called 'say_hi'
        self.hi_there["command"] = self.say_hi
        # Place this button on the top of the Frame
        self.hi_there.pack(side="top")

        # Create a quit button that closes the window, make the text red
        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)

        # Place this button on the bottom of the Frame
        self.QUIT.pack(side="bottom")

    # Create the 'say_hi' function to handle when the 'hi_there' button is clicked
    def say_hi(self):
        # This is printed in the terminal
        print("hi there, everyone!")
        # TODO: Change this to be a popup window.

# Create a tkinter class object
# This object is needed for a Frame to be created
root = tk.Tk()
# Set the default size of the root tkinter object
root.geometry("400x300")

# Create the application, make it the parent object
app = Application(master=root)

# Start the program
app.mainloop()
