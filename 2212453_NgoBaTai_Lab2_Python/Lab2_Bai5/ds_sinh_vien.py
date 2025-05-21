from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from sinh_vien import SinhVien
from datetime import datetime

class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []

    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)
    
    def xuat(self):
        for sv in self.dssv:
            print(sv)
    
    def timSVTheoMs(self, ms: str):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == ms:
                return i
        else:
            return -1
    
    def timSVTheoLoai(self, loai: str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ)]
    
    def timSVCoDiemRL_Tren80(self):
        sv_chinhquy = self.timSVTheoLoai("chinhquy")
        return [sv for sv in sv_chinhquy if sv.diemRL >= 80]
    
    def timSVTheoNgay(self):
        sv_phichinhquy = self.timSVTheoLoai("")
        return [sv for sv in sv_phichinhquy if sv.ngaySinh < datetime.strptime("15/8/1999","%d/%m/%Y") and sv.trinhdo == "Cao đẳng"]