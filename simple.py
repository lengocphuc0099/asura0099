from tkinter import *


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

window.mainloop()
