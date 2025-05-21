from danh_sach import DanhSach
from sach_giay import SachGiay
from sach_dien_tu import SachDienTu
from datetime import datetime

sach_giay_1 = SachGiay("a", "A", datetime.strptime("12/12/2022","%d/%m/%Y"),23, 25000, 10)
sach_giay_2 = SachGiay("b", "B", datetime.strptime("22/12/2023","%d/%m/%Y"),35, 35000, 100)
sach_giay_3 = SachGiay("c", "C", datetime.strptime("12/11/2022","%d/%m/%Y"),67, 15000, 50)
sach_dien_tu_1 = SachDienTu("d", "D", datetime.strptime("12/11/2023","%d/%m/%Y"),67, 15000, 50)
sach_dien_tu_2 = SachDienTu("e", "D", datetime.strptime("12/11/2022","%d/%m/%Y"),67, 15000, 5)

ds = DanhSach()

ds.them(sach_giay_1)
ds.them(sach_giay_2)
ds.them(sach_giay_3)
ds.them(sach_dien_tu_1)
ds.them(sach_dien_tu_2)

kq = ds.TimSachTheoGiaBan(5000, 12000)
kq.xuat()
