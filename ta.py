# 量化分析回测常用方法库，只封装基本方法，不封其他量化库的api，防止过度封装
import pandas as pd
import pandas_ta as ta
import plotly.graph_objects as go

# 呼叫技术支持，测试导入
def zer():
    print('------------------------技术支持微信zer888666------------------------')

# 转换为DatetimeIndex（确保索引为日期格式）适用于掘金量化
def date(df):
    df['eob'] = pd.to_datetime(df['eob'])
    df.set_index('eob', inplace=True)
    return df

# 计算【一剑成魔】技术指标
def monster(df):
    df['ma20'] = ta.sma(df['close'],20)
    df['os'] = 100*(df['close']-df['ma20'])
    df['os1'] = ta.ema(df['os'],6)
    df['os2'] = df['os'].rolling(window=60).max()
    df['os3'] = ta.ema(df['os2'], 26)
    df['line'] = 100
    return df

# 绘制【一剑成魔】图表
def monster_k(df):
    # 创建 K 线图
    fig = go.Figure()

    # 添加 K 线图
    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
        increasing_line_color='red',  # 增长的K线颜色
        decreasing_line_color='green'     # 下降的K线颜色
    ))

    # 添加附图1：OS 指标
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['os'],
        mode='lines',
        name='OS',
        line=dict(color='blue'),
        yaxis='y2'  # 设置该线在附图2显示
    ))

    # 添加附图2：OS1 指标
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['os1'],
        mode='lines',
        name='OS1',
        line=dict(color='green'),
        yaxis='y2'  # 设置该线在附图2显示
    ))

    # 添加附图4：OS3 指标
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['os3'],
        mode='lines',
        name='OS3',
        line=dict(color='purple'),
        yaxis='y2'  # 设置该线在附图2显示
    ))
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['line'],
        mode='lines',
        name='line',
        line=dict(color='black'),
        yaxis='y2'
    ))
    # 更新图表的布局
    fig.update_layout(
        title = '一剑成魔',
        xaxis_title='Date',
        yaxis_title='Price',
        width=1000,  # 设置宽度
        height=800,  # 设置高度
        xaxis_rangeslider_visible=False,  # 隐藏下方的范围滑块
        template='plotly',  # 可选的主题，'plotly', 'plotly_dark', 'ggplot2', 等等
        yaxis=dict(domain=[0.5, 1]),  # 主图占用 y 轴的 40% 到 100%
        yaxis2=dict(domain=[0, 0.4], title='')  # 附图占用 y 轴的 0% 到 40%
    )

    # 显示图表
    fig.show()











