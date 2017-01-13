# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from openpyxl import Workbook
class ZhongcaoyaoPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['name'])
    

    def process_item(self, item, spider):
        line = item['name']

        for i in line:
            self.ws.append([i])
            self.wb.save('zhongcaoyao.xlsx')
        return item

