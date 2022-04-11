import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

NotCountryList=['World','Africa','North America','South America','Europe','Asia','Oceania','High income','European Union','Upper middle income','Lower middle income','Low income']

def num_transform(data):
    y = str(data)
    y = y.replace(',', '')
    if y.isdigit():
        return int(y) / 1000000
    elif len(y) > 0:
        return float(y.split(' ')[0])
    else:
        return 0

df = pd.read_csv('data.csv')
#筛掉非国家的数据
df = df.loc[df['country'].isin(NotCountryList) == False]
#选取总和为前十的国家
df['confirmed_cases'] = df['confirmed_cases'].apply(num_transform)
list = df.groupby('country')['confirmed_cases'].max().sort_values(ascending=False).head(10)

plt.xlabel("国家")
plt.ylabel("累计确诊（百万人）")
plt.title('2021年12月5日~20日累计确诊前十的国家和数量')
plt.bar(list.index, list.values, width=0.5)
for a, b in zip(list.index, list.values):
    plt.text(a, b+2, b, ha='center', va='top', fontsize=10)

plt.show()
