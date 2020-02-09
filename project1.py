from tkinter import Tk, Frame, BOTH


class Window(Frame):
    """docstring for MyClass"""

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("MyApp - 1")
        self.pack(fill=BOTH, expand=1)


root = Tk()
root.geometry("500x500")
app = Window(root)
root.mainloop()
