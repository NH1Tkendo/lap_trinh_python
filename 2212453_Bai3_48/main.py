#Bài tập tìm lỗi sai
#
#Author: Ngô Bá Tài
#Bài tập này bao gồm 48 câu tìm lỗi sai về những lỗi phổ biến hay gặp phải

#1. Identation Error
# if 5 > 2:
#     print("Năm lớn hơn hai!")

#2. Không được dùng dấu "-" trong đặt tên biến, và tên biến không được bắt đầu bằng số
#my_first_name = "John"

#3. Global
# def myfunc():
#     global x
#     x= "fantastic"

#4.<class 'str'>
# x = "Hello World"
# print(type(x))

#5. class 'tuple'
# x = ("apple", "banana", "cherry")
# print(type(x))

#6. float
# x = 5
# x = float(x)

#7. strip
# txt = " Hello World "
# x = txt.strip()

#8.  replace
# txt = "Hello World"
# txt = txt.replace(txt[0],"T")

#9. f-string
# age = 36
# txt = "My name is John, and I am {age}"
# print(txt.format(age))

#10. print boolean: True
# print(bool("abc"))

#11. print boolean: False
# print(10 == 9)

#12. or
# if 5 == 10 or 4 == 4:
#     print("Một trong 2 điều kiện đúng")

#13. 2
#print(10 // 4)

#14. 25
# sum = 0
# for i in range(1,10,2):
#     sum += i
# print(sum)

#15. 0 1 2 3 4 theo chiều dọc
# i= 0
# while i < 5:
#     print(i)
#     i+=1

#16. 10
# sum = 0
# for i in range(5):
#     sum += i
# print(sum)

#17. list indexed
# fruits = ["apple", "banana", "cherry"]
# fruits[0] = "kiwi"

#18. list indexed
# fruits = ["apple", "banana", "cherry"]
# fruits[2] = "lemon"

#19, list indexed
# fruits = ["apple", "banana", "cherry"]
# print(fruits[-1])

#20. lambda
# x = lambda a : a + 10
# print(x(5))

#21. list indexed
# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(fruits[2:5])

#22. kiwi melon mango
# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(fruits[4:])

#23. add
# fruits = {"apple", "banana", "cherry"}
# fruits.add("lemon")
# print(fruits)

#24. discard
# fruits = {"apple", "banana", "cherry"}
# fruits.discard("banana")

#25. dictionary: add key:value
# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# car["color"] = "red"
# print(car)

#26. dictionary: change value
# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# car["year"] = 2020
# print(car)

#27.  break
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         break
#     print(i)

#28. *
# def my_function(*kids):
#     print("The youngest child is " + kids[2])

#29. instance
# class MyClass:
#     x = 5
# p1 = MyClass()

#30. init
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#31. 22
# def myfunc(n):
#     return lambda a : a * n
# mydoubler = myfunc(2)
# print(mydoubler(11))

#32. pop
# list1 = [3, 4, 5, 20, 5, 25, 1, 3]
# list1.pop(1)
# print(list1)

#33. datetime : số giây kể từ thời điểm Epoch (mốc thời gian 0) 
# import time
# a = time.time()
# print(a)

#34. Phương thức
#35. Toán tử nào là quá tải hàm của hàm or() 

#36. 1 3
# i = 0
# while i < 3:
#     print(i)
#     i+= 1
#     print(i+1)

#37. Đảo ngược chuỗi
#print("Dalat university"[::-1])

#38 Một hàm không trả về giá trị nào, giá trị trả về được nhìn thấy khi 
# gọi hàm hoặc khi hàm được thực thi tại shell là gì? -> None

#39. False
#print (0.1 + 0.2 == 0.3)

#40. ~ = -(x+1) = 5
#41. -19
#42. s[1]= a sai
#43. Để chạy python ở chế độ dòng lệnh, sử dụng lệnh python
#44. Class không phải kiểu dữ liệu gốc
#45. L = [1, 23, ‘hello’, 1] -> List
#46. 6
# nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv']
# pos = nameList.index("Bob")
# print (pos * 3)

#47. 
# D = dict()
# for x in enumerate(range(2)):
#     D[x[0]] = x[1]
#     D[x[1]+7] = x[0]
# print(D)

#48. 
# a = {i: i * i for i in range(6)}
# print (a)