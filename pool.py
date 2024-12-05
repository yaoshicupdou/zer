import baostock as bs
import pandas as pd
from datetime import date

def a():
    # 登录
    lg = bs.login()

    # 获取今日日期
    today = date.today()

    if lg.error_code != '0':
        print(f"登录失败，错误信息：{lg.error_msg}")
        exit()

    # 获取所有 A 股股票列表
    rs = bs.query_all_stock(day=today)
    if rs.error_code != '0':
        print(f"获取股票列表失败，错误信息：{rs.error_msg}")
        bs.logout()
        exit()

    # 将股票数据存入 DataFrame
    stock_list = []
    while rs.next():
        stock_list.append(rs.get_row_data())

    columns = rs.fields
    df = pd.DataFrame(stock_list, columns=columns)

    # 过滤 A 股股票（股票代码以 sh.6 或 sz.0 开头）
    df = df[(df['code'].str.startswith('sh.6')) | (df['code'].str.startswith('sz.0'))]

    df = df[~df['code_name'].str.contains(r'ST|\*ST', case=False, regex=True)]

    df = df[df['tradeStatus'] != 0]

    return df
    
