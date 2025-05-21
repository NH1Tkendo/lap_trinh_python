from hinh_hoc import HinhHoc
from hinh_tron import HinhTron
from hinh_chu_nhat import HinhChuNhat
from hinh_vuong import HinhVuong

class DanhSachHinhHoc:
    def __init__(self):
        self.dshh = []

    def themHinh(self, hh: HinhHoc):
        self.dshh.append(hh)
    
    def xuat(self):
        for hh in self.dshh:
            print(hh)
    
    def hinhDTLonNhat(self):
        max = self.dshh[0].tinhDienTich()
        for i in range(1, len(self.dshh)):
            if(self.dshh[i].tinhDienTich() > max):
                max = self.dshh[i].tinhDienTich()
        return max
    
    def hinhDTNhoNhat(self):
        min = self.dshh[0].tinhDienTich()
        for i in range(1, len(self.dshh)):
            if(self.dshh[i].tinhDienTich() < min):
                min = self.dshh[i].tinhDienTich()
        return min
    
    def phanLoaiHinh(self, loai: str):
        if loai == "Hình tròn":
            return [hh for hh in self.dshh if isinstance(hh, HinhTron)]
        elif loai == "Hình vuông":
            return [hh for hh in self.dshh if isinstance(hh, HinhVuong)]
        return [hh for hh in self.dshh if isinstance(hh, HinhChuNhat)]
    
    def timHTNhoNhat(self):
        hinh_tron = self.phanLoaiHinh("Hình tròn")
        min = hinh_tron[0].tinhDienTich()
        for hh in hinh_tron:
            if(hh.tinhDienTich() < min):
                min = hh.tinhDienTich()
        return min
    
    def demSoLuongHinh(self, loai: str) -> int:
        ket_qua = self.phanLoaiHinh(loai)
        return len(ket_qua)
    
    def tinhTongDienTich(self) -> float:
        ket_qua = 0.0
        for hh in self.dshh:
            ket_qua += hh.tinhDienTich()
        return ket_qua
    
    def timHinhCoDTMax(self, loai: str):
        hinh = self.phanLoaiHinh(loai)
        max = hinh[0].tinhDienTich()
        for hh in hinh:
            if(hh.tinhDienTich() > max):
                max = hh.tinhDienTich()
        return max
    
    def timVTHinh(self, h: HinhHoc):
        for i in range(len(self.dshh)):
            if self.dshh[i] == h:
                return i
        else:
            return -1
        
    def xoaHinh(self, i: int) -> bool:
        if i > 0:
            del self.dshh[i-1]
            return True
        return False
    
    def xoaHinhTheoHinh(self, h: HinhHoc) -> bool:
        vt = self.timVTHinh(h)
        if vt > 0:
            del self.dshh[vt]
            return True
        return False
    
    def timHinhTheoDT(self, dt: float):
        return [hh for hh in self.dshh if hh.tinhDienTich() == dt]
    
    def xoaTheoLoai(self, loai: str):
        loai_hinh = {
            "Hình tròn": HinhTron,
            "Hình vuông": HinhVuong,
            "Hình chữ nhật": HinhChuNhat
        }
    
        if loai in loai_hinh:
            self.dshh = [hinh for hinh in self.dshh if not isinstance(hinh, loai_hinh[loai])]
    
    def tongDTTheoLoai(self, loai: str):
        hinh = self.phanLoaiHinh(loai)
        tong = 0.0
        for i in hinh:
            tong+= i.tinhDienTich()
        return tong
    
    def sapXepGiamDT(self):
        return self.dshh.sort(key= lambda x :x.tinhDienTich(), reverse= True)
    
    def xuatHinhTG(self, kieu: str, giam = bool):
        hinh = self.phanLoaiHinh(kieu)
        return sorted(hinh, key= lambda x: x.tinhDienTich(), reverse= giam)

            


           
