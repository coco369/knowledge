
import json

from scrapy import Request
from scrapy.spiders import Spider
from scrapy.selector import Selector

from lianjiaspider.items import LianjiaspiderItem


class LianJiaSpider(Spider):

    name = 'lianjia'
    # allowed_domains = ['lianjia.com']
    domains_url = 'https://cd.lianjia.com'
    start_linjia_url = 'https://cd.lianjia.com/ershoufang'

    def start_requests(self):
        yield Request(self.start_linjia_url)

    def parse(self, response):

        sel = Selector(response)
        ershoufang_aera = sel.xpath('//div[@data-role="ershoufang"]')
        area_info = ershoufang_aera.xpath('./div/a')

        for area in area_info:
            area_href = area.xpath('./@href').extract()[0]
            area_name = area.xpath('./text()').extract()[0]

            yield Request(self.domains_url + area_href,
                          callback=self.parse_house_info,
                          meta={'name': area_name, 'href': area_href})

    def parse_house_info(self, response):
        sel = Selector(response)
        page_box = sel.xpath('//div[@class="page-box house-lst-page-box"]/@page-data').extract()
        total_page = json.loads(page_box[0]).get('totalPage')

        for i in range(1, int(total_page)+1):
            yield Request(self.domains_url + response.meta.get('href') + 'pg' + str(i),
                          callback=self.parse_house,
                          meta={'name': response.meta.get('name')})

    def parse_house(self, response):

        sel = Selector(response)
        lis = sel.xpath('//html/body/div[4]/div[1]/ul/li[@class="clear"]')
        for li in lis:

            item = LianjiaspiderItem()
            item['house_code'] = li.xpath('./a/@data-housecode').extract()[0]
            if li.xpath('./a/img/@src').extract():
                item['img_src'] = li.xpath('./a/img/@src').extract()[0]
            if li.xpath('./div/div/a/text()').extract():
                item['title'] = li.xpath('./div/div/a/text()').extract()[0]
            item['address'] = li.xpath('./div/div[2]/div/a/text()').extract()
            item['info'] = li.xpath('./div/div[2]/div/text()').extract()
            item['flood'] = li.xpath('./div/div[3]/div/text()').extract()
            item['tag'] = li.xpath('.//div[@class="tag"]/span/text()').extract()
            item['type'] = 'ershoufang'
            item['city'] = '成都'
            item['area'] = response.meta.get('name')

            yield item

    def split_house_info(self, info):
        return [i.strip() for i in info.split('|')[1:]]