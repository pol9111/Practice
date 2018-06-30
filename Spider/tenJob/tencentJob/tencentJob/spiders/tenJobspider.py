# -*- coding: utf-8 -*-
import scrapy, re
from tencentJob.items import TencentjobItem

class TenjobspiderSpider(scrapy.Spider):
    name = 'tenJobspider'
    allowed_domains = ['hr.tencent.com']
    url = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            item = TencentjobItem()
            name_work = each.xpath('./td[1]/a[@target]/text()').extract()[0]
            detail_link = each.xpath('./td[1]/a/@href').extract()[0]
            position_info = each.xpath('./td[2]/text()').extract()
            people_num = each.xpath('./td[3]/text()').extract()[0]
            work_localtion = each.xpath('./td[4]/text()').extract()[0]
            publish_time = each.xpath('./td[5]/text()').extract()[0]


            item['name_work'] = name_work
            item['detail_link'] = detail_link
            item['position_info'] = position_info
            item['people_num'] = people_num
            item['work_localtion'] = work_localtion
            item['publish_time'] = publish_time

            yield item

        if self.offset < 3760:
            self.offset += 10

        # else:
        #     raise "没有下一页了"

        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)






