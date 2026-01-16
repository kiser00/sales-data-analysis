import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("データを確認したいCSVファイル名を入力してください")
file_pass = input()

#dfに集計したいcsv名をユーザーに指定させる
try:
    df = pd.read_csv(file_pass)
except FileNotFoundError:
    print("エラー: ファイルが見つかりません。")
except Exception as e:
    print(f"予期せぬエラーが発生しました: {e}")
#exit()

columns_list = list(df.columns)
print(columns_list)

columns_list = df.columns
print(columns_list)

print("計算したいカラム名を入力してください")
columns_number_select = input("")
if(columns_number_select in 101):
    print("未入力です！")
#elif(columns_number_select.swapcase() in "id"):　顧客IDをはじけるように実装
 #   print("参照するカラム名を確認してください")
else:
    #print(df[columns_number_select : 1])
    de_sales = columns_number_select
    #カンマをとって売上列を数値に変換して合計を算出
    def convert_sales_to_int(series):
        return (
            series.astype(str)
                .str.replace(",", "", regex=False)
                .astype(int)
        )

    #以下df["売上"]は数値
    df[de_sales] = convert_sales_to_int(df[de_sales])
    #print(df[de_sales])

    total_sales = df[de_sales].sum()

    print(f"月の合計売上：￥{total_sales}")

    #-------------------------------------------
    print("1:日別の売上をグラフで確認する / 2:終了")
    continue_question = int(input())

    if(continue_question == 1):
        print("日付に対応するカラム名を入力してください")
        df_day = input("")
        # 日付を日付型に
        df[df_day] = pd.to_datetime(df[df_day])
        # 日別合計
        daily_sales = df.groupby(df_day)[de_sales].sum()
        daily_sales_df = daily_sales.reset_index()
        print(daily_sales_df)
        #グラフ描画
        plt.plot(daily_sales)
        plt.title('total_sales')
        plt.xlabel(de_sales, size=30)
        plt.ylabel(df_day, size=30)
        plt.grid()
        plt.show()
    elif(continue_question == 2):
        print("終了")
    else:
        print("1か2を選択してください")


#最初に「顧客ID」、でもを入力しても動作してしまう

