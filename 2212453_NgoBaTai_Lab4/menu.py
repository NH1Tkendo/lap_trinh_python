from tkinter import Frame, Tk, Menu

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Simple Menu")

        menuBar = Menu(self.parent, tearoff=0)
        self.parent.config(menu = menuBar)

        fileMenu = Menu(menuBar)
        subMenu = Menu(fileMenu)
        subMenu.add_command(label="New Feed")
        subMenu.add_command(label="1")
        subMenu.add_command(label="2")
        fileMenu.add_cascade(label="Import", menu=subMenu)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.onExit)
        menuBar.add_cascade(label="File", menu=fileMenu)
        
        self.popupMenu = Menu(menuBar)
        self.popupMenu.add_command(label="Beep", command=self.bell)
        self.popupMenu.add_command(label="Exit", command=self.onExit)
        menuBar.add_cascade(label="@@", menu=self.popupMenu)
        self.parent.bind("<Button-3>", self.showMenu)
        self.pack()

    def showMenu(self, e):
        self.popupMenu.post(e.x_root, e.y_root)
    def onExit(self):
        self.quit()

root = Tk()
root.geometry("250x150+300+300")
app = Example(root)
root.mainloop()
