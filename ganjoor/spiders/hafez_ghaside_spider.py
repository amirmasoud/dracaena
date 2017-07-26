# -*- coding: utf-8 -*-
import scrapy


class HafezMasnaviSpider(scrapy.Spider):
    name = "hafez_ghaside"
    allowed_domains = ["ganjoor.net"]
    start_urls = ['https://ganjoor.net/hafez/ghaside/sh1/']

    def parse(self, response):
        sh = {}
        txt = response.css('div.poem>article>h2>a::text').extract_first()
        try:
            sh['title'] = txt.split('-')[1]
        except IndexError:
            sh['title'] = ''
        try:
            sh['unit'] = 'قصیده'
        except IndexError:
            sh['unit'] = 'شعر'
        for index, poem in enumerate(response.css('div.poem>article>div.b')):
            sh[index] = {
                'm1':    poem.css('div.m1>p::text').extract_first(),
                'm2':    poem.css('div.m2>p::text').extract_first(),
            }
        yield sh
        next_page = response.css('div.navigation>div.navleft>a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
