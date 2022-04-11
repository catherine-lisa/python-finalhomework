import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

NotCountryList=['World','Africa','North America','South America','Europe','Asia','Oceania','High income','European Union','Upper middle income','Lower middle income','Low income']

def num_transform(data):
    y = str(data)
    y = y.replace(',', '')
    if len(y) > 0:
        return float(y)
    else:
        return 0
 
df = pd.read_csv('data.csv')
#筛掉非国家的数据
df = df.loc[df['country'].isin(NotCountryList) == False]
#删除"," 统一数据形式
df['confirmed_cases_per_million'] = df['confirmed_cases_per_million'].apply(num_transform)
#获取占比前10的国家
list = df.groupby('country') ['confirmed_cases_per_million'].max().sort_values(ascending=False).head(10)
plt.xlabel("国家")
plt.ylabel("每百万人累计确诊")
plt.title('2021年12月5日-20日每百万人确诊前十')

plt.bar(list.index, list.values, width=0.5)
for a, b in zip(list.index, list.values):
    plt.text(a, b+10000, b, ha='center', va='top', fontsize=10)
plt.show()