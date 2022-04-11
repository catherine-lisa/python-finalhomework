import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

NotCountryList=['World','Africa','North America','South America','Europe','Asia','Oceania','High income','European Union','Upper middle income','Lower middle income','Low income']

def num_transform(data):
    y = str(data)
    y = y.replace('%', '')
    if len(y) > 0:
        return float(y) / 100
    else:
        return 0
    
#筛掉非国家的数据
df = pd.read_csv('data.csv')
df = df.loc[df['country'].isin(NotCountryList) == False]
#统一百分比数据形式
df['people_fully_vaccinated'] = df['people_fully_vaccinated'].apply(num_transform)
#取最低的五个国家
list = df.groupby('country')['people_fully_vaccinated'].max().sort_values(ascending=True).head(10)

plt.xlabel("国家")
plt.ylabel("接种率")
plt.title('2021年12月5日-20日接种率最低前十')

plt.bar(list.index, list.values, width=0.5)
for a, b in zip(list.index, list.values):
    plt.text(a, b+0.0005, b, ha='center', va='top', fontsize=10)

plt.show()
