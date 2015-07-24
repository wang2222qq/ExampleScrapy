# ExampleScrapy
循序渐进的学习Scrapy的过程

# 依赖库

json
codecs
scrapy 

# Create (2015-07-22)
第一版本(bbsspider):
     功能：爬取单个论坛页面，获取论坛的题目与连接。然后生成JSON格式的文件

# Update (2015-07-23)
第二版本(bbsSecond):
     功能: 根据论坛主页网址(domain),获取子论坛地址。然后爬取子论坛里的标题与连接，并自动翻页爬取。
           结果生成在项目根目录下的result文件夹内，以JSON格式保存。
     爬取速度：慢


