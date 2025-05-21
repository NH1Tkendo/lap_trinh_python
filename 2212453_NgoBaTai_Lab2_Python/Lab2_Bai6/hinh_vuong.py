from hinh_chu_nhat import HinhChuNhat

class HinhVuong(HinhChuNhat):
    def __init__(self, canh: float):
        super().__init__(canh, canh)

    def tinhDienTich(self):
        return super().tinhDienTich()
    
    def __str__(self):
        return f"Diện tích hình vuông là: {self.tinhDienTich()}"