import sys
#=============================================================
#Reverse the tuple
# tuple1 = (10, 20, 30, 40, 50)
# print(tuple1[::-1])
#=============================================================
#Access value 20 from the tuple
# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# print(tuple1[1][1])
#=============================================================
#Create a tuple with single item 50
# tuple1 = (50,)
#=============================================================
#Unpack the tuple into 4 variables
# tuple1 = (10, 20, 30, 40)
# a,b,c,d = tuple1
# print(a,b,c,d)
#=============================================================
#Swap two tuples in Python
# tuple1 = (11, 22)
# tuple2 = (99, 88)
# tuple1, tuple2 = tuple2, tuple1
# print(tuple2)
# print(tuple1)
#=============================================================
#Copy specific elements from one tuple to a new tuple
# tuple1 = (11, 22, 33, 44, 55, 66)
# tuple2 = tuple(tuple1[3:5])
# print(tuple2)
#=============================================================
#Modify the tuple
# tuple1 = (11, [22, 33], 44, 55)
# tuple1[1][0] = 222
# print(tuple1)
#=============================================================
#Sort a tuple of tuples by 2nd item 
# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# tuple1 = tuple(sorted(list(tuple1), key = lambda x: x[1]))
# print(tuple1)
#=============================================================
#Counts the number of occurrences of item 50 from a tuple
# tuple1 = (50, 10, 60, 70, 50)
# print(tuple1.count(50))
#=============================================================
#Check if all items in the tuple are the same
# def check(t):
#     return all(i == t[0] for i in t)
# tuple1 = (45, 45, 45, 45)
# print(check(tuple1))
#=============================================================
#1. Print unique rows in a given boolean matrix using Set with tuples
# mat = [[0, 1, 0, 0, 1],
#              [1, 0, 1, 1, 0],
#              [0, 1, 0, 0, 1],
#              [1, 1, 1, 0, 0]]
# mat = map(tuple, mat)
# result = set(mat)
# for r in result:
#     print(r)
#=============================================================
#2. Sử dụng module sys để tính kích cỡ của tuple: (byte)
# tuple = (1, 2, 3, 4, 5, 6)
# print(sys.getsizeof(tuple))
#=============================================================
#3. Maximum and Minimum K elements in Tuple
# tuples = (1, 22, 10, 2, 3, 6, 7)
# k = 2

# def timso(k):
#     ds = sorted(tuples)
#     ket_qua = []
#     for index, value in enumerate(ds):
#         if index < k or len(ds) - k <= index:
#             ket_qua.append(value)
#     return tuple(ket_qua)

# print(timso(k))
#=============================================================
#4. Python program to create a list of tuples from given list having number and its cube in each tuple
#aa = [1, 2, 3, 4, 5]

#def tuple_lapphuong():
#   return [(a, a**3) for a in aa]
    #return list(map(lambda n: (n,n**3), aa))

# print(tuple_lapphuong())
#=============================================================
#5.  Adding Tuple to List
#Cách 1: Using += operator [list + tuple] 
# tup = (1,2)
# li = [-1, 0]
# li += tup
# print(li)
#=============================================================