from tkinter import Tk, BOTH 
from tkinter.ttk import Frame, Button, Style
#Lop Tk dung de tao cua so
#Frame dung de quan ly widget
class Example(Frame):#Tao lop Example duoc goi chung la container, layout
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent#Luu doi tuong root
        self.initUI()#dung de tao cac widget tren cua so
    
    def initUI(self):
        self.parent.title("VD1-2212453")#Thay doi tieu de cua so
        self.style = Style()
        self.style.theme_use("default")#Quy dinh kieu theme
        self.pack(fill=BOTH, expand= 1)#Sap xep cac widget truoc khi hien thi len cua so chinh, fill=BOTH dan widget ra chieu ngang va chieu rong

        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=50, y=50)#Quy dinh vi tri nut bam

#Cua so luon phai duoc tao ra truoc widget
root = Tk()
root.geometry("250x150+300+300")#geometry giup quy dinh kich thuoc cua so, 2 tham so dau la kich thuoc cua so, 2 tham so sau la vi tri cua so
app = Example(root)#Tao 1 frame va gan vao cua so chinh
root.mainloop()#Phuong thuc quan trong de hien thi cua so