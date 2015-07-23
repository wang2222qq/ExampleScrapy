# -*- coding: utf-8 -*-

# Scrapy settings for bbsspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bbsspider'

SPIDER_MODULES = ['bbsspider.spiders']
NEWSPIDER_MODULE = 'bbsspider.spiders'
##目前还不清楚作用
ITEM_PIPELINES={
    'bbsspider.pipelines.BbsspiderPipeline':300,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bbsspider (+http://www.yourdomain.com)'
