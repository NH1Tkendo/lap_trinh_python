from sach import Sach
class DanhSach():
    def __init__(self):
        self.ds = []

    def xuat(self):
        for i in self.ds:
            print(i)

    def them(self, sach: Sach):
        self.ds.append(sach)

    def timSachTheoNamXb(self, nam_xb: int) -> 'DanhSach':
        dskq = DanhSach()
        for i in self.ds:
            if i.ngay_xb.year == nam_xb:
                dskq.them(i)
        return dskq

    def timSachTheoTacGia(self, ten_tg: str) -> "DanhSach":
        dskq = DanhSach()
        for i in self.ds:
            if i.ten_tac_gia == ten_tg:
                dskq.them(i)
        return dskq
    
    def timSachTheoSoTrang(self, trang: int) -> "DanhSach":
        dskq = DanhSach()
        for i in self.ds:
            if i.so_trang >= trang:
                dskq.them(i)
        return dskq
    
    def SapXepTheoTenTG(self):
        self.ds.sort(key = lambda x: x.ten_tac_gia, reverse= True)
        
    def SapxepTheoNamXB(self):
        self.ds.sort(key = lambda x: x.ngay_xb.year)

    def TimSachTheoGiaBan(self, gia_min: float, gia_max: float) -> 'DanhSach':
        dskq = DanhSach()
        for i in self.ds:
            if gia_min <= i.tinh_gia_ban() <= gia_max:
                dskq.them(i)
        return dskq
        