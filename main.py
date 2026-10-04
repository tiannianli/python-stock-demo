import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取模拟股票csv数据
df = pd.read_csv("data/stock.csv")
# 日期转为时间格式
df["date"] = pd.to_datetime(df["date"])
# 按日期排序
df = df.sort_values("date").reset_index(drop=True)

# 计算5日均线
df["ma5"] = df["close"].rolling(window=5).mean()

# 简单缺失值清洗
df = df.dropna(subset=["close"])

# 绘图
plt.figure(figsize=(12,6))
plt.plot(df["date"], df["close"], label="收盘价", color="#2E86AB")
plt.plot(df["date"], df["ma5"], label="5日均线", color="#A23B72", linestyle="--")
plt.title("股票收盘价与5日均线可视化")
plt.xlabel("日期")
plt.ylabel("价格")
plt.legend()
plt.grid(alpha=0.3)
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

print("数据分析完成！")
print(df[["date","close","ma5"]].head(10))
