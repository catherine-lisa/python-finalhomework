import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

NotCountryList=['World','Africa','North America','South America','Europe','Asia','Oceania','High income','European Union','Upper middle income','Lower middle income','Low income']

def num_transform(data):
    y = str(data)
    y = y.replace(',', '')
    if y.isdigit():
        return int(y)
    else:
        return 0

df = pd.read_csv('data.csv')
df['new_cases'] = df['new_cases'].apply(num_transform)
#筛掉非国家的数据
df = df.loc[df['country'].isin(NotCountryList) == False]
#选取总和为前十的国家
list = df.groupby('country')['new_cases'].sum().sort_values(ascending=False).head(10).index.tolist()

plt.xlabel("日期")
plt.ylabel("每日新增确诊（人）")
plt.title('2021年12月5日-2022年1月20日每日新增病例')
for i in list:
    Y = df.loc[df['country']==i]['new_cases'].apply(num_transform)
    X = df.loc[df['country']==i]['time']
    plt.plot(X, Y, linewidth=1, marker='o', label=i, markersize=2)
    for a, b in zip(X, Y):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

plt.legend(list, loc='upper left', fontsize=10)
plt.show()
