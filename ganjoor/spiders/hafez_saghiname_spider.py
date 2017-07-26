# -*- coding: utf-8 -*-
import scrapy


class HafezMasnaviSpider(scrapy.Spider):
    name = "hafez_saghiname"
    allowed_domains = ["ganjoor.net"]
    start_urls = ['https://ganjoor.net/hafez/saghiname']

    def parse(self, response):
        sh = {}
        for index, poem in enumerate(response.css('div.poem>article>div.b')):
            sh[index] = {
                'm1': poem.css('div.m1>p::text').extract_first(),
                'm2': poem.css('div.m2>p::text').extract_first(),
            }
        yield sh
