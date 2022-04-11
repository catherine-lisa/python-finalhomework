# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class NcovspiderPipeline:
    def open_spider(self, spider):
        self.df = pd.DataFrame(columns=['country', 'time', 'new_cases', 'confirmed_cases', 'confirmed_cases_per_million', 'people_vaccinated', 'people_fully_vaccinated', 'confirmed_deaths'])

    def process_item(self, item, spider):
        dict_item = ItemAdapter(item).asdict()
        if (self.df[(self.df['country'] == dict_item['country']) & (self.df['time'] == dict_item['time'])].empty):
            self.df = self.df.append(dict_item, ignore_index=True)
        else:
            index = self.df[(self.df['country'] == dict_item['country']) & (self.df['time'] == dict_item['time'])].index[0]
            for (key, value) in dict_item.items():
                #这里对空值进行处理
                if value != "":
                    self.df.at[index, key] = value
        return item
    
    def close_spider(self, spider):
        self.df.sort_values(by=['country', 'time'], inplace=True)
        self.df.to_csv('data.csv', index=False)
