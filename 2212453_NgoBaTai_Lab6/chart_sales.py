import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("D:\\Code\\Python\\2212453_NgoBaTai_Lab6\\sales_data.csv")
print(df)

profitList = df['total_profit'].tolist()
monthList = df['month_number'].tolist()

arr = np.array(
    [
        df["facecream"],
        df["facewash"],
        df["toothpaste"],
        df["bathingsoap"],
        df["shampoo"],
        df["moisturizer"]
    ]
)

dd = df.drop(columns=['month_number', 'total_units', 'total_profit'])
columnList = dd.columns

sum_eachamount = dd.sum()

df = df[df.month_number == 3][columnList]

total_mathang_sale = df.sum()
# -----------------------Câu 1-------------------------------
# plt.figure("Biểu đồ đoạn thẳng")
# plt.plot(monthList, profitList)
# plt.xlabel('Tháng')
# plt.ylabel("Lợi nhuận ($)")
# plt.xticks(monthList)
# plt.title('Lợi nhuận hàng tháng năm 2021')
# plt.yticks([100000, 200000, 300000, 400000, 500000])
# plt.show()
# -----------------------------------------------------------
# -----------------------Câu 2-------------------------------
# plt.figure("Biểu đồ đoạn thẳng")
# plt.plot(monthList, profitList, "o--g")
# plt.xlabel("Tháng")
# plt.ylabel("Lợi nhuận ($)")
# plt.xticks(monthList)
# plt.title("Lợi nhuận hàng tháng năm 2021")
# plt.yticks([100000, 200000, 300000, 400000, 500000])
# plt.show()
# -----------------------------------------------------------
# -----------------------Câu 3-------------------------------
# plt.figure("Số lượng bán của từng sản phẩm")
# plt.plot(monthList, arr[0], "o-b")
# plt.plot(monthList, arr[1], "o-m")
# plt.plot(monthList, arr[2], "o-g")
# plt.plot(monthList, arr[3], "o-r")
# plt.plot(monthList, arr[4], "o-c")
# plt.plot(monthList, arr[5], "o-k")
# plt.xlabel("Tháng")
# plt.ylabel("Số lượng bán")
# plt.xticks(monthList)
# plt.title("Lợi nhuận hàng tháng năm 2021")
# plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
# plt.show()
# -----------------------------------------------------------
# -----------------------Câu 4-------------------------------
# plt.figure("Biểu đồ tán xạ")
# plt.scatter(monthList, arr[1])
# plt.scatter(monthList, arr[0])
# plt.xlabel("Tháng")
# plt.ylabel("Số lượng bán")
# plt.xticks(monthList)
# plt.title("Số lượng bán của sữa rữa mặt và kem dưỡng da mặt theo tháng")
# plt.yticks([1000,2000, 3000, 4000, 5000, 6000])
# plt.grid()
# plt.show()
# -----------------------------------------------------------
# -----------------------Câu 5-------------------------------
# plt.figure("Biểu đồ cột")
# plt.bar(monthList, arr[3])
# plt.xlabel("Tháng")
# plt.ylabel("Số lượng bán")
# plt.xticks(monthList)
# plt.title("Số lượng bán xà bông tắm theo tháng")
# plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 14000])
# plt.grid()
# plt.show()
# -----------------------------------------------------------
# -----------------------Câu 6-------------------------------
# plt.figure("Biểu đồ cột")
# bar_width = 0.4

# plt.bar(monthList, arr[0])
# plt.bar(monthList, arr[1])
# plt.xlabel("Tháng")
# plt.ylabel("Số lượng bán")
# plt.xticks(monthList)
# plt.title("So sánh số lượng bán của sữa rửa mặt và kem dưỡng da mặt theo tháng")
# plt.yticks([1000, 2000, 3000, 4000, 5000, 6000])
# plt.grid()
# plt.show()
# -----------------------------------------------------------
# -----------------------Câu 7-------------------------------
# plt.figure("Biểu đồ tròn")
# plt.title("Thống kê mặt hàng đã bán năm 2021")

# plt.pie(sum_eachamount, autopct="%1.1f%%", labels= columnList)

# plt.show()
# -----------------------------------------------------------
# -----------------------Câu 8-------------------------------
# plt.figure("Biểu đồ tròn")
# plt.title("Thống kê mặt hàng đã bán trong tháng 3 năm 2021")

# plt.pie(total_mathang_sale, autopct="%1.1f%%", labels=columnList)

# plt.show()
# -----------------------------------------------------------
# -----------------------Câu 9-------------------------------
# plt.figure("Số lượng bán của từng sản phẩm")

# plt.subplot(2, 1, 1)
# plt.plot(monthList, arr[3], "o-b")
# plt.title("Số lượng xà bông tắm đã bán")
# plt.gca().set_xticklabels([])
# plt.yticks([6000, 8000, 10000, 12000, 14000])

# plt.subplot(2, 1, 2)
# plt.plot(monthList, arr[1], "o-m")
# plt.xlabel("Tháng")
# plt.ylabel("Số lượng")
# plt.xticks(monthList)
# plt.title("Số lượng sữa rữa mặt đã bán")
# plt.yticks([3000, 4000, 5000, 6000])
# plt.show()
# -----------------------------------------------------------
