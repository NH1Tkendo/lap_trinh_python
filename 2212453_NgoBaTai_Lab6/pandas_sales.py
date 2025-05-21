import pandas as pd

df = pd.read_csv("D:\\Code\\Python\\2212453_NgoBaTai_Lab6\\sales_data.csv")
# --------------------Hiển thị thông tin của dữ liệu----------------------
# print(df.info())
# Dữ liệu có 9 cột và không có cột nào chứa giá trị null
#  0   month_number  12 non-null     int64
#  1   facecream     12 non-null     int64
#  2   facewash      12 non-null     int64
#  3   toothpaste    12 non-null     int64
#  4   bathingsoap   12 non-null     int64
#  5   shampoo       12 non-null     int64
#  6   moisturizer   12 non-null     int64
#  7   total_units   12 non-null     int64
#  8   total_profit  12 non-null     int64
# ------------------------------------------------------------------------
# -------------------Hiển thị nội dung toàn bộ dữ liệu--------------------
print(df)
# ------------------------------------------------------------------------
# ----------Xuất hàng dữ liệu của tháng có lợi nhuận cao nhất ------------
# max_profit = df[df.total_profit == df['total_profit'].max()]
# print(max_profit)
# ------------------------------------------------------------------------
# ---------Xuất hàng dữ liệu của tháng bán nhiều mặt hàng nhất -----------
# max_profit = df[df.total_units == df['total_units'].max()]
# print(max_profit)
# ------------------------------------------------------------------------
# --------Xuất hàng dữ liệu của tháng bán nhiều kem đánh răng nhất--------
# max_profit = df[df.toothpaste == df['toothpaste'].max()]
# print(max_profit)
# ------------------------------------------------------------------------
# ------------------Cho biết tổng lợi nhuận của cả năm--------------------
# sum_profit = df['total_profit'].sum()
# print(f"Tổng lợi nhuận của cả năm là : {sum_profit}")
# ------------------------------------------------------------------------
# -------------Cho biết tổng số lượng đã bán theo mặt hàng----------------
# df = df.drop(columns=['month_number','total_units','total_profit'], errors="ignore")
# print(df.sum())
# ------------------------------------------------------------------------
# --------Hiển thị số lượng các mặt hàng bán trong tháng 2 ---------------
# df = df[df.month_number == 2]['total_units']
# print(df)
# ------------------------------------------------------------------------
# --------------Số lượng mặt hàng bán chạy nhất tháng 2-------------------
# df = df[df["month_number"] == 2]
# df = df.drop(columns=['total_units','total_profit'], errors="ignore")
# total_mathang_sale = df.sum()
# hot_mathang = total_mathang_sale.idxmax()
# hot_soluong = total_mathang_sale.max()
# print(f"Mặt hàng bán chạy nhất tháng 2: {hot_mathang} với {hot_soluong} sản phẩm")
# ------------------------------------------------------------------------
# ----------------Tìm mặt hàng bán chạy nhất trong năm--------------------
# df = df.drop(columns=['total_units','total_profit'], errors="ignore")
# total_mathang_sale = df.sum()
# hot_mathang = total_mathang_sale.idxmax()
# print(f"Mặt hàng bán chạy nhất năm: {hot_mathang}")
# ------------------------------------------------------------------------
