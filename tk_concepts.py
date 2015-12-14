'''
Tk Concepts
http://www.tkdocs.com/tutorial/concepts.html
'''

from tkinter import *
from tkinter import ttk

# HIERARCHY
'''
When creating a widget, you must pass its parent
as a paramter to the widget creation function.
'''
# Example
root = Tk()                     # 'Root' widget object
content = ttk.Frame(root)       # 'Content' widget to contain other widgets
button = ttk.Button(content)    # Therefore, 'button' is a child of 'content'
'''
You don't have to store all your widget objects in a variable.
They don't get garbage collected after creating your Frame.
'''


# CONFIGURATION OPTIONS
'''
Options can be set for a widget when its first created.
'''
# Example
root = Tk()
# Create a button, passing two options
button = ttk.Button(root, text="Hello", command="buttonpressed")
button.grid()
# Check the current value of the text option
print(button['text'])
# Change the value of the text option
button['text'] = 'goodbye'
# Another way to do the same thing
button.configure(text='goodbye')
# Check the current value of the text option
print(button['text'])
# Get all information about the text option
print(button.configure('text'))
# Get information on all options for this widget
print(button.configure())


# GEOMETRY MANAGEMENT (GRID)
'''
This is the concept of how to place widgets in your window.

Understanding the following OPTIONS may help with a grid:
column              # cell address y
row                 # cell address x
sticky              # alignment
columnconfigure     # columns to expand if extra space available
rowconfigure        # rows to expand if extra space available
'''


# EVENT HANDLING
'''
Events like button presses, keystrokes, mouse movement,
window resizing, etc.

Some events are already handled for you, for example buttons.
'''
# Example with event bindings
root = Tk()
# Create label widget as child of 'root'
l = ttk.Label(root, text="Starting...")
# Apply 'l' to 'grid' Geometry Mgmt
l.grid()
# When the mouse is in the label's area, change the label text
l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
# When the mouse is out of the label's area, change the label text
l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
# When the user clicks the left mouse button, change the label text
l.bind('<1>', lambda e: l.configure(text='Clicked left mouse button'))
# When the user double-clicks the left mouse button, change the label text
l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
# When the user right clicks and drags the mouse, change the label text dynamically
l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d, %d' % (e.x, e.y)))
# Run the program
root.mainloop()


# BASIC WIDGETS
'''
An overview of the most common widgets:
frames
labels
buttons
checkbuttons
radiobuttons
entries
comboboxes
'''
root = Tk()
'''
Frame
'''
# A simple rectangle widget
frame = ttk.Frame(root)
# Padding - Specify extra space around the widget
frame['padding'] = (5, 10)
# Borders & relief - Border around the widget, type of border
frame['borderwidth'] = 2
#   Other visual styles: flat (default), raised, sunken, solid, ridge, groove
frame['relief'] = 'sunken'
'''
Label
'''
# A widget that displays text or images
label = ttk.Label(frame, text='Full name:')
# Displaying text
#   Read or write the current value using the 'get' and 'set' methods
resultsContents = StringVar()
label['textvariable'] = resultsContents
resultsContents.set('New value to display')
# Displaying images
#   Other options: text, image, center, top, left, bottom, right
image = PhotoImage(file='myimage.gif')
label['image'] = image
# Layout
'''
There are several options that let you control how
the label will be displayed within the box

If the box given to the label is larger than the label requires
you can use 'anchor' to specify which edge/corner the label will be.
These values are specified as compass directions: n, ne, e, se, s, sw, w, nw, center

Labels can display more than one line of text.
This can be achieved with '\n' or the 'wraplength' option.

You can also control how the text is justified with the 'justify' option.
These values are: left, center, right.
If it is just 1 line of text, it effectively is the same as using the anchor option
'''
# Fonts, Colors and More
'''
These are specific properties to labels

TkDefaultFont
TkTextFont
TkFixedFont
TkMenuFont
TkHeadingFont
TkSmallCaptionFont
TkIconFont
TkTooltipFont
'''

