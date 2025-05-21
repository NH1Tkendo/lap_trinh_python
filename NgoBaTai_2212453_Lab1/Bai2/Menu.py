#Menu chương trình
#
#File này chứa giao diện chính của chương trình
#Author: Ngô Bá Tài

import Bai2.chuc_nang as cn

def xuatmenu():
    print("===============Bảng danh sách chức năng=================")
    print("1. Thực hiện các phép toán")
    print("2. Tính diện tích hình tròn khi biết bán kính")
    print("3. Xuất tất cả các số nguyên tố trong 1 khoảng cho trước")
    print("4. Kiểm tra 1 số có phải số fibonacci hay không")
    print("5. Tìm số fibonacci thứ n (đệ quy và không đệ quy)")
    print("0. Thoát chương trình")
    print("========================================================")

def chonmenu(menu):
    xuatmenu()
    while(True):
        chon=int(input(f"Chọn một số từ 0 tới {menu}:"))
        if(chon >=0 and chon <= menu):
            break
    return chon

def xulymenu(menu):
    match menu:
        case 1:
            print(cn.tinhtoan())
        case 2:
            cn.tinhdientich_hinhtron()
        case 3:
            cn.xuatsonguyento()
        case 4:
            x = int(input("Nhập số nguyên: "))
            if(cn.la_so_fibonacci(x)):
                print(f"{x} là số fibonacci")
            else:
                print(f"{x} không là số fibonacci")
            cn.dungmotnhip()
        case 5:
            x = int(input("Nhập số nguyên: "))
            print(cn.fibonacci_n_khongdequy(x))
            cn.dungmotnhip()
        case _:
            print("Thoát chương trình thành công")

    