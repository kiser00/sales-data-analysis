import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open("Book1.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()
    #print("ファイルの行数:", len(lines))
    #for i, line in enumerate(lines[:12], 1):
        #print(f"{i}: {line.strip()}")

#dfにcsvを取り込んで使用する列を指定
df = pd.read_csv("Book1.csv")
df = df[["売上", "日付"]]

#カンマをとって売上列を数値に変換して合計を算出
def convert_sales_to_int(series):
    return (
        series
        .str.replace(",", "", regex=False)
        .astype(int)
    )

#以下df["売上"]は数値
df["売上"] = convert_sales_to_int(df["売上"])

total_sales = df["売上"].sum()

print(f"月の合計売上：￥{total_sales}")

# 日付を日付型に
df["日付"] = pd.to_datetime(df["日付"])

# 日別合計
daily_sales = df.groupby("日付")["売上"].sum()

daily_sales_df = daily_sales.reset_index()
print(daily_sales_df)

#グラフ描画
plt.plot(daily_sales)
plt.grid()
plt.show()


