from sach import Sach
from datetime import datetime
from sach_giay import SachGiay
from sach_dien_tu import SachDienTu

class DSSach:
    def __init__(self):
        self.dss = []
    
    def xuat(self):
        for s in self.dss:
            print(s)

    def themSach(self, a: Sach):
        self.dss.append(a)

    def timSachTheoTacGia(self, ten_tg: str) -> 'DSSach':
        ket_qua = DSSach()
        for s in self.dss:
            if ten_tg in s.ten_tac_gia:
                ket_qua.themSach(s)
        return ket_qua
    
    def timSachTheoNamXB(self, nam_xb: int) -> 'DSSach':
        ket_qua = DSSach()
        for s in self.dss:
            if s.ngay_xb.year == nam_xb:
                ket_qua.themSach(s)
        return ket_qua
    
    def timSachTheoSoTrang(self, so_trang: int) -> 'DSSach':
        ket_qua = DSSach()
        for s in self.dss:
            if s.so_trang > 100:
                ket_qua.themSach(s)
        return ket_qua
    
    def sapXepTheoTenTacGia(self, giam: bool):
        self.dss.sort(key = lambda x: x.ten_tac_gia, reverse = giam)
    
    def sapXepTheoNamXB(self, giam: bool):
        self.dss.sort(key = lambda x: x.ngay_xb.year, reverse = giam)
    
    def timSachTheoGiaBan(self, gia_max: float, gia_min: float) -> 'DSSach':
        ket_qua = DSSach()
        for s in self.dss:
            if s.tinh_gia_ban() > gia_min and s.tinh_gia_ban() < gia_max:
                ket_qua.themSach(s)
        return ket_qua

    def sachGMaxGia(self) -> 'DSSach':
        sach_giay_list = [s for s in self.dss if isinstance(s, SachGiay)]
        gia_ban =  max(sach_giay_list, key=lambda x: x.tinh_gia_ban()).tinh_gia_ban()
        ket_qua = DSSach()
        for s in self.dss:
            if isinstance(s, SachGiay) and s.tinh_gia_ban() == gia_ban:
                ket_qua.themSach(s)
        return ket_qua
    
    def sachDTDLMax(self) -> 'DSSach':
        sach_dt = [s for s in self.dss if isinstance(s, SachDienTu)]
        dl =  max(sach_dt, key=lambda x: x.dung_luong).dung_luong
        ket_qua = DSSach()
        for s in self.dss:
            if isinstance(s, SachDienTu) and s.dung_luong == dl:
                ket_qua.themSach(s)
        return ket_qua

    
