from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH
from tkinter.ttk import Frame, Style


class Window(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)
        # set background
        Style().configure("TFrame", background="#333")
        # create image object and load it in program
        bard = Image.open("/home/asura0099/Pictures/test/2.jpeg")
        bardejov = ImageTk.PhotoImage(bard)
        # create a object to display image
        label1 = Label(self, image=bardejov)
        # save referent to image
        label1.image = bardejov
        label1.place(x=20, y=20)

        rot = Image.open("/home/asura0099/Pictures/test/3.jpeg")
        rotunda = ImageTk.PhotoImage(rot)
        label2 = Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=280, y=20)

root = Tk()
root.geometry("800x800")
app = Window(root)
root.mainloop()
