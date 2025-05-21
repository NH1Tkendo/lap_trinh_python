#150 bài tập cơ bản python
#
#150 bài tập cơ bản python nhằm giúp người làm hiểu hơn về các câu lệnh trong python
#Author: Ngô Bá Tài

#Import
import sys #Bài tập 2
import datetime #Bài tập 3
import math#Bài tập 4
import calendar#Bài tập 12
from datetime import date#Bài tập 14
#===================================
#Bài tập 1: Formatted Twinkle Poem
#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")
#=================================
#Bài tập 2: Check Python version
#print("Python version " + sys.version)
#print(f"Version info.{sys.version_info}")
#========================================
#Bài tập 3: Current DateTime Display
#date = datetime.datetime.now()
#print(date)
#print(date.strftime("%Y-%m-%d")) #phương thức strftime giúp format thời gian xuất ra
#===================================
#Bài tập 4: Circle Area Calculator (Tính diện tích hình tròn = pi * R^2)
#banKinh = float(input("Nhập bán kính hình tròn: "))
#dienTich = math.pi * banKinh ** 2
#print(f"Diên tích hình tròn có bán kính = {banKinh} là : {dienTich}")#Ngoài ra có thể dùng str(banKinh) nếu muốn nối chuỗi
#======================================================================
#Bài tập 5: Reverse Full Name
#hovatendem = input("Nhập họ và tên đệm: ")
#ten = input("Nhập tên: ")
#print(ten, hovatendem, sep=" ")
#============================
#Bài tập 6: List and Tuple Generator
#value = input("Nhập vào dữ liệu: ")
#list= value.split(",")
#tuple=tuple(list)

#print("List: ",list)
#print("Tuple: ",tuple)
#===================================
#Bài tập 7: File Extension Extractor (Nhập vào một file và in ra phần mở rộng file đó)
#filename = input("Nhập vào tên file: ")
#extension = filename.split(".")
#print("Phần mở rộng của file "+filename+ "là: " + str(extension[-1]))
#=====================================================================================
#Bài tập 8: First and Last Colors
#color_list = ["Red","Green","White" ,"Black"]
#print("Màu đầu tiên trong danh sách là: "+str(color_list[0]))
#print("Màu cuối cùng trong danh sách là: "+str(color_list[-1]))
#================================
#Bài tập 9: Exam Schedule Formatter
#exam_st_date = (11, 12, 2014)
#print("The examination will start from : %i / %i / %i" % exam_st_date)
#=================================
#Bài tập 10: Number Expansion Calculator
#value = int(input())

#n1 = int("%s" % value)
#n2 = int("%s%s" % (value,value))
#n3 = int("%s%s%s" % (value,value,value))

#print(n1+n2+n3) 
#=================================
#Bài tập 11: Function Documentation Printer (Trả về chức năng của phương thức đó)
#print(len.__doc__)#Kết quả: Return the number of items in a container.
#==========================================
#Bài tập 12: Monthly Calendar Display
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))

# print(calendar.month(y, m))
#====================================
#Bài tập 13: Multi-line Here Document
# print("""
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# """)
#====================================
#Bài tập 14: Days Between Dates
# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)

# delta = l_date - f_date

# print(delta.days)
#====================================
#Bài tập 15: Sphere Volume Calculator
# bankinh= float(input("Nhập bán kính: "))
# the_tich_hinhcau= 4/3 * math.pi * bankinh**3
# print("Thể tích hình cầu là: " + str(the_tich_hinhcau))
#====================================
#Bài tập 16: Difference from 17
# def different17(n):
#     if(n>17):
#         return (n-17)*2
#     else:
#         return 17-n

# so = int(input("Nhập 1 số: "))
# print(different17(so))
#====================================
#Bài tập 17: Number Range Tester
# def near_thousand(n):
#     return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
# print(near_thousand(800))
#====================================
#Bài tập 18: Triple Sum Calculator
# def triple_sum_caculator(a,b,c):
#     if(a==b==c):
#         return (a**3)**3
#     else:
#         return a+b+c

# a = int(input("Nhập số đầu tiên: "))
# b = int(input("Nhập số thứ hai: "))
# c = int(input("Nhập số thứ ba: "))

# print(triple_sum_caculator(a,b,c))
#=================================
#Bài tập 19: Prefix "Is" String Modifier
# def add_is(text):
#     if len(text) >= 2 and text[:2]=="Is":
#         return text
#     else:
#         return "Is"+text

# print(add_is("Array"))
#=======================================
#Bài tập 20: String Copy Generator
# def larger_string(text, n=2):
#     result=""
#     for i in range(n):
#         result+=text
#     return result
# print(larger_string("Hello"))
#=================================
#Bài tập 21: Even or Odd Checker
# def check_even_odd(n):
#     if(n & 1):
#         print("This is an odd number")
#     else:
#         print("This is an even number")

# print(check_even_odd(5))
#===============================
#Bài tập 22: Count 4 in List
# def count4_in_list(n):
#     count=0
#     for num in n:
#         if num==4:
#             count+=1
#     return count
# print(count4_in_list([1,2,3,4,5,6,4]))
#===========================
#Bài tập 23: String Prefix Copies
# def string_prefix_copies(text, n):
#     result=""
#     if(len(text)>2):
#         for i in range(n):
#             result+=text[:2]
#     else:
#         for i in n:
#             result+=text
#     return result
# print(string_prefix_copies("abcdefg",3))
#================================
#Bài tập 24: Vowel Tester
# def check_nguyenam(text):
#     all_vowel="euoai"
#     return text in all_vowel
# print(check_nguyenam("a"))
#=========================
#Bài tập 25: Value in Group Tester
# def check_value(n):
#     a=[1,3,4,6]
#     for i in a:
#         if n == i:
#             return True
#     return False
# print(check_value(3))
#===============================
#Bài tập 26: List Histogram
# def histogram(items):
#     for n in items:
#         output = ''
#         count= n
#         while(count>0):
#             output+='*'
#             count-=1
#         print(output)
# histogram([2,3,5,6])
#==========================
#Bài tập 27: List to String Concatenator
# def concat_list(items):
#     output=""
#     for i in items:
#         output+=i
#     return output
# print(concat_list(["c","o","a","c"]))
#=======================================
#Bài tập 28: Even Numbers Until 237
# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]
# def print_even_number(numbers):
#     for i in numbers:
#         if(i == 237):
#             print(i)
#             break
#         elif(i & 1==False):
#             print(i)

# print_even_number(numbers)
#==================================
#Bài tập 29: Unique Colors Finder
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# print(color_list_1.difference(color_list_2))
#================================
#Bài tập 30: Triangle Area Calculator
# def dientich_tamgiac(a,h):
#     return a*h/2
# print(dientich_tamgiac(3,4))

