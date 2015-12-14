'''
Widgets
http://www.tkdocs.com/tutorial/morewidgets.html
'''

from tkinter import *
from tkinter import ttk

root = Tk()

'''
Listbox
'''
# Displays a list of single-line text items for the user to
#   select one or more
l = Listbox(root, height=10)
'''
Each listbox widget has a 'listvariable' config option.
    This allows you to link a variable, which must hold a list.
    Order of list stored in the variable is preserved in the widget.

You can specify how many selections the user is allowed to make with
    the 'selectmode' option.
    Default mode is 'browse' which means the user can only select
    one item. The mode 'extended' allows the user to select multiple
    items.

To find out which item(s) the user has selected, use the 'curselection'
    method. This returns the list of indices of all items currently
    selected. Alternatively, you can use the 'selection includes INDEX'
    method to see if the item with the given index is selected.

To programmatically change the selection, you can use 'selection
    clear FIRST ?LAST?' method to deselect a single or range of
    indices provided. To select an item or all items in a range
    use 'selection set FIRST ?LAST?' method. If the index is out
    of range (scrolled out of view), use the 'see index' method.

When a selection is made by the user, a '<ListboxSelect>' virtual
    event is generated. You can bind this to take any action you need.
    Depending on the app, you may also want to bind a double-click
    'Double-1' event.

The following example uses a listbox:
'''

root = Tk()

# Initialize our country "databases":
#  - the list of country codes (a subset anyway)
#  - a parallel list of country names, in the same order as the country codes
#  - a hash table mapping country code to population<
countrycodes = ('ar', 'au', 'be', 'br', 'ca', 'cn', 'dk', 'fi', 'fr', 'gr', 'in', 'it', 'jp', 'mx', 'nl', 'no', 'es', 'se', 'ch')
countrynames = ('Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada', 'China', 'Denmark', \
        'Finland', 'France', 'Greece', 'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Norway', 'Spain', \
        'Sweden', 'Switzerland')
cnames = StringVar(value=countrynames)
populations = {'ar':41000000, 'au':21179211, 'be':10584534, 'br':185971537, \
        'ca':33148682, 'cn':1323128240, 'dk':5457415, 'fi':5302000, 'fr':64102140, 'gr':11147000, \
        'in':1131043000, 'it':59206382, 'jp':127718000, 'mx':106535000, 'nl':16402414, \
        'no':4738085, 'es':45116894, 'se':9174082, 'ch':7508700}

# Names of the gifts we can send
gifts = { 'card':'Greeting card', 'flowers':'Flowers', 'nastygram':'Nastygram'}

# State variables
gift = StringVar()
sentmsg = StringVar()
statusmsg = StringVar()

