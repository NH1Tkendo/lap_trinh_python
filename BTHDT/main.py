from ds_sach import DSSach
from sach_dien_tu import SachDienTu
from sach_giay import SachGiay
from datetime import datetime

a = SachGiay("ABC", "Nguyễn Văn A", datetime.strptime("12/12/2000", "%d/%m/%Y"), 100, 45000, 200)
b = SachGiay("ABCD", "Nguyễn Văn B", datetime.strptime("11/12/2005", "%d/%m/%Y"), 80, 55000, 250)
c = SachGiay("ABCE", "Nguyễn Văn C", datetime.strptime("12/8/2003", "%d/%m/%Y"), 150, 65000, 100)
d = SachDienTu("CBA", "Nguyễn Văn EE", datetime.strptime("2/12/2005", "%d/%m/%Y"), 10, 4000, 3)
e = SachDienTu("CBB", "Nguyễn Văn BB", datetime.strptime("1/5/2008", "%d/%m/%Y"), 100, 40000, 2)

dss = DSSach()
dss.themSach(a)
dss.themSach(b)
dss.themSach(c)
dss.themSach(d)
dss.themSach(e)

dss.xuat()

# print("Sách xuất bản năm 2000: ")
# ket_qua = dss.timSachTheoNamXB(2000)
# ket_qua.xuat()

# print("Sách theo tên tác giả: ")
# ket_qua = dss.timSachTheoTacGia("A")
# ket_qua.xuat()

# print("Tìm sách trên 100 trang: ")
# ket_qua = dss.timSachTheoSoTrang(100)
# ket_qua.xuat()

# print("Sắp xếp theo năm xuất bản: ")
# dss.sapXepTheoNamXB(False)
# dss.xuat()

# print("Sắp xếp theo tên tác giả: ")
# dss.sapXepTheoTenTacGia(False)
# dss.xuat()

# print("Tìm theo giá bán: ")
# ket_qua = dss.timSachTheoGiaBan(3000000, 100000)
# ket_qua.xuat()

# print('Tìm sách giấy có giá bán cao nhất')
# ket_qua = dss.sachGMaxGia()
# ket_qua.xuat()

print('Tìm sách điện tử có dung lượng cao nhất')
ket_qua = dss.sachDTDLMax()
ket_qua.xuat()