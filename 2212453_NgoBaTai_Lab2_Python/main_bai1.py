import datetime
from bai1 import SinhVien, DanhSachSv

noi_dung = DanhSachSv()
def doc_file():
    f = open("Bai1_Lab2.txt", "r")
    for x in f:
        parts = x.split(",") 

        maso = int(parts[0])  
        hoten = parts[1].strip()  
        ngaysinh = datetime.datetime.strptime(parts[2].strip(), "%d/%m/%Y") 

        sv = SinhVien(maso, hoten, ngaysinh)
        noi_dung.themsinhvien(sv)
        
    f.close()

doc_file() #đọc file
# Tìm SV sinh trước ngày
# ngay = datetime.datetime.strptime("17/11/2004", "%d/%m/%Y")
# vt = noi_dung.timSvSinhTruocNgay(ngay)
# vt.xuat()

#Tìm Sv theo tên
#vt = noi_dung.timSvTheoTen("Tai")
# vt.xuat()

#Sắp xếp danh sách sinh viên tăng/giảm theo họ tên
# noi_dung.sapxep_hoten(2)
#noi_dung.xuat()