# Called when the selection in the listbox changes; figure out
# which country is currently selected, and then lookup its country
# code, and from that, its population.  Update the status message
# with the new population.  As well, clear the message about the
# gift being sent, so it doesn't stick around after we start doing
# other things.
def showPopulation(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        code = countrycodes[idx]
        name = countrynames[idx]
        popn = populations[code]
        statusmsg.set("The population of %s (%s) is %d" % (name, code, popn))
    sentmsg.set('')

# Called when the user double clicks an item in the listbox, presses
# the "Send Gift" button, or presses the Return key.  In case the selected
# item is scrolled out of view, make sure it is visible.
#
# Figure out which country is selected, which gift is selected with the
# radiobuttons, "send the gift", and provide feedback that it was sent.
def sendGift(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = countrynames[idx]
        # Gift sending left as an exercise to the reader
        sentmsg.set("Sent %s to leader of %s" % (gifts[gift.get()], name))

# Create and grid the outer content frame
c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

# Create the different widgets; note the variables that many
# of them are bound to, as well as the button callback.
# Note we're using the StringVar() 'cnames', constructed from 'countrynames'
lbox = Listbox(c, listvariable=cnames, height=5)
lbl = ttk.Label(c, text="Send to country's leader:")
g1 = ttk.Radiobutton(c, text=gifts['card'], variable=gift, value='card')
g2 = ttk.Radiobutton(c, text=gifts['flowers'], variable=gift, value='flowers')
g3 = ttk.Radiobutton(c, text=gifts['nastygram'], variable=gift, value='nastygram')
send = ttk.Button(c, text='Send Gift', command=sendGift, default='active')
sentlbl = ttk.Label(c, textvariable=sentmsg, anchor='center')
status = ttk.Label(c, textvariable=statusmsg, anchor=W)

# Grid all the widgets
lbox.grid(column=0, row=0, rowspan=6, sticky=(N,S,E,W))
lbl.grid(column=1, row=0, padx=10, pady=5)
g1.grid(column=1, row=1, sticky=W, padx=20)
g2.grid(column=1, row=2, sticky=W, padx=20)
g3.grid(column=1, row=3, sticky=W, padx=20)
send.grid(column=2, row=4, sticky=E)
sentlbl.grid(column=1, row=5, columnspan=2, sticky=N, pady=5, padx=5)
status.grid(column=0, row=6, columnspan=2, sticky=(W,E))
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(5, weight=1)

# Set event bindings for when the selection in the listbox changes,
# when the user double clicks the list, and when they hit the Return key
lbox.bind('<<ListboxSelect>>', showPopulation)
lbox.bind('<Double-1>', sendGift)
root.bind('<Return>', sendGift)

# Colorize alternating lines of the listbox
for i in range(0,len(countrynames),2):
    lbox.itemconfigure(i, background='#f0f0ff')

# Set the starting state of the interface, including selecting the
# default gift to send, and clearing the messages.  Select the first
# country in the list; because the <<ListboxSelect>> event is only
# generated when the user makes a change, we explicitly call showPopulation.
gift.set('card')
sentmsg.set('')
statusmsg.set('')
lbox.selection_set(0)
showPopulation()

root.mainloop()

'''
Scrollbar
'''
# A scrollbar allows the user to see all parts of another widget
s = ttk.Scrollbar(root, orient=VERTICAL, command=listbox.yview)
listbox.configure(yscrollcommand=s.set)
'''
Scrollbars are separate widgets altogether.
However, scrollbars communicate with the scrolled widget by calling
    methods on the scrolled widget.

The 'orient' scrollbar option determines whether it will scroll
    in the 'horizontal' or 'vertical' direction. You then need to
    set up the 'command' config option to communicate with the
    scrolled widget. This needs to be te method to call on the
    scrolled widget.

Every widget that can be scrolled vertically has a 'yview' method,
    and every widget that can be scrolled horizontally has a
    'xview' method.

The scrolled widget needs to go back and tell the scrollbar what
    percentage of the widget is now visible. Every scrollable
    widget has a 'yscrollcommand' and/or 'xscrollcommand' option.
    This is used to specify a method call which must be the
    scrollbar's 'set' method.

Here is an example that uses a scrollbar:
'''

root = Tk()
l = Listbox(root, height=5)
l.grid(column=9, row=0, sticky=(N,W,E,S))
s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=1, row=0, sticky=(N,S))
l['yscrollcommand'] = s.set
ttk.Sizegrip().grid(column=1, row=1, sticky=(S,E))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
for i in range(1, 101):
    l.insert('end', 'Line %d of 100' % i)
root.mainloop()

'''
SizeGrip
'''
# SizeGrip is a little box at the bottom right corner
#   of the winder that allows you to resize it.
ttk.Sizegrip(root).grid(column=999, row=999, sticky=(S,E))

'''
Text
'''
# Provides users with an area that they can enter
#   multiple lines of text
t = Text(root, width=40, height=40)
'''
'width' and 'height' options specify the size of the widget
    in characters and rows, respectively. You can use 'wrap'
    option with the following option values:
     - 'none' = no wrapping, text will horizontally scroll
     - 'char' = wrap at any character
     - 'word' = wrap only on word boundaries

Like an entry field, a text widget can be disabled so that
    no editing can occur. Since this is not a themed widget,
    however, you need to set the 'state' option to either
    'disabled' or 'normal'.

Scrolling works the same in listboxes. Use 'xscrollcommand'
    and 'yscrollcommand' options to attach this widget to horizontal
    or vertical scrollbars. 'xview' and 'yview' methods are available
    to be called from scrollbars.

Text widgets have no linked variable associated with them, unlike
    the entry widget.

Text can be added by using 'insert INDEX STRING' method. 'index'
    is in the form "line.char" and marks the character before
    which text is inserted. Use 'end' to add text to the end
    of a widget.

You can delete a range of text using 'delete START END' method,
    where both "start" and "end" are text indices in the form
    "line.char".
'''
