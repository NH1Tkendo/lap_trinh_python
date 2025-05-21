#Chức năng chính
#
#File này chứa các chức năng chính của chương trình( các bài tập của lab 1 bài 2)
#Author: Ngô Bá Tài

#import
import math
#=======
#Dừng 1 nhịp
def dungmotnhip():
    print("Nhấn một phím để tiếp tục")
    input()
#Hàm nhập giá trị cho câu 1
def nhap_gia_tri():
    a = int(input("Nhập số đầu tiên:"))
    b = int(input("Nhập số thứ hai: "))
    while(True):
        print("Chọn một trong các phép tính dưới đây:")
        print("1. (a+b)")
        print("2. a/b")
        print("3. a**b")
        c = int(input("Chọn:"))
        if(c>=1 and c<= 3):
            break
        else:
            print("Nhập sai, mời nhập lại")
    return a,b,c
#Hàm tính toán cho câu 1
def tinhtoan():
    a,b,c = nhap_gia_tri()
    print("Kết quả của phép tính là: ",end="")
    match c:
        case 1:
            return (a+b)
        case 2:
            return (a/b)
        case 3: 
            return a**b
#Câu 2  
def tinhdientich_hinhtron():
    bankinh = float(input("Nhập bán kính hình tròn: "))
    dientich = math.pi * bankinh**2
    print(f"Diện tích hình tròn là: {dientich:.2f}")
    dungmotnhip()
#Câu 3: Xuất tất cả các số nguyên tố trong một khoảng cho trước
def la_so_nguyento(a:int)->bool:
    if a<2:
        return False
    for i in range(2,a):
        if(a%i==0):
            return False
    return True

def xuatsonguyento():
    diem_bd= int(input("Nhập điểm bắt đầu:"))
    diem_kt= int(input("Nhập điểm kết thúc: "))
    print(f"Dãy số nguyên tố:")
    for i in range(diem_bd,diem_kt):
        if(la_so_nguyento(i)):
            print(i) 
    dungmotnhip()
#Câu 4:
def la_so_chinh_phuong(n)->bool:#Số chính phương là số khi lấy kết quả căn bậc 2 nó mũ 2 lên thì ra chính nó
    result= int(math.sqrt(n))
    return result**2==n

def la_so_fibonacci(n)->bool:
    if n <0:
        return False
    return la_so_chinh_phuong(5*n**2+4) or la_so_chinh_phuong(5*n**2-4)
#Câu 5: Tính fibonacci thứ n (Không đệ quy: dùng công thức binet và đệ quy: F(n-1) + F(n-2))
def fibonacci_n_khongdequy(n):
    a = ((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5))/2)/math.sqrt(5)
    return a

def fibonacci_n_dequy(n):
    return fibonacci_n_dequy(n-1) + fibonacci_n_dequy(n-2)

