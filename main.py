import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取模拟股票csv数据
df = pd.read_csv("数据/stock.csv")
# 日期转为时间格式
df["日期"] = pd.to_datetime(df["日期"])
# 按日期排序
df = df.sort_values("日期").reset_index(drop=True)

# 计算5日均线 MA5
df["MA5"] = df["关闭"].rolling(window=5).mean()

# 简单缺失值清洗
df = df.dropna(subset=["关闭"])

# 绘图
plt.figure(figsize=(12,6))
plt.plot(df["日期"], df["关闭"], label="收盘价", color="#2E86AB")
plt.plot(df["日期"], df["MA5"], label="5日均线", color="#A23B72", linestyle="--")
plt.title("股票收盘价与5日均线可视化")
plt.xlabel("日期")
plt.ylabel("价格")
plt.legend()
plt.grid(alpha=0.3)
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

