from tkinter import *

class Form(Frame):#Tạo một lớp con kế thừa từ lớp Frame, Frame là một khung chứa tổ chức các widget trong giao diện
    def __init__(self, parent): #Phương thức khởi tạo chạy ngay khi Form được khởi tạo, parent là lớp cha (Tk())
        Frame.__init__(self, parent) #Gọi hàm khởi tạo của Frame giúp form hoạt động như 1 Frame, self chính là 1 Frame trong cửa sổ parent
        self.parent = parent#Lưu tham chiếu của parent vào self.parent để có thể dễ dàng truy cập cửa sổ ch
        self.initUI() #gọi phương thức initUI()

    def initUI(self):
        self.parent.title("Caculator")
        self.parent.configure(background="blue")
        self.grid() #Kích hoạt trình quản lý bố cục để sắp xếp Frame(self) trong cửa sổ cha

        self.expression = StringVar()

root = Tk() #Tạo cửa sổ chính
app = Form(root) #Tạo một đối tượng của lớp Form
root.geometry('600x400') 
root.mainloop() # Giữ cho cửa sổ luôn mở và lắng nghe sự kiện, nếu không có thì đóng ngay lập tức
