from Bai2 import PhanSo, DanhSachPhanSo

a = PhanSo(-1,6)
b = PhanSo(4,12)
c = PhanSo(5,12)
# print(f"{a} + {b} = {a+b}")
# print(f"{a} - {b} = {a-b}")
# print(f"{a} * {b} = {a*b}")
# print(f"{a} / {b} = {a/b}")

dsps = DanhSachPhanSo()
dsps.themPhanSo(a)
dsps.themPhanSo(b)
dsps.themPhanSo(c)
dsps.themPhanSo(b)
dsps.themPhanSo(a)

# print(f"Số phân số âm trong danh sách là: {dsps.demPSAm()}")
#print(f"Phân số dương nhỏ nhất trong mảng là: {dsps.timPSDuongMin()}")

# print(f"Các vị trị xuất hiện phân số x là:")
# ket_qua = dsps.timVTPSX(b)
# for i in ket_qua:
#     print(i)

# ket_qua = dsps.tongPSAm()
# print(f"Tổng các phân số ấm trong mảng là: {ket_qua}")

# ket_qua = dsps.timVTPSX(b)
# for i in ket_qua:
#     dsps.xoaPS(i)

# dsps.xuat()

# dsps.sap_xep_tang_giam()