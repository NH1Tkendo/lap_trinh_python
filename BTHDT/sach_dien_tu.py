from sach import Sach
from datetime import datetime

class SachDienTu(Sach):
    def __init__(self, ten_sach: str, ten_tac_gia: str, ngay_xb: datetime, so_trang: int, gia_bia: int, dung_luong: int):
        super().__init__(ten_sach, ten_tac_gia, ngay_xb, so_trang, gia_bia)
        self.dung_luong = dung_luong

    def tinh_gia_ban(self):
        phu_thu = 0
        if(self.dung_luong > 10):
            phu_thu = 10000
        return self.gia_bia * 75 + phu_thu
    
     
    def __str__(self):
        return super().__str__() + f"\t{self.tinh_gia_ban()}"