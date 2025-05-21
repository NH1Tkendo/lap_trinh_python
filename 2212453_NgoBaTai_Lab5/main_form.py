from tkinter import *
from tkinter.ttk import Style, Combobox
from sql_helper import get_nhom_food, get_tt_food, cbb_choice
from tkinter import ttk

class Form(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Quản lý món ăn")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        # Frame trên chứa Combobox
        top = Frame(self, pady=20, padx=100)
        top.grid(column=0, row=0)

        text = Label(top, text="Chọn loại món ăn", padx=50)
        text.grid(column=0, row=0)

        self.loai_thuc_an = Combobox(top)
        self.loai_thuc_an["values"] = get_nhom_food()
        self.loai_thuc_an.grid(column=1, row=0)

        # Gắn sự kiện khi chọn combobox
        self.loai_thuc_an.bind("<<ComboboxSelected>>", self.cbb_choice)

        # Frame dưới chứa Treeview
        bottom = Frame(self)
        bottom.grid(column=0, row=1)

        self.treev = ttk.Treeview(bottom, selectmode="browse")

        # Thanh cuộn dọc
        verscrlbar = ttk.Scrollbar(bottom, orient="vertical", command=self.treev.yview)
        verscrlbar.pack(side="right", fill="y")
        self.treev.configure(yscrollcommand=verscrlbar.set)

        # Định nghĩa cột
        self.treev["columns"] = ("1", "2", "3", "4", "5")
        self.treev["show"] = "headings"

        self.treev.column("1", width=90, anchor="c")
        self.treev.column("2", width=150, anchor="w")
        self.treev.column("3", width=90, anchor="center")
        self.treev.column("4", width=90, anchor="e")
        self.treev.column("5", width=120, anchor="w")

        # Định nghĩa tiêu đề cột
        self.treev.heading("1", text="Mã món ăn")
        self.treev.heading("2", text="Tên món ăn")
        self.treev.heading("3", text="Đơn vị tính")
        self.treev.heading("4", text="Đơn giá")
        self.treev.heading("5", text="Nhóm")

        self.treev.pack(fill="both", expand=True)

        # Load dữ liệu mặc định
        self.update_treeview(get_tt_food())

    def cbb_choice(self, event):
        """Gọi khi chọn giá trị trong Combobox"""
        selected_value = self.loai_thuc_an.get()
        data = cbb_choice(selected_value)  # Gọi từ sql_helper.py
        self.update_treeview(data)

    def update_treeview(self, data):
        """Xóa dữ liệu cũ và cập nhật dữ liệu mới vào Treeview"""
        self.treev.delete(*self.treev.get_children())

        for item in data:
            self.treev.insert("", "end", values=list(item))


