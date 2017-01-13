# -*- coding: utf-8 -*-
import scrapy


class ZhongcaoyaoItem(scrapy.Item):
    name = scrapy.Field()

class zhongyaoSpider(scrapy.Spider):
    name="zhongcaoyao"
    
    url  = "http://www.zhongyoo.com/name/"   
    start_urls = [ url+"page_"+str(i)+".html" for i in range(1,42)]

    def parse(self,response):
        item = ZhongcaoyaoItem()
        item['name'] = response.xpath('//div[@class="sp"]//strong/a/text()').extract()
        yield item       
