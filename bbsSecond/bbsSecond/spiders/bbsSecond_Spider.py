# -*- coding: utf-8 -*-
#bbsSecond_Spider.py
"""
Created on Thu Jul 23 10:13:13 2015

@author: Frank
"""
from scrapy.spider import Spider  
from scrapy.http import Request  
from scrapy.selector import Selector  
from scrapy.log import start,msg
from bbsSecond.items import BbssecondItem

class BBSSecondSpider(Spider):
    """
    论坛爬虫
    """
    name="bbsSecond"

    #减慢爬虫速度 为1s
    download_delay=1
    allowed_domains=["bbs2.99nets.me"]
    start_urls =[
            ##论坛主页
            "http://bbs2.99nets.me",
            ]
    def __init__(self,*args,**kwargs):
        super(BBSSecondSpider,self).__init__(*args,**kwargs)
        start("./Debug.log",'INFO',False)
        self.IndexFlag=True

    def parse(self,response):
        """
        第一次解析时，由于是论坛主页,XPath解析规则不同,之后根据从主页上获取子
        论坛URL后，对每个子论坛的URL调用Parse
        """
        sel=Selector(response)
        items=[]
        if self.IndexFlag:
            self.IndexFlag=False
##由于使用BBS论坛页面原因，使用Xpath方式获取不是很好的选择
            urls=sel.re(r"(http://bbs2.99nets.me/forum.*html)")[1:-2]
            for url in urls:
                msg("------URL: %s -----" % url,level="DEBUG")
                yield Request(url,callback=self.parse)
            msg("-----Crawl END----",level="INFO")
        else:
            sites=sel.xpath("//form/table/tbody/tr/th/a[@class='s xst']")
            for site in sites:
                item=BbssecondItem()
                item['title']=site.xpath("text()").extract()
                item['link'] =site.xpath("@href").extract()
                yield item
            url,text=response.url,sel.xpath("//title/text()").extract()
            msg("---CURRENT URL:%s \n ---TEXT:%s" % (url,str(text).encode("UTF8")),
                    level='INFO')
            ##子论坛翻页
            rule="//div[@class='pg']/a[@class='nxt']/"
            if sel.xpath(rule+"text()").extract():
                yield Request(sel.xpath(rule+"@href").extract()[0]
                        ,callback=self.parse)

            
            



           
        

    
    

