# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class BbsspiderPipeline(object):
    def __init__(self):
        self.file=codecs.open('./result/bbs_data_utf8.json','wb',encoding='UTF-8')
    def process_item(self, item, spider):
        """
        将Item以JSON格式存放
        """
        line=json.dumps(dict(item))+'\n'
        self.file.write(line.decode("unicode_escape"))
        return item
