#1. Binary search 
#Cách 1: Recursion
a = [1, 6, 4 , 18 ,10, 15]

# def binaryRecursion(a, low, high, tim):
#     if high >= low:
#         mid = (high + low) // 2
#         if a[mid] == tim:
#             return mid
#         elif tim > a[mid]:
#             return binaryRecursion(a, mid + 1, high, tim)
#         else:
#             return binaryRecursion(a, low, mid -1, tim)
#     else:
#         return -1

# result = binaryRecursion(a, 0, len(a)-1, 6)
 
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")
#Cách 2: Interative
# def binaryInterative(a, low, high, tim):
#     mid = (high + low) // 2

#     while mid >= low and mid <= high:
#         if a[mid] == tim:
#             return mid
#         elif a[mid] > tim:
#             mid -= 1
#         else:
#             mid += 1
#     return -1
    
# result = binaryInterative(a, 0, len(a)-1, 6)
 
# if result != -1:
#      print("Element is present at index", str(result))
# else:
#      print("Element is not present in array")

#2. Linear Search
#Cách 1: Cách bình thường
# def linearSearch_normal(a, x):
#     for index in range(len(a)):
#         if a[index] == x:
#             return index
#     else:
#         return -1

# print(linearSearch_normal(a, 1) + 1)

#Cách 2: Recursion
# def linearSearch_recursion(a, x, index = 0):
#     if index == len(a):
#         return -1

#     if a[index] == x:
#         return index

#     return linearSearch_recursion(a, x, index + 1)

# print(linearSearch_recursion(a, 1) + 1)

#3. Insertion sort
#Cách 1:
# def insertionsort_tangdan(a):
#     n = len(a)
#     if n <= 1:
#         return 
    
#     for i in range(1,n):
#         key = a[i]
#         j = i-1

#         while j >= 0 and a[j] > key:
#             a[j + 1] = a[j]
#             j -= 1
#         a[j+1] = key

# def insertionsort_giamdan(a):
#     n = len(a)
#     if n <= 1:
#         return 
    
#     for i in range(1,n):
#         key = a[i]
#         j = i-1

#         while j >= 0 and a[j] < key:
#             a[j + 1] = a[j]
#             j -= 1
#         a[j+1] = key

# insertionsort_tangdan(a)
#insertionsort_giamdan(a)
# print(a)

#4. Quick Sort:
#Cách 1: Recursion quick sort
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         left = [x for x in arr[1:] if x < pivot]
#         right = [x for x in arr[1:] if x >= pivot]
#         return quicksort(left) + [pivot] + quicksort(right)

