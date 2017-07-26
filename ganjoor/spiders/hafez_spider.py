# -*- coding: utf-8 -*-
import scrapy


class HafezSpider(scrapy.Spider):
    name = "hafez"
    allowed_domains = ["ganjoor.net"]
    start_urls = ['https://ganjoor.net/hafez/ghazal/sh1']

    def parse(self, response):
        sh = {}
        sh['unit'] = 'غزل'
        for index, poem in enumerate(response.css('div.poem>article>div.b')):
            if index == 0:
                sh['title'] = poem.css('div.m1>p::text').extract_first()
            sh[index] = {
                'm1': poem.css('div.m1>p::text').extract_first(),
                'm2': poem.css('div.m2>p::text').extract_first(),
            }
        yield sh
            # yield {
            #     'm1': poem.css('div.m1>p::text').extract_first(),
            #     'm2': poem.css('div.m2>p::text').extract_first(),
            # }
        next_page = response.css('div.navigation>div.navleft>a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)