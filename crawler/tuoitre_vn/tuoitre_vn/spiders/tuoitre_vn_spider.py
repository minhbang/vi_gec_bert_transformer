# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from datetime import datetime, timedelta


class TuoitreVnSpider(Spider):
    name = 'tuoitre_vn'
    start_urls = ['https://tuoitre.vn/van-hoa/xem-theo-ngay/%s.html']
    domain = 'https://tuoitre.vn'
    xpaths = {
        'news_href': '//li[@class="news-item"]/a/@href',
        'news_content': '//div[@id="main-detail-body"]/p'
    }

    def __init__(self, start_date=None, days=2, **kwargs):
        if start_date is None:
            start_date = datetime.now()
        else:
            start_date = datetime.strptime(start_date, '%d-%m-%Y')

        dates = []
        for i in range(int(days)):
            dates.append(start_date.strftime('%d-%m-%Y'))
            start_date = start_date - timedelta(days=1)

        urls = []
        for url in self.start_urls:
            for date in dates:
                urls.append(url % date)
        self.start_urls = urls

        super().__init__(**kwargs)  # python3

    def parse(self, response):
        for href in response.xpath(self.xpaths['news_href']).getall():
            yield Request(self.domain + href, self.parse_article)

    def parse_article(self, response):
        content = '\n'.join(response.xpath(self.xpaths['news_content']).extract()).strip()
        return {'content': content}
