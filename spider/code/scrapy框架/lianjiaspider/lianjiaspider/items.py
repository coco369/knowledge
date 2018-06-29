# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    page = scrapy.Field()
    title = scrapy.Field()
    community = scrapy.Field()
    model = scrapy.Field()
    area = scrapy.Field()
    focus_num = scrapy.Field()
    watch_num =scrapy.Field()
    time = scrapy.Field()
    price = scrapy.Field()
    average_price =scrapy.Field()
    link = scrapy.Field()
    city = scrapy.Field()

