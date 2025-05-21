#Bài tập về list
#
#Author: Ngô Bá Tài
#Bài tập về cấu trúc dữ liệu list

#1. Python Program for Reversal algorithm for array rotation & Python Program to Split the array and add the first part to the end
# a = [1, 2, 3, 4, 5, 6]
# d = 3
# def reversal(d):
#     return a[d-1:] + a[:d]
# print(reversal(d))

#2. Python Program for Find remainder of array multiplication divided by n
# a = [1, 2, 3, 4, 5, 6]
# d = 7
# def remain(d):
#     mul = 1
#     for i in a:
#         mul *= i
#     return mul%d
# print(remain(d))

#3. Python Program to check if given array is Monotonic
# a = [1, 2, 3, 4, 5, 6]

# def monotocnic() -> bool:
#     x, y = [], []
#     x.extend(a)
#     y.extend(a)
#     x.sort()
#     y.sort(reverse=True)
#     if(x == a or y == a):
#         return True
#     return False

#Tim giá trị lớn nhất hoặc nhỏ nhất thì dùng max, min và loop
#Để đảo ngược danh sách hiệu quả thì dùng reverse