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
    elif not np.isnan(float(y.split(' ')[0])):
        return int(float(y.split(' ')[0]) * 1000000)
    else:
        return np.nan
    

df = pd.read_csv('data.csv')
#筛掉非国家的数据
df = df.loc[df['country'].isin(NotCountryList) == False]
df['confirmed_deaths'] = df['confirmed_deaths'].apply(num_transform)
df['confirmed_cases'] = df['confirmed_cases'].apply(num_transform)
maxdate = df['time'].max()
df = df.loc[df['time']==maxdate]
#计算死亡率
df['confirmed_deaths_rate'] = df['confirmed_deaths'] / df['confirmed_cases'] * 100
#取前10的国家
list = df.groupby('country')['confirmed_deaths_rate'].max().sort_values(ascending=False).head(10)

plt.xlabel("国家")
plt.ylabel("每百万人死亡人数")
plt.title('2021年12月5日-20日死亡率')
plt.bar(list.index, list.values, width=0.5)
for a, b in zip(list.index, list.values):
    plt.text(a, b+1, '{:.2f}%'.format(b), ha='center', va='top', fontsize=10)

plt.show()