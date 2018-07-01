# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import scrapy, os

class ImagesPipeline(ImagesPipeline):
    IMAGE_STROE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        image_url = item["imagelink"]
        yield scrapy.Request(image_url)

    def item_completed(self, result, item, info):
        image_path = [x["path"] for ok, x in result if ok]

        os.rename(self.IMAGE_STROE + "/" + image_path[0], self.IMAGE_STROE + "/" + item["nickname"] + '.jpg')

        item["imagePath"] = self.IMAGE_STROE + "/" + item["nickname"]

        return item
