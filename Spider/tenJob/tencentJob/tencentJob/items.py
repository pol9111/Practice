# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentjobItem(scrapy.Item):
    name_work = scrapy.Field()
    detail_link = scrapy.Field()
    position_info = scrapy.Field()
    people_num = scrapy.Field()
    work_localtion = scrapy.Field()
    publish_time = scrapy.Field()
