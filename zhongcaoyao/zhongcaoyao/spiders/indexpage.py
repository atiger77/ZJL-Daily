# -*- coding: utf-8 -*-
import scrapy
from openpyxl import Workbook

class zhongyaoSpider(scrapy.Spider):
    name="zhongcaoyao"
    
    url  = "http://www.zhongyoo.com/name/"   
    start_urls = [ url+"page_"+str(i)+".html" for i in range(1,5)]

    def parse(self,response):
        wb = Workbook()
        ws = wb.active
        name = response.xpath('//div[@class="sp"]//strong/a/text()').extract()
        for i in name:
            ws.append([i])
            wb.save('zhongcaoyao.xlsx')    
        
