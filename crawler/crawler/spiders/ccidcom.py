# -*- coding: utf-8 -*-
import scrapy
from crawler.crawler.items import CrawlerItem


class CcidcomSpider(scrapy.Spider):
    name = 'ccidcom'
    allowed_domains = ['ccidcom.com']
    start_urls = [
        'http://www.ccidcom.com/yaowen/20200517/dWhVS6rn8kyER9Cjt17hatdz73u3k.html']

    def parse(self, response):
        item = CrawlerItem()
        item['title'] = response.css('div.heading::text').get()
        yield item
