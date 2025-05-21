from sach import Sach
import datetime


class SachDienTu(Sach):
    def __init__(
        self,
        ten_sach: str,
        ten_tac_gia: str,
        ngay_xb: datetime,
        so_trang: int,
        gia_bia: int,
        dung_luong: int,
    ) -> None:
        super().__init__(ten_sach, ten_tac_gia, ngay_xb, so_trang, gia_bia)
        self.dung_luong = dung_luong

    def tinh_gia_ban(self):
        phu_thu = 10000 if self.dung_luong > 10 else 0
        return super().tinh_gia_ban() * 75 / 100 + phu_thu

    def __str__(self):
        return super().__str__() + f" {self.tinh_gia_ban()}"
