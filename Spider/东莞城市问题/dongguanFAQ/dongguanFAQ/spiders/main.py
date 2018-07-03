# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from dongguanFAQ.items import DongguanfaqItem


class MainSpider(CrawlSpider):
    name = 'main'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']


    rules = (
        Rule(LinkExtractor(allow=r'type=4&page=\d+')), # 没有callback  follow默认为True 每页调用执行这个规则
        Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'), callback='parse_item'), # 有callback  follow默认为False 不用跟进
    )

    def parse_item(self, response):
        item = DongguanfaqItem()

        item['title'] = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        item['number'] = item['title'].split(' ')[-1].split(":")[-1]
        item['content'] = response.xpath('//div[@class="pagecenter p3"]//div[@class="c1 text14_2"]/text() | //div[@class="pagecenter p3"]//div[@class="c1 text14_2"]//div').extract()[0]
        item['url'] = response.url

        yield item