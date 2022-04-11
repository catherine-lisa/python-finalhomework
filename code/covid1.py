import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

plt.rcParams['font.sans-serif'] = ['SimHei']

def num_transform(data):
    y = str(data)
    y = y.replace(',', '')
    if y.isdigit():
        return int(y)
    else:
        return 0
    
df = pd.read_csv('data.csv')

Y = df.loc[df['country']=='World']['new_cases'].apply(num_transform)
X = df.loc[df['country']=='World']['time']

for a,b in zip(X,Y):
    plt.text(a, b, b, ha='center',va='bottom',fontsize=9,color='b',alpha=0.9)
plt.plot(X, Y, linewidth=4)
plt.xlabel("日期")
plt.ylabel("每日新增确诊（人）")
plt.title('世界每日新增病例(2021年12月5日-2022年1月20日)')

plt.show()

