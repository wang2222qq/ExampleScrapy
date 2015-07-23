# -*- coding:utf8 -*-
#bbsspiderSpider.py
from scrapy import Spider,log,Selector
from bbsspider.items import BbsspiderItem

class BBSSpider(Spider):
    #爬虫器名字,必须要赋值的，且是scrapy同一项目中唯一的名字
    name='bbs'
    allowed_domains=['28tui.com']
    #目标网址,需注意变量名字
    start_urls=[
            'http://bbs.28tui.com/forum-46-1.html',
            'http://bbs.28tui.com/forum-38-1.html',
            'http://bbs.28tui.com/forum-42-1.html',
            ]
    def __inti__(self,*args,**kwargs):
        super(BBSSpider,self).__init__(*args,**kwargs)
        ##打开日志机制,放在项目根目录下
        log.start("./log/BBS_Spider_log.txt","INFO",false)
    def parse(self,response):
        """
        利用正则匹配,获取内容，将内容存放在item中并返回,然后交给pipelines.py中
        的函数进行处理
        """            
        sel=Selector(response)
        sites=sel.xpath("//tbody/tr/th/a[@class='s xst']")
        items=[]
        for site in sites:
            item=BbsspiderItem()
            item['title']=site.xpath("text()").extract()
            item['link'] =site.xpath("@href").extract()
            items.append(item)
            log.msg("------Appending item-----",level='INFO')
        log.msg("-----Parse URL:%s END------" % response.url,level='INFO')
        return items
           