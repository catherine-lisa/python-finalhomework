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
    elif y.find('million') != -1:
        return int(float(y.split(' ')[0]) * 1000000)
    elif y.find('billion') != -1:
        return int(float(y.split(' ')[0]) * 1000000000)
    else:
        return 0

def num_transform_float(data):
    y = str(data)
    y = y.replace('%', '')
    y = y.replace(',', '')
    if len(y) > 0:
        return float(y)
    else:
        return 0
    
df = pd.read_csv('data.csv')
#筛掉非国家的数据
df = df.loc[df['country'].isin(NotCountryList) == False]
#获取所有的数据
df['confirmed_cases_per_million'] = df['confirmed_cases_per_million'].apply(num_transform_float)
df['people_vaccinated'] = df['people_vaccinated'].apply(num_transform_float)
df['confirmed_deaths'] = df['confirmed_deaths'].apply(num_transform_float)
df['confirmed_cases'] = df['confirmed_cases'].apply(num_transform)
df['new_cases'] = df['new_cases'].apply(num_transform)
#确诊率
df1 = df.groupby('country')['confirmed_cases_per_million'].max().sort_index()
#疫苗接种率
df2 = df.groupby('country')['people_vaccinated'].max().sort_index() / 100
#死亡数/确诊数=死亡率
df3 = df.groupby('country')['confirmed_deaths'].max().sort_index()
df4 = df.groupby('country')['confirmed_cases'].max().sort_index()
df3 = df3 / df4
#确诊率越低，接种率越高，死亡率越低，抗疫效果越好,体现为数值越大越好
valuedf =(-1*df1) * 0.3 + df2 * 0.4 + (-1*df3) * 0.3
#乘上-1变为正数，此时越小越好
valuedf *= -1

valuedf = valuedf.sort_values(ascending=True).head(10)
plt.bar(valuedf.index, valuedf.values, alpha=0.8)
plt.ylabel("综合参数(越小越好)")
plt.title("2021年12月5日-20日抗疫排名")
plt.xlabel("国家或地区")
plt.show()

