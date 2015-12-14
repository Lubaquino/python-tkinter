'''
Tk Grid Geometry Manager
http://www.tkdocs.com/tutorial/concepts.html
'''

from tkinter import *
from tkinter import ttk

# Columns and Rows
'''
Widgets are assigned a 'column' and 'row' number.
This indicates their relative position to each other.
Width of each column (or height of each row) depends on
the width/height of the widgets contained in the column/row.
'''

# Spanning Multiple Cells
'''
You can use 'columnspan' and 'rowspan' options to
specify how many cells the widget will span.

The following example shows some widgets that take
up more than a single cell
'''

root = Tk()

content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()
onevar.set(True)
twovar.set(False)
threevar.set(True)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=3, rowspan=2)
namelbl.grid(column=3, row=0, columnspan=2)
name.grid(column=3, row=1, columnspan=2)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.mainloop()

# Layout within the Cell
'''
By default, if a cell is larger than the widget contained in it,
the widget will be centered within it horizontally and vertically.
You can use the 'sticky' option to change this default behavior.

'sticky' option is a string of 0 or more cardinal directions:
"nsew":
    "n" = north (top of cell)
    "s" = south (bottom of cell)
    "e" = east (right of cell)
    "w" = west (left of cell)
    "nw" = northwest (top left of cell)
    "we" = westeast (stretch widget to left and right of cell)
    "nsew" = northsoutheastwest (stretch widget to all sides)
'''

# Handling Resize
'''
To update the positioning of the interface, we need to use the
'columnconfigure' and 'rowconfigure' methods of grid.
By default, each column has a 'weight' grid option of 1,
meaning: each column will expand at the same rate. However,
this can be modified.

There is also a 'minsize' grid option which specifies
a minimum size which prevents the window from being sized
down.
'''

# Padding
'''
Padding is the way you create spaces between widgets.
You can alter this with the 'padding' option.
Alternatively, you can use 'padx', 'pady' grid options.
    'padx' = adds space to left and right of widget
    'pady' = adds space to top and bottom of widget
A single value for the option puts the same padding on
left & right and top & bottom.
    Note: this padding is w/in the grid cell containing the widget.
If you want to add more padding around an entire row or column,
you can use the 'columnconfigure' and 'rowconfigure' methods.
These methods accept 'pad' options.

Let's alter the previous example and add padding:
'''

root = Tk()
content = ttk.Frame(root, padding=(3, 3, 12, 12))
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()

onevar.set(True)
twovar.set(False)
threevar.set(True)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

root.mainloop()

# Internal Padding
'''
External padding = if you have a 20x20 frame with external padding of 5 pix,
    the grid manager will grant it 20x20 pixels. The frame will end up being
    a 10x10 frame with a 5 pix border all around it.
Internal padding = if you have a 20x20 frame with internal padding of 5 pix,
    the grid manager will grant it 30x30 pixels. The frame will end up being
    a 20x20 frame with a 5 pix border all around it.
'''

# Forget and Remove
'''
'Forget' method of grid can be used to remove slaves/children from the grid
they're on.
It doesn't destroy the widget, it only takes it off the window as if it was
not "gridded" after being created. The grid options are not remembered.
'Remove' method has the same effect, except that the grid options will be
remembered.
'''

# Nested Layouts
'''
You can have more than one frame in a 'root' Tk object.
Within those frames can be nested more frames.
This is useful if you have a widget that is independent
of the other widgets.
'''
