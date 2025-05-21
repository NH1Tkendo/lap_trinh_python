from sach import Sach
from datetime import datetime

class SachGiay(Sach):
    def __init__(self, ten_sach: str, ten_tac_gia: str, ngay_xb: datetime, so_trang: int, gia_bia: int, trong_luong: int):
        super().__init__(ten_sach, ten_tac_gia, ngay_xb, so_trang, gia_bia)
        self.trong_luong = trong_luong

    def tinh_gia_ban(self):
        return self.gia_bia * 95 + self.trong_luong * 100
    
    def __str__(self):
        return super().__str__() + f"\t{self.tinh_gia_ban()}"