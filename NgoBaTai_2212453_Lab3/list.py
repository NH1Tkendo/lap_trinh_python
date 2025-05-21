import math
from collections import Counter
#=============================================================
#Đảo ngược list
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)
#=============================================================
#Concatenate two lists index-wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# list3 = [i + j for i,j in zip(list1, list2)]
# print(list3)
#=============================================================
#Turn every item of a list into its square
# numbers = [1, 2, 3, 4, 5, 6, 7]
# n = [n ** 2 for n in numbers]
# print(n)
#=============================================================
#Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# list3 = [ i + j for i in list1 for j in list2]
# print(list3)

# list3 = []
# for i in list1:
#     for j in list2:
#         list3.append(i+j)

# print(list3)
#=============================================================
#Iterate both lists simultaneously
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# for x,y in zip(list1, list2[::-1]):
#     print(x,y)
#=============================================================
#Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# for i in range(len(list1)):
#     if "" in list1:
#         list1.remove("")
# print(list1)

# list2 = [x for x in list1 if x != ""]
# print(list2)

# res = list(filter(None, list1))
# print(res)
#=============================================================
#Add new item to list after a specified item
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)
#=============================================================
#Extend nested list by adding the sublist
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# # sub list to add
# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
# print(list1)
#=============================================================
#Replace list’s item with new value if found
# list1 = [5, 10, 15, 20, 25, 50, 20]

# i = list1.index(20)

# list1[i] = 200
# print(list1)
#=============================================================
#Remove all occurrences of a specific item from a list.
# list1 = [5, 10, 15, 20, 25, 50, 20]
# list2 = [x for x in list1 if x != 20]
# print(list2)
#=============================================================
#5. Khai báo một List chứa 10 số nguyên và dùng List này cho các câu từ 1-17
a = [1,2,3,4,5,6,6,8,9,11]
#=============================================================
#Xuât tất cả các số lẻ không chia hết cho 5
# a1 = [x for x in a if x % 5 != 0 and x & 1]
# print(a1)
#=============================================================
#Xuất tất cả các số Fibonacci
#a2 = [x for x in a if (5 * x * x + 4) ** 0.5 % 1 == 0 or (5 * x * x - 4) ** 0.5 % 1 == 0]
# print(a2)
#=============================================================
#Tìm số nguyên tố lớn nhất
# def laSoNguyenTo(a):
#     if a < 2:
#         return False
#     elif a in (2,3):
#         return True
#     elif a % 2 == 0 or a % 3 == 0:
#         return False
    
#     for i in range(0, int(a** 0.5)):
#         if 6 * i - 1 == a or 6 * i + 1 == a:
#             return True
#     return False

# a3 = [x for x in a if laSoNguyenTo(x)]
# print(a3)
#-----------------------------------------------------
#Tính trung bình các số lẻ
# def tBCSoLe(a):
#     so_le = [x for x in a if x & 1]
#     return sum(so_le) / len(so_le)
# print(tBCSoLe(a))
#-----------------------------------------------------
#Tìm số Fibonacci bé nhất
#print(min(a2))
#-----------------------------------------------------
#Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng
# def tichSoLeKhongChiaHetCho3(a):
#     so_le = (x for x in a if x & 1 and x % 3 != 0)
#     return math.prod(so_le)

# print(tichSoLeKhongChiaHetCho3(a))
#-----------------------------------------------------
#Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ
# def doiCho(a, x, y):
#     a[x], a[y] = a[y], a[x]

# doiCho(a, 2, 5)
# print(a)
#-----------------------------------------------------
#Đảo ngược trật tự các phần tử của danh sách
#print(a[::-1])
#-----------------------------------------------------
#Xuất tất cả các số lớn thứ nhì của danh sách
# def xuatSoLonThu2(a):
#     e = sorted(a)
#     so_lon_thu_2 = e[-2]
#     return [x for x in e if x == so_lon_thu_2]

# print(xuatSoLonThu2(a))
#-----------------------------------------------------
#Tính tổng các chữ số của tất cả các số trong danh sách
# def tongChuSo(a):
#     return sum(int(c) for x in a for c in str(abs(x)))
# print(tongChuSo(a))
#-----------------------------------------------------
#Đếm số lần xuất hiện của một số trong danh sách
# def demSoLanXuatHien(a, x):
#     return a.count(x)
# print(demSoLanXuatHien(a, 5))
#-----------------------------------------------------
#Xuất các số xuất hiện n lần trong danh sách
# def xuatSoXuatHienNLan(a, b):
#     return [x for x in a if a.count(x) == b]
# print(xuatSoXuatHienNLan(a, 2))
#-----------------------------------------------------
#Xuất các số xuất hiện nhiều lần nhất trong danh sách
# def xuatSoXuatHienNhieuLanNhat(a):
#     max = 0
#     for i in a:
#         if a.count(i) > max:
#             max = a.count(i)
#     return [x for x in a if a.count(x) == max]

#Cach2:
def xuatCach2(a):
    freq = Counter(a)  # Đếm số lần xuất hiện của từng phần tử
    max_freq = max(freq.values())  # Tìm tần suất lớn nhất
    return [x for x in a if freq[x] == max_freq]

# print(xuatSoXuatHienNhieuLanNhat(a))
 
    