import pandas as pd
df = pd.read_csv("D:\\Code\\Python\\2212453_NgoBaTai_Lab6\\Automobile_data.csv")
# ----------------Thanh lọc dữ liệu---------------------------
df.dropna(inplace=True)#Xóa 3 hàng có cột price để trống
df = df.drop_duplicates()
# ------------------------------------------------------------
# ------------------------In thông tin------------------------
# print(df)
# print(df.head(6))
# print(df.tail(6))
# print(df.loc[0])
# print(df.info())
# ------------------------------------------------------------
# ---------------Tìm hãng xe có ô tô mắc nhất-----------------
# df = df[['company', 'price']][df.price == df['price'].max()]
# print(df)
# ------------------------------------------------------------
# Xuất ra thông tin chi tiết của tất cả các xe thuộc hãng Toyota
# car_Manufacturers = df.groupby('company')
# toyotaDf = car_Manufacturers.get_group("toyota")
# print(toyotaDf)
# --------------------------------------------------------------
# -------------------Đếm số xe của từng hãng--------------------
# count = df['company'].value_counts()
# print(count)
# --------------------------------------------------------------
# --------Hãy hiển thị giá xe cao nhất của mỗi hãng xe----------
# max_prices = df.groupby('company')['price'].max().reset_index()
# print(max_prices)
# --------------------------------------------------------------
# ----------Hiển thị giá xe trung bình của mỗi hãng xe----------
# mean_price = df.groupby('company')['price'].mean().reset_index()
# print(mean_price)
# --------------------------------------------------------------
