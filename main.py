import pandas as pd
import numpy as np
import function

print("データを確認したいCSVファイルパスを貼り付けてください")
file_pass = input() #自動でディレクトリ内のcsvファイルを参照したい

try:
    df = pd.read_csv(file_pass)
except FileNotFoundError:
    print("エラー: ファイルが見つかりません。")
    exit()
except Exception as e:
    print(f"予期せぬエラーが発生しました: {e}")
    exit()

function.show_columns(df)

print("計算したいカラム名を入力してください")
sales_col = input("") #Series
if(sales_col == ""):
    print("未入力です！")
elif(sales_col == "顧客ID"):
    print("参照するカラム名を確認してください")
else:
    function.convert_sales_to_int(df, sales_col)

    function.total_sales_sum(df, sales_col)
    print("-------------------------------------")

    print("日付に対応するカラム名を入力してください")
    date_col = input("")
    if date_col not in df.columns:
        print("存在しないカラム名です")
        exit()

    function.daily_sales(df, date_col, sales_col)
    print(df[[date_col, sales_col]].head())
    print(type(df[[date_col, sales_col]]))
    #-------------------------------------------
    print("1:日別の売上をグラフで確認する / 2:終了")
    try:
        continue_question = int(input())
    except ValueError:
        print("数値を入力してください")
        exit()


    if(continue_question == 1):
        function.plot_daily_sales(df, date_col, sales_col)
    elif(continue_question == 2):
        print("終了")
    else:
        print("1か2を選択してください")

df[date_col] = pd.to_datetime(df[date_col])
df = df.set_index(date_col)

weekly_avg = df[sales_col].resample("W").mean()
weekly_total_sales = df[sales_col].resample("W").sum()

total_sales_avg = weekly_avg.mean()
vols = weekly_avg.pct_change() * 100

print(f"今月の週平均売上: ￥{int(total_sales_avg)}")

for i, date in enumerate(weekly_avg.index, 1):
    total = weekly_total_sales.loc[date]
    v = vols.loc[date]

    if pd.isna(v):
        print(f"週{i} 売上合計: ￥{int(total)}（変動率: 比較不可）")
    else:
        print(f"週{i} 売上合計: ￥{int(total)}（変動率: {v:.2f}%）")
