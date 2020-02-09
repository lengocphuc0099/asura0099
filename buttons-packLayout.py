from tkinter import Tk, RIGHT, BOTH, GROOVE
from tkinter.ttk import Frame, Button, Style

### pack  ###
class Windon(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
    	self.parent.title("Button")
    	self.style = Style()
    	self.style.theme_use("default")

    	frame = Frame(self, relief = GROOVE, borderwidth = 1)
    	frame.pack(fill = BOTH, expand = True)
    	self.pack(fill = BOTH, expand = True)
    	closeButton = Button(self, text = "Close")
    	closeButton.pack(side = RIGHT, padx = 5, pady = 5)
    	okButton = Button(self, text = "Ok")
    	okButton.pack(side = RIGHT)




root = Tk()
root.geometry("500x500")
app = Windon(root)
root.mainloop()