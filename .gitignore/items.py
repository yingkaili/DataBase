# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FuliItem(scrapy.Item):

    #个人主页
    douHomePage = scrapy.Field()

    #说说标题
    douTitle = scrapy.Field()

    #个人图片
    douPicture = scrapy.Field()

    #豆瓣名字
    douName = scrapy.Field()

    #居住地
    douLive = scrapy.Field()


