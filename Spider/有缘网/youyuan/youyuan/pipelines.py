# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
import json

class YouyuanPipeline(object):
    def process_item(self, item, spider):
        item['time'] = datetime.utcnow()
        item['spidername'] = spider.name
        return item
