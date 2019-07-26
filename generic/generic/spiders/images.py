# -*- coding: utf-8 -*-
import scrapy
# from scrapy.http import Request
import os
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
# This spider download pdf in a determine domain

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.utils.response import open_in_browser

from scrapy.shell import inspect_response
import logging

DATAPATH="/home/agalan/Downloads/crawler"
DOMAINS=["wgsn.com"]
URLS=["https://www.wgsn.com/content/personalized/reports?content_types=14&markets=57&seasons=2431"]

DOMAINS=["wow-trend.com"]
URLS=["http://www.wow-trend.com/index/index/gender/2.shtml"]

class ImagesSpider(CrawlSpider):
    name = 'images-wow'
    allowed_domains = DOMAINS
    start_urls = URLS
    login_page = "http://www.wow-trend.com/Join/login"
    custom_settings = {
      'LOG_FILE' :'logs/images.log',
       # 'LOG_LEVEL':'INFO',
       'DEPTH_LIMIT': 5,
       'ROBOTSTXT_OBEY': False,
       'DOWNLOAD_DELAY' : 5,
       'COOKIES_ENABLED' : True
        }

    def start_requests(self):
        logging.log(logging.INFO,"Login: " )
        return [scrapy.FormRequest("http://www.wow-trend.com/Join/login",
                                    formdata={'acount': '15197081015', 'password': 'li123456'},
                                   callback=self.after_login)]
               
    def check_login_response(self,response):
        """ Check the response returned by login request to see if we are logged in """
        cookies=response.headers.getlist('Set-Cookie')
        if any("czo1OiI1MjA3MiI" in str(s) for s in cookies):
            logging.log(logging.INFO, 'GOOD LOGIN... ')
            return True
        else:
            logging.log(logging.INFO, 'BAD LOGIN... ')
            print ('BAD LOGIN... ')
            raise CloseSpider('BAD LOGIN')
            # return False

    def after_login(self,response):
        url="http://www.wow-trend.com/index/index/gender/2.shtml"
        return [scrapy.Request(url=url, callback=self.parse)]
        # return [scrapy.Request(url="http://www.wow-trend.com/index/index/gender/2.shtml", callback=self.parse)]


    def login(self):
        logging.log(logging.INFO,"Login: " )
        return [scrapy.FormRequest("http://www.wow-trend.com/Join/login",
                                    formdata={'acount': '15197081015', 'password': 'li123456'},
                                   callback=self.after_login)]

    def parse(self, response):
        #if response.headers['Content-Type'].startswith(b'application/pdf'):
        self.state['items_count'] = self.state.get('items_count', 0) + 1
        print (self.state)

        # DEBUG TOOLS
        # open_in_browser(response)
        # Inspect Response
        # inspect_response(response, self)

        # YIELD IMAGES
        if self.check_login_response(response):
            # taking original data
            imagesurl=response.css("a::attr(data-original)").extract()
            for elem in imagesurl:
                print (elem)
                if elem[:4] == "http":
                    yield {'image_urls': [elem]}
        else:
            return [scrapy.FormRequest("http://www.wow-trend.com/Join/login",
                                    formdata={'acount': '15197081015', 'password': 'li123456'})]
  

        # CRAWL NEXT PAGES
        pages = response.css ('a::attr(href)').getall()
        for page  in pages:
            next_page = response.urljoin(page)
            if next_page[:4] == "http" and next_page[-3:] != "jpg":
                self.logger.info('checking links %s', next_page)
                yield scrapy.Request(next_page,callback=self.parse)
