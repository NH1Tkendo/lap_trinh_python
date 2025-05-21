import datetime

class SinhVien:
    truong = "Đại học Đà Lạt"
    def __init__(self, maso: int, hoten: str, ngaysinh: datetime) -> None:
        self.__maso = maso
        self.__hoten = hoten
        self.__ngaysinh = ngaysinh

    @property
    def maso(self):
        return self.__maso

    @property
    def hoten(self):
        return self.__hoten
    
    @property
    def ngaysinh(self):
        return self.__ngaysinh
    
    @maso.setter
    def maso(self, maso):
        if self.lamasohople(maso):
            self.__maso = maso

    @staticmethod
    def lamasohople(maso: int):
        return len(str(maso)) == 7

    @classmethod
    def doitentruong(self, tenmoi):
        self.truong = tenmoi

    def __str__(self) -> str:
        return f"{self.__maso}\t{self.__hoten}\t{self.__ngaysinh}"

    def xuat(self):
        print(f"{self.__maso}\t{self.__hoten}\t{self.__ngaysinh}")
		

class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []

    def themsinhvien(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timsvtheomssv(self, mssv: int):
        return [ sv for sv in self.dssv if sv.maso == mssv]

    def timVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maso == mssv:
                return i
        return -1

    def xoasvtheomssv(self, maso: int) -> bool:
        vt = self.timVTSvTheoMssv(maso)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False

    def timSvTheoTen(self, ten: str) -> 'DanhSachSv':
        ket_qua = DanhSachSv() 
        for sv in self.dssv:
            if ten.lower() in sv.hoten.lower():
                ket_qua.dssv.append(sv)  
        return ket_qua

    def timSvSinhTruocNgay(self, ngay: datetime):
        ket_qua = DanhSachSv() 
        for sv in self.dssv:
            if sv.ngaysinh < ngay:  
                ket_qua.dssv.append(sv)  
        return ket_qua 
    
    def sapxep_hoten(self, kieusapxep: int) -> None:
        match(kieusapxep):
            case 1:
                self.dssv.sort(key=lambda x: x.hoten)
            case 2:
                self.dssv.sort(key=lambda x: x.hoten, reverse=True)    



