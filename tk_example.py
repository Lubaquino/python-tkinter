__author__ = 'cbartel'

'''
The following program converts feet to meters
from input from the user.
'''

# Import the Tk library
from tkinter import *
# Import the "themed" widgets library
from tkinter import ttk

# Create the calculate function
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

# Set up the main window
root = Tk()
# Add a title to the window
root.title("Feet to Meters")
# This is the widget that holds all other widgets
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# If the main window is re-sized, expand the frame to take the extra space
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Create the feet and meters variables
feet = StringVar()
meters = StringVar()
# Create the object to take user input
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# Place the 'feet_entry' input field in the frame
feet_entry.grid(column=2, row=1, sticky=(W, E))
# Create the label that displays the output, place it in the frame, anchor to left and right of cell
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
# Create the button that runs the calculation, place it in the frame, anchor to left of cell
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# Create 3 static labels, pick the cell, and anchor them
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# Iterate through all child widgets and add 5 pix of padding to each
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
# Place the cursor in the 'feet_entry' field when the window opens
feet_entry.focus()
# If the user presses the "Return"/"Enter" key, then run the calculate function
root.bind('<Return>', calculate)

# Run the program
root.mainloop()
