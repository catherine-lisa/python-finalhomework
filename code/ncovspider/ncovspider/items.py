# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NcovspiderItem(scrapy.Item):
    # define the fields for your item here like:
    country = scrapy.Field()                       #表示国家名
    time = scrapy.Field()                          #表示爬取数据的时间
    new_cases = scrapy.Field()                     #新增病例数
    confirmed_cases = scrapy.Field()               #确诊人数
    confirmed_cases_per_million = scrapy.Field()   #每百万的确诊人数
    people_vaccinated = scrapy.Field()             #注射疫苗的人数
    people_fully_vaccinated = scrapy.Field()       #接种超过一针的人数
    confirmed_deaths = scrapy.Field()              #死亡人数
    pass
