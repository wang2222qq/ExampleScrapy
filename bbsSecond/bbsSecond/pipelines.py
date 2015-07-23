# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from json import dumps
from codecs import open

class BbssecondPipeline(object):
    def __init__(self):
        self.file=open("./result/date_utf8.json","wb",encoding="UTF-8")
    def process_item(self, item, spider):
        """
        Item 以JSON格式存放
        """
        line=dumps(dict(item))+'\n'
        self.file.write(line.decode("unicode_escape"))
        return item
