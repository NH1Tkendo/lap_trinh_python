from sach import Sach
import datetime

class SachGiay(Sach):
    def __init__(self, ten_sach: str,  ten_tac_gia: str, ngay_xb:datetime, so_trang: int, gia_bia: int, trong_luong: int) -> None:
        super().__init__(ten_sach, ten_tac_gia, ngay_xb, so_trang, gia_bia)
        self.trong_luong = trong_luong

    def tinh_gia_ban(self):
        return super().tinh_gia_ban() * 95 / 100 + self.trong_luong * 100
    
    def __str__(self):
        return super().__str__() + f" {self.tinh_gia_ban()}"
