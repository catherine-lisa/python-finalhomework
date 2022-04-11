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
#对数据统一为百万为单位
df['confirmed_cases'] = df['confirmed_cases'].apply(num_transform)
list = df.groupby('country')['confirmed_cases'].max().sort_values(ascending=False).head(25).index.tolist()
#将非前25的所有国家合并为其他
df1 = df.loc[df['country'].isin(list)].groupby('country')['confirmed_cases'].max()
othernum = df.loc[df['country'].isin(list) == False].groupby('country')['confirmed_cases'].max().sum()
df1.sort_values(ascending=False, inplace=True)
df1 = df1.append(pd.Series(othernum, index=['其他']))
#绘制饼图
plt.pie(df1, labels=df1.index, autopct='%1.1f%%', shadow=False, startangle=90)
plt.title('2021年12月5日-20日各国累计确诊比例')

plt.show()