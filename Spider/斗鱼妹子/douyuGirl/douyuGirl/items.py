# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyugirlItem(scrapy.Item):
    nickname = scrapy.Field()
    imagelink = scrapy.Field()
    imagePath = scrapy.Field()