# -*- coding: utf-8 -*-

# Scrapy settings for bbsSecond project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bbsSecond'

SPIDER_MODULES = ['bbsSecond.spiders']
NEWSPIDER_MODULE = 'bbsSecond.spiders'
##使用pipeline里的BbssecondPipeline类
ITEM_PIPELINES={
    'bbsSecond.pipelines.BbssecondPipeline':300
}

##禁止cookies,防止被ban
COOKIES_ENABLED = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bbsSecond (+http://www.yourdomain.com)'
