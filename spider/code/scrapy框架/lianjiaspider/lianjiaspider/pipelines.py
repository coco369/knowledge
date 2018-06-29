# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv


class LianjiaPipeline(object):

    def process_item(self, item, spider):
        f = open('lianjia.csv', 'a+')
        write = csv.writer(f)
        write.writerow((item['title'], item['community'], item['model'], item['area'], \
        item['focus_num'], item['watch_num'], item['time'], item['price'], item['average_price'], item['link'], \
        item['city'], item['page']))

        return item
