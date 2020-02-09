from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button, Style

class Window(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.initUI()


	def initUI(self):
		self.parent.title("Quit Button")
		self.style = Style()
		self.style.theme_use("default")
		self.pack(fill = BOTH, expand = 1)

		quitButton = Button(self, text = "Quit", command = self.quit)
		quitButton.place(x = 0, y = 475)

root = Tk()
root.geometry("500x500")
app = Window(root)
root.mainloop()