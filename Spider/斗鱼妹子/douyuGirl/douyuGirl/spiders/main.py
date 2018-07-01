# -*- coding: utf-8 -*-
import json
import scrapy
from douyuGirl.items import DouyugirlItem


class MainSpider(scrapy.Spider):
    name = 'main'
    allowed_domains = ['capi.douyucdn.cn']

    offset = 0
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    start_urls = [url + str(offset)]

    def parse(self, response):
        data = json.loads(response.text)["data"]

        for each in data:
            item = DouyugirlItem()
            item["nickname"] = each["nickname"]
            item["imagelink"] = each["vertical_src"]

            yield item

        self.offset += 20
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)









