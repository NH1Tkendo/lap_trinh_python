import numpy as np
# ----------------------------Filter------------------------------------
# filter bằng 1 list thuộc kiểu boolean

# arr = np.array([41, 42, 43, 44])
# x = [True, False, True, False]
# newarr = arr[x]
# print(newarr)

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# # Create an empty list
# filter_arr = []

# # go through each element in arr
# for element in arr:
#     # if the element is completely divisble by 2, set the value to True, otherwise False
#     if element % 2 == 0:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)
# ----------------------------------------------------------------------
# ---------------------Sắp xếp 1 mảng----------------------------------
# sort(): trả về 1 mảng mới
# arr = np.array(["banana", "cherry", "apple"])
# print(np.sort(arr))
# Nếu sắp xếp mảng 2 chiều thì cả 2 mảng con đều được sắp xếp
# arr = np.array([[3, 2, 4], [5, 0, 1]])
# print(np.sort(arr))
# ----------------------Tìm kiếm trong mảng---------------------------
# where(): kết quả trả về là 1 tuple

# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 4)
# print(x)

# search_sorted(): Trả về vị trí mà tham số nên được chèn vào để duy trì thứ tự
# Có thể truyền vào 1 mảng giá trị cần chèn: kết quả trả về là 1 mảng index
# x = np.searchsorted(arr, 7)
# print(x)
# ----------------------Hợp 2 mảng numpy------------------------------
# Dùng concatenate() hoắc stack() để hợp nhất 2 mảng
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# arr = np.concatenate((arr1, arr2))
# arr = np.concatenate((arr1, arr2), axis=1)

# arr = np.stack((arr1, arr2), axis=1)
# print(arr)

# hstack(): stack theo dòng
# vstack(): stack theo cột
# dstack():
# --------------------------------------------------------------------
# ----------------------Tách mảng--------------------------------------
# array_split(): nhận 2 tham số lần lượt là mảng cha và số lượng mảng con muốn tạo
# Lưu ý: Nếu không đủ phần tử để chia thì numpy sẽ tự động điều chỉnh

# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
# newarr = np.array_split(arr, 3)

# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 4)
# print(newarr)

# hsplit(): tách chuỗi theo hàng
# Tương tự với vsplit() and dsplit()
# ---------------------------------------------------------------------
# ----------------Duyệt qua các phần tử trong mảng-------------------
# Khi duyệt mảng trong numpy, các phần tử được xuất ra trong mảng sẽ là chiều -1
# arr = np.array([1, 2, 3])
# for x in arr:
#     print(x)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#     print(x)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# for x in arr:
#     for y in x:
#         print(y)

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#     print(x)

# nditer(): duyệt qua chiều thứ 1 của các phần tử trong mảng
# Tham số op_dtypes: Thay đổi kiểu dữ liệu của phần tử, VD op_dtypes = 'S'
# Tham số flags=['buffered]: Tạo chỗ để chuyển đổi dữ liệu
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for x in np.nditer(arr):
#     print(x)

# for x in np.nditer(arr, flags=["buffered"], op_dtypes=["S"]):
#     print(x)

# for x in np.nditer(arr[:, ::2]):
#     print(x)

# ndenumerate(): Trả về giá trị và chỉ mục của 1 phần tử
# for idx, x in np.ndenumerate(arr):
#     print(idx, x)
# -------------------------------------------------------------------
# --------------------------Reshape array --------------------------
# Reshape array là thay đổi shape của 1 array
# Có thể reshape thành bất cứu chiều nào nếu có đủ phần tử
# Lưu ý: reshape trả về 1 view, có thể truyền -1 để numpy tự tính toán phần tử (chỉ dùng được 1 lần)
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3)
# print(newarr)
# Phân rã mảng: truyền tham số duy nhất là -1 để phân rã mảng
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# newarr = arr.reshape(-1)
# print(newarr)
# ------------------------------------------------------------------
# ---------------------------Array shape-----------------------------
# Shape của 1 mảng là số phần tử trong mỗi chiều
# arr.shape trả về 1 tuple chứa số phần tử tương ứng trong mỗi chiều
# arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]]])
# print(arr.shape)
# -------------------------------------------------------------------
# ---------------------- Copy và view ------------------------------
# Copy: Tạo thành 1 mảng mới hoàn toàn
# View: Tham chiếu tới cùng 1 mảng trong bộ nhớ
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42
# print(arr)
# print(x)

# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42
# print(arr)
# print(x)

# print(x.base)
# print(y.base)
# ------------------------------------------------------------------
# ------------------- Chuyển đổi dữ liệu --------------------------
# arr = np.array([1.1, 2.1, 3.1])
# print(arr.dtype)
# newarr = arr.astype(int)
# print(newarr)
# print(newarr.dtype)
# ----------------Xử lý trên mảng bình thường----------------------
# arr = np.array([1, "ss", 3, 4, 5, 6, 7])
# print(arr)
# print(arr[1, 1, 0])#Truy cap index y chang nhu list
# print(arr.ndim)# in ra so dimension cua arr
# ---------------------In kiểu dữ liệu-----------------------------
# print(type(arr))
# print(arr.dtype)
# -----------------------------------------------------------------
# print(arr[-3:-1]) #Cat chuoi y chang binh thuong
# ----------------Cắt mảng đa chiều--------------------------------
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# Tham số đầu tiên là index để truy cập, tham số thứ 2 là giá trị cần lấy
# print(arr[1, 1:4]) #Đối với mảng 2 chiều thì truy cập vào phần tử trước rồi cắt
# print(arr[0:2, 2])
# -----------------------------------------------------------------