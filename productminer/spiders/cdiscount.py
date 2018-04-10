# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CdiscountSpider(CrawlSpider):
    name = 'cdiscount'
    allowed_domains = ['cdiscount.com']
    start_urls = ['http://cdiscount.com/']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        filename = 'downloads/'+response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)