from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd

def num_transform(data):
    y = str(data)
    y = y.replace('%', '')
    return float(y) / 100
    
NotCountryList=['World','Africa','North America','South America','Europe','Asia','Oceania','High income','European Union','Upper middle income','Lower middle income','Low income']


df = pd.read_csv('data.csv')
#筛掉非国家的数据
df = df.loc[df['country'].isin(NotCountryList) == False]
df['people_vaccinated'] = df['people_vaccinated'].apply(num_transform)
df = df.groupby('country')['people_vaccinated'].max()

Map().add(
    "疫苗接种率",
    [list(z) for z in zip(df.index, df.values)],
    is_map_symbol_show=False,
    maptype="world",
    label_opts=opts.LabelOpts(is_show=False),
    itemstyle_opts=opts.ItemStyleOpts(color="rgba(255,255,255,0.5)"),
).set_series_opts(label_opts=opts.LabelOpts(is_show=False)).set_global_opts(
    title_opts=opts.TitleOpts(title="疫苗接种率"),
    visualmap_opts=opts.VisualMapOpts(max_=1.0),
).render("6.html")

    