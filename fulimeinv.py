# coding: utf-8

import scrapy
from fuli.items import FuliItem

class DoubanmeinvSpider(scrapy.Spider):
    name = 'fuli'
    allowed_domains = ["dbmeinv.com"]
    url = 'https://www.dbmeinv.com/?pager_offset='
    offset = 1
    start_urls = [url + str(offset)]

    def parse(self, response):
        #每一页帖子
        links = response.xpath('//div[@class="img_single"]//a/@href').extract()
        for link in links:
            yield scrapy.Request(link, callback = self.parseDouban)
        if self.offset < 10:
            self.offset +=1
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    def parseDouban(self, response):
        item = FuliItem()

        item['douTitle'] = response.xpath('//h1/text()').extract()[0]

        pic = response.xpath('//div[@class="topic-figure cc"]/img/@src').extract()
        #print 'pic',pic
        if len(pic) == 0:
            item['douPicture'] = response.xpath('//div[@class="image-wrapper"]/img/@src').extract()
        else:
            item['douPicture'] = pic

        item['douName'] = response.xpath('//li[@class="name"]/text()').extract()[0]

        live = response.xpath('//li[@class="loc"]/text()').extract()[0]

        item['douLive'] = live.split(':')[1].split(' ')[0]

        yield item


