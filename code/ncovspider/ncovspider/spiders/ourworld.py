import scrapy

import datetime
from ncovspider.items import NcovspiderItem

keywordlist = ["new_cases", "confirmed_cases", "confirmed_cases_per_million", "people_vaccinated", "people_fully_vaccinated", "confirmed_deaths"]

class OurworldSpider(scrapy.Spider):
    name = 'ourworld'
    allowed_domains = ['ourworldindata.org']
    start_urls = [
        'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&zoomToSelection=true&facet=none&uniformYAxis=0&pickerSort=asc&pickerMetric=total_cases&Metric=Confirmed+cases&Interval=New+per+day&Relative+to+Population=false&Color+by+test+positivity=false&time=',
        'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&facet=none&Interval=Cumulative&Relative+to+Population=false&Color+by+test+positivity=false&Metric=Confirmed+cases&time=earliest..',
        'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&facet=none&Interval=Cumulative&Relative+to+Population=true&Color+by+test+positivity=false&Metric=Confirmed+cases&time=earliest..',
        'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&facet=none&Metric=People+vaccinated&Interval=Cumulative&Relative+to+Population=true&Color+by+test+positivity=false&time=earliest..',
        'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&facet=none&Metric=People+fully+vaccinated&Interval=Cumulative&Relative+to+Population=true&Color+by+test+positivity=false&time=earliest..',
        'https://ourworldindata.org/explorers/coronavirus-data-explorer?tab=table&facet=none&uniformYAxis=0&Metric=Confirmed+deaths&Interval=Cumulative&Relative+to+Population=false&Color+by+test+positivity=false&time=earliest..',
        ]

    def start_requests(self):
        self.logger.info("Start requests")
        starttime = 5
        endtime = 20
        while starttime <= endtime:
            yield scrapy.Request(self.start_urls[0] + "2022-01-" + (str)starttime, callback=self.parse, cb_kwargs=dict(date="2022-01-" + (str)starttime, type="new_cases"))
            yield scrapy.Request(self.start_urls[1] + "2022-01-" + (str)starttime, callback=self.parse, cb_kwargs=dict(date="2022-01-" + (str)starttime, type="confirmed_cases"))
            yield scrapy.Request(self.start_urls[2] + "2022-01-" + (str)starttime, callback=self.parse, cb_kwargs=dict(date="2022-01-" + (str)starttime, type="confirmed_cases_per_million"))
            yield scrapy.Request(self.start_urls[3] + "2022-01-" + (str)starttime, callback=self.parse, cb_kwargs=dict(date="2022-01-" + (str)starttime, type="people_vaccinated"))
            yield scrapy.Request(self.start_urls[4] + "2022-01-" + (str)starttime, callback=self.parse, cb_kwargs=dict(date="2022-01-" + (str)starttime, type="people_fully_vaccinated"))
            yield scrapy.Request(self.start_urls[5] + "2022-01-" + (str)starttime, callback=self.parse, cb_kwargs=dict(date="2022-01-" + (str)starttime, type="confirmed_deaths"))
            starttime += 1
    
    def parse(self, response, *args, **kwargs):
        item = NcovspiderItem()
        for keyword in keywordlist:
            item[keyword] = ""
        col = 2
        if (kwargs["type"] != "new_cases"):
            col = 3
        
        item['time'] = kwargs['date']
        for row in response.xpath("/html/body/main/div/div[3]/div/div[1]/div/table/tbody/*"):
            item['country'] = row.xpath("./td[1]/text()").get()
            item[kwargs['type']] = row.xpath('./td[{}]/text()'.format(col)).get()
            yield item
            item[kwargs["type"]] = "" #方便for循环的后续处理
