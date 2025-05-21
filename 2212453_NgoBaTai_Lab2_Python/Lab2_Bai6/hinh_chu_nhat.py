from hinh_hoc import HinhHoc

class HinhChuNhat(HinhHoc):
    def __init__(self, dai: float, rong: float):
        super().__init__(dai)
        self.rong = rong
    
    def tinhDienTich(self):
        return super().tinhDienTich() * self.rong
    
    def __str__(self):
        return super().__str__() + f"chữ nhật là: {self.tinhDienTich()}" 