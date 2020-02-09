from tkinter import *
from tkinter.ttk import *


window = Tk()
window.title("Welcome to ASURA app")
# Label widget
lbl = Label(window, text="hello world!", font=("Arial Bold", 14))
# position on from
lbl.grid(column=0, row=0)

#txt.grid(column=2, row=0)
# window size
window.geometry('500x200')
# Button widget
# handle button click event


def clicked():
    txt = Entry(window, width=10)
    txt.grid(column=2, row=0)
    res = "Welcome to" + txt.get()
    lbl.configure(text=res)


btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=1)
# combobox widget
combo = Combobox(window)
combo['values'] = (1, 2, 3, 5, "Text")
# set the selected item
combo.current(0)
combo.grid(column=0, row=2)
combo.get()
# checkbutton widget
chk_state = BooleanVar()
# set check state
chk_state.set(False)
chk = Checkbutton(window, text="choose", var=chk_state)
chk.grid(column=0, row=3)

# radio buttons widgets
rad1 = Radiobutton(window, text='First')
rad2 = Radiobutton(window, text='Second')
rad3 = Radiobutton(window, text='Third')
rad1.grid(column=0, row=4)
rad2.grid(column=1, row=4)
rad3.grid(column=2, row=4)
window.mainloop()
