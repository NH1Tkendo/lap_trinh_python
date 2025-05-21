from hinh_tron import HinhTron
from hinh_chu_nhat import HinhChuNhat
from hinh_vuong import HinhVuong
from ds_hinh_hoc import DanhSachHinhHoc

a = HinhVuong(5)
b = HinhVuong(7)
c = HinhVuong(9)
d = HinhTron(3.5)
e = HinhTron(4.6)
f = HinhTron(5.9)
g = HinhChuNhat(3,4)
h = HinhChuNhat(4,6)
i = HinhChuNhat(7,8)

dshh = DanhSachHinhHoc()
dshh.themHinh(a)
dshh.themHinh(b)
dshh.themHinh(c)
dshh.themHinh(g)
dshh.themHinh(h)
dshh.themHinh(i)
dshh.themHinh(d)
dshh.themHinh(e)
dshh.themHinh(f)

# dshh.xuat()
# print(f"Hình có diện tích lớn nhất là: {dshh.hinhDTLonNhat():.2f}")
# print(f"Hình có diện tích nhỏ nhất là: {dshh.hinhDTNhoNhat():.2f}")
# print(f"Hình tròn nhỏ nhất có diện tích: {dshh.timHTNhoNhat():.2f}")

# loai = input("Nhập loại hình")
# ket_qua = dshh.demSoLuongHinh(loai)
# print(f"Số lượng {loai.lower()} : {ket_qua}")

# tong_dt = dshh.tinhTongDienTich()
# print(f"Tổng diện tích : {tong_dt:.2f}")

# loai = input("Nhập loại hình")
# max = dshh.timHinhCoDTMax(loai)
# print(f"Hình có diện tích lớn nhất là: {max}")

#print(f"Vị trí của hình cần tìm trong danh sách là: {dshh.timVTHinh(f)+1}")

# print(f"Xóa hình tại vị trí {dshh.xoaHinh(4)}")
# dshh.xuat()
# kq = dshh.timHinhTheoDT(24)
# for i in kq:
#     print(i)

# dshh.xoaTheoLoai("Hình vuông")
# dshh.xuat()

# tong = dshh.tongDTTheoLoai("Hình tròn")
# print(tong)

# dshh.sapXepGiamDT()
# dshh.xuat()

ket_qua = dshh.xuatHinhTG("Hình tròn", False)
for i in ket_qua:
    print(i)