'''
Button
'''
# Widget that is used to perform an action
button = ttk.Button(root, text='Okay', command=submitForm)
# Options: text, textvariable, image, compund, default, command
# Command Callback
button.invoke()
# Button State
'''
All themed widgets carry an internal states which is
a series of binary flags.
'''
button.state(['disabled'])              # set the disabled flag, disabling the button
button.state(['!disabled'])             # clear the disabled flag
button.instate(['disabled'])            # return true if the button is disabled, else false
button.instate(['!disabled'])           # return true if the button is not disabled, else false
button.instate(['!disabled'], cmd)      # execute 'cmd' if the button is not disabled

'''
Checkbutton
'''
# A button that holds a binary value
measureSystem = StringVar()
check = ttk.Checkbutton(root, text='Use Metric',
                        command=metricChanged, variable=measureSystem,
                        onvalue='metric', offvalue='imperial')
# Options: text, textvariable, image, compound, command, onvalue, offvalue
# Methods: state, instate
'''
Unlike buttons, checkbuttons can hold a value.
By default, checkbuttons use a value of 1 when the widget is checked
and a 0 when not checked.
These default values can be changed using the onvalue/offvalue options.

When the linked variable has neither an on/off value,
the checkbutton is put into a special 'tristate' or indeterminate mode.
Essentially, it can hold 3 values instead of 2 in this mode.
You can enable this by using the flag 'alternate' and you can
check for it with the 'instate method:
'''
check.instate(['alternate'])

'''
Radiobutton
'''
# A button that lets you choose b/w one of a # of mutually exclusive choices
phone = StringVar()
home = ttk.Radiobutton(root, text='Home', variable=phone, value='home')
office = ttk.Radiobutton(root, text='Office', variable=phone, value='office')
cell = ttk.Radiobutton(root, text='Mobile', variable=phone, value='cell')
'''
Each of the radiobuttons of the set have the same linked variable,
but a different value; when the var has the given value,
the radiobutton will be selected, otherwise unselected.

When a linked variable does not exist, radiobuttons also display
a 'tristate' or indeterminate, which can be checked via the
'alternate' state flag.
'''

'''
Entry
'''
# A single line text field for the user to type in a string
username = StringVar()
name = ttk.Entry(root, textvariable=username)
'''
The 'width' option lets you restrict the # of chars can be entered.
The linked variable is specified with the 'textvariable' option.
You can get/change the value of the entry widget directly:
    'get' method = returns current value
    'delete'/'insert' method = change contents
'''
print('current value is %s' % name.get())
name.delete(0, 'end'))              # delete b/w two indices, 0-based
name.insert(0, 'your name')         # insert new text at a given index
'''
Entries do not have a command option.
Therefore, if you want to watch for changes on the entry,
you need to watch for changes on the linked variable.

You can use ENTRY for passwords by using the 'show' option.

Entry fields can be put into a disabled state
via the 'state' command and queried with 'instate' method.
Entries can use the 'readonly' flag where the user cannot
change the entry but can select the text and copy it.
There is also an 'invalid' state, to check the validation of the entry.
'''

'''
Combobox
'''
# Combines entry with a list of choices
countryvar = StringVar()
country = ttk.Combobox(root, textvariable=countryvar)
'''
You can get the current value of with 'get' and
change the current value using the 'set' method

Comboboxes generate virtual events "<ComboboxSelected>" that
you can bind to whenever its value changes
'''
country.bind('<<ComboboxSelected>>', function)
# You can supply predefined values to choose from
# with the 'values' config option
country['values'] = ('USA', 'Canada', 'Australia')
'''
You can use the 'readonly' state flag to restrict the user
to only make selections from a predefined list rather than
entering their own values.

You can use the 'current' method to determine which item
in the predefined values list is selected (used with 'get'
and 'set' method).
'''
