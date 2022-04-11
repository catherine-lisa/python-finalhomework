import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

NotCountryList=['World','Africa','North America','South America','Europe','Asia','Oceania','High income','European Union','Upper middle income','Lower middle income','Low income']
gdpList=['Luxembourg','Singapore','Ireland','Qatar','Bermuda','Cayman Islands','Switzerland','United Arab Emirates','Norway','Brunei']

def num_transform(data):
    y = str(data)
    y = y.replace(',', '')
    if y.isdigit():
        return int(y)
    elif len(y) > 0:
        return float(y.split(' ')[0]) * 1000000
    else:
        return 0
    
df = pd.read_csv('data.csv')
df = df.loc[(df['country'].isin(NotCountryList) == False) & (df['country'].isin(gdpList))]
#统一数据形式
df['confirmed_cases'] = df['confirmed_cases'].apply(num_transform)
#绘制箱型图
list = df.groupby('country')['confirmed_cases'].max().sort_values(ascending=False)
list.plot.box(title='2021年12月20日GDP前十国家累计确诊')
plt.ylabel("累计确诊人数")
plt.grid(linestyle='--', linewidth=1, color='#d8d8d8')
plt.show()
print ("平均数：", list.mean())