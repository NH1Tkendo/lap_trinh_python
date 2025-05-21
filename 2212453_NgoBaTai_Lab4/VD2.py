from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH, RAISED, RIGHT
from tkinter.ttk import Frame, Style, Button, Entry

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Absolute positioning")
        self.style = Style()
        self.style.theme_use("default")
        
        Style().configure("TFrane", background = "#333")#To mau nen xam den
        
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        #Tao cac doi tuong anh va tai chung vao chuong trinh
        hinh1 = Image.open("Z:\\1.jpg")
        hinh1 = hinh1.resize((100,100), Image.LANCZOS)
        hinh11 = ImageTk.PhotoImage(hinh1)
        #-----
        #Hien thi chu va anh
        label1 = Label(self, image = hinh11)
        label1.image = hinh11
        label1.place(x=20,y=20)
        #------

        hinh2 = Image.open("Z:\\2.jpg")
        hinh2 = hinh2.resize((100,100), Image.LANCZOS)
        hinh22 = ImageTk.PhotoImage(hinh2)
        label2 = Label(self, image = hinh22)
        label2.image = hinh22
        label2.place(x=40,y=160)

        hinh3 = Image.open("Z:\\3.jpg")
        hinh3 = hinh3.resize((100,100), Image.LANCZOS)
        hinh33 = ImageTk.PhotoImage(hinh3)
        label3 = Label(self, image = hinh33)
        label3.image = hinh33
        label3.place(x=170,y=50)

        closeButton = Button(self, text="Close")
        closeButton.pack(side = RIGHT, padx = 5, pady= 5)
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)

root = Tk()
root.geometry("300x300+300+300")
app = Example(root)
root.mainloop()

