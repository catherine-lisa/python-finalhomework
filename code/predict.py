import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

def num_transform(data):
    y = str(data)
    y = y.replace(',', '')
    if y.isdigit():
        return int(y)
    else:
        return 0

df = pd.read_csv('data.csv')
#X Y表示原始数据
Y = df.loc[df['country']=='World']['new_cases'].apply(num_transform).values
X = df.loc[df['country']=='World']['time']

#NewY表示预测的数据，前10保持不变
NewY = []
for i in range(0, 10):
    NewY.append(Y[i])
#用base计算7天周期的波动平均值
base = 0
for i in range(0, 3):
    base += Y[i + 7] - Y[i]
base = (base / 3)
#预测后5天的数据
for i in range(10, 16):
    NewY.append(Y[i - 7] + base)

#绘制趋势图
plt.plot(X, Y, linewidth=4)
for (a, b) in zip(X, Y):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.plot(X, NewY, linewidth=4)
for (a, b) in zip(X, NewY):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.legend(['原始数据', '预测值'])
plt.xlabel("日期")
plt.ylabel("每日新增确诊（人）")
plt.title('世界每日新增病例(2021年12月5日-2022年1月20日)')
plt.show()