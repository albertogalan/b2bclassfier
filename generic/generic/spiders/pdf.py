# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# This spider download pdf in a determine domain


DATAPATH="/home/agalan/Downloads/crawler"
DOMAINS=["i487.lxd"]
URLS=["http://i487.lxd/pdf/toread"]

# Variables
# start_url 
# domain

class EtsystemsSpider(CrawlSpider):
    name = 'Pdf'
    allowed_domains = DOMAINS
    start_urls = URLS
    custom_settings = {
    #   'LOG_FILE' :'logs/quotes.log',
       # 'LOG_LEVEL':'INFO',
       'DEPTH_LIMIT': 4,
       'ROBOTSTXT_OBEY': False
       # 'COOKIES_ENABLED' : False
        }

    def parse(self, response):
        #if response.headers['Content-Type'].startswith(b'application/pdf'):
        if response.headers['Content-Type'].startswith(b'application/pdf'):
           print(response.url)
           print("doing request")
           self.save_pdf(response)

        else:
            if response.headers['Content-Type'].startswith(b'text'):
                pages = response.css ('a::attr(href)').getall()

                for page  in pages:
                    next_page = response.urljoin(page)
                    self.logger.info('checking links %s', next_page)
                    yield scrapy.Request(next_page, callback=self.parse)

    def save_pdf (self, response):
        print ("saving page")
        os.makedirs(DATAPATH + "/data/" +self.allowed_domains[0], exist_ok=True) 
        path = DATAPATH  +'/data/'+ self.allowed_domains[0] +"/" + response.url.split('/')[-1]
        self.logger.info('Saving PDF %s', path)
        with open(path,'wb') as f:
            f.write(response.body)

