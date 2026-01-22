import pandas as pd
import matplotlib.pyplot as plt

#カラム名を取得して一覧表示
def show_columns(df):
    columns_list = list(df.columns)
    print(f"csvに存在するカラム一覧: {columns_list}")

#売上データを数値に変換
def convert_sales_to_int(df, sales_col):
    return (
        df[sales_col].astype(str)
            .str.replace(",", "", regex=False)
            .astype(int)
        )

#売り上げに対応するカラムの合計を出力
def total_sales_sum(df, sales_col):
    df_sales = sales_col
    df[df_sales] = convert_sales_to_int(df, df_sales)
    total_sales = df[df_sales].sum()
    print(f"月の合計売上：￥{total_sales}")

# 日付を日付型に
def daily_sales(df, date_col, df_sales):
    df[date_col] = pd.to_datetime(df[date_col])
    daily_sales = df.groupby(date_col)[df_sales].sum()
    daily_sales_df = daily_sales.reset_index()
    print(f"{daily_sales_df}")
    return daily_sales_df

def plot_daily_sales(df, date_col, sales_col):
    daily_df = daily_sales(df, date_col, sales_col)
    plt.plot(daily_df[date_col], daily_df[sales_col])
    plt.title('total_sales')
    plt.xlabel('date_col', size=30)
    plt.ylabel('df_sales', size=30)
    plt.grid()
    plt.show()
#やること変数名の修正
#seriesかdfか把握しながら
