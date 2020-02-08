from tkinter import *

window = Tk()
window.title("Welcome to ASURA app")
# Label widget
lbl = Label(window, text = "hello world!", font = ("Arial Bold",14))
# position on from 
lbl.grid(column = 0, row = 0)
# window size
window.geometry('500x200')
# Button widget
btn = Button(window, text = "Click Me")
btn.grid(column = 0, row = 1)
window.mainloop()
