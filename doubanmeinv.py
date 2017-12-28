# coding: utf-8
import scrapy
# 导入CrawlSpider类和Rule
from scrapy.spiders import CrawlSpider, Rule
# 导入链接规则匹配类，用来提取符合规则的连接
from scrapy.linkextractors import LinkExtractor
from fuli.items import FuliItem

class DoubanmeinvSpider(CrawlSpider):
    name = 'doubanmeinv'
    allowed_domains = ["dbmeinv.com"]
    start_urls = ["https://www.dbmeinv.com/?pager_offset=1"]

    rules = (
        # 本案例的url被web服务器篡改，需要调用process_links来处理提取出来的url
        Rule(LinkExtractor(allow=r"pager_offset=\d+")),
        Rule(LinkExtractor(allow=r"dbgroup/\d+"), callback = "parseDouban"),
    )

    def parseDouban(self, response):
        item = FuliItem()

        item['douTitle'] = response.xpath('//h1/text()').extract()[0]

        item['douPicture'] = response.xpath('//div[@class="topic-figure cc"]/img/@src').extract()

        item['douName'] = response.xpath('//li[@class="name"]/text()').extract()[0]

        live = response.xpath('//li[@class="loc"]/text()').extract()[0]

        item['douLive'] = live.split(':')[1].split(' ')[0]

        yield item


