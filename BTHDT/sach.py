from datetime import datetime

class Sach:
    def __init__(self, ten_sach: str, ten_tac_gia: str, ngay_xb: datetime, so_trang: int, gia_bia: int):
        self.ten_sach = ten_sach
        self.ten_tac_gia = ten_tac_gia
        self.ngay_xb = ngay_xb
        self.so_trang = so_trang
        self.gia_bia = gia_bia
    
    def __str__(self):
        return f"{self.ten_sach}\t{self.ten_tac_gia}\t{self.ngay_xb}\t{self.gia_bia}"
    

