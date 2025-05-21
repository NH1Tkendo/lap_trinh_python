from hinh_hoc import HinhHoc
import math

class HinhTron(HinhHoc):
    def __init__(self, banKinh: float):
        super().__init__(banKinh)
    
    def tinhDienTich(self):
        return super().tinhDienTich()**2 * math.pi
    
    def __str__(self):
        return super().__str__() + f"tròn là: {self.tinhDienTich():.2f}"