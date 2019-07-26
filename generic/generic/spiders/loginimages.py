# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
# This spider download pdf in a determine domain

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


from scrapy.utils.response import open_in_browser

from scrapy.http import FormRequest
from scrapy.spiders.init import InitSpider

import sqlite3



import json
import base64
import scrapy
from scrapy_splash import SplashRequest

DATAPATH="/home/agalan/Downloads/crawler"
DOMAINS=["wow-trend.com"]
URLS=["https://www.wgsn.com/content/personalized/reports?content_types=14&markets=57&seasons=2431"]
URLS=["http://www.wow-trend.com/retail/index/season/273161/gender/2.shtml"]




# Variables
# start_url 
# domain

class ImagesSpider(CrawlSpider):
    name = 'loginimages'
    allowed_domains = DOMAINS
    start_urls = URLS
    custom_settings = {
      'LOG_FILE' :'logs/images.log',
       # 'LOG_LEVEL':'INFO',
       'DEPTH_LIMIT': 1,
       'ROBOTSTXT_OBEY': False,
       'DOWNLOAD_DELAY' : 3
       # 'COOKIES_ENABLED' : False
        }
    splash_args = {
            'html': 1,
            'png': 1,
            'width': 600,
            'render_all': 1,
        }
    

    def start_requests(self):
        splash_args = {
            'html': 1,
            'png': 1,
            'width': 600,
            'render_all': 1,
            'wait': 0.5
        }
        self.state['items_count'] = self.state.get('items_count', 0) + 1
        print (self.state)
        for url in self.start_urls:
           yield SplashRequest(url, self.parse, args={'wait': 1})
           # yield SplashRequest(url, self.parse, 
                            # args=splash_args)
    


    def parse(self, response):
        #if response.headers['Content-Type'].startswith(b'application/pdf'):

        open_in_browser(response)
        # print(response.url)

        # full decoded JSON data is available as response.data:
        # png_bytes = base64.b64decode(response.data['png'])
        # f = open('/tmp/output.png', 'wb')
        # f.write(png_bytes)
        # print ("begin")
        # f.close()
        # return True

        print(response.url)
        pages = response.css ('a::attr(href)').getall()
        for page  in pages:
            next_page = response.urljoin(page)
            self.logger.info('checking links %s', next_page)
            # cookie=self.get_chrome_cookies()
            # print(cookie)
        #     yield scrapy.Request(next_page, callback=self.parse)


    # get cookies from chrome and return scrapy format    
    def get_chrome_cookies(self):
        conn = sqlite3.connect('/home/agalan/.config/chromium/Default/Cookies')
        # query = 'select * from cookies where host_key="wwww.wgsn.com";'
        query = 'select * from cookies where host_key="www.wow-trend.com";'
        # return [{"name": r[0], "value": r[1], "path": r[2]} for r in conn.execute(query)]
        # return [{"name": r[2], "value": r[0], "path": r[4]} for r in conn.execute(query)]
        return [{ r[2] : r[0]} for r in conn.execute(query)]
        # return [{r[0],  r[2],r[4]} for r in conn.execute(query)]




    # def parse(self, response):
    #     #if response.headers['Content-Type'].startswith(b'application/pdf'):
    #     self.state['items_count'] = self.state.get('items_count', 0) + 1
    #     print (self.state)
    #     open_in_browser(response)

        # print(response.url)
        # # self.parse_items_background_image(response)

        # rawurls = response.css('.media::attr(style)').getall()
        # imagesurl = [ re.search('(https|http).*(jpg|png)',x).group(0) for x in rawurls if re.search('(https|http).*(jpg|png)',x)]
        # for elem in imagesurl:
        #   print ("yield image " + elem)
        #   yield {'image_urls': [elem]}
  
        # pages = response.css ('a::attr(href)').getall()
        # for page  in pages:
        #     next_page = response.urljoin(page)
        #     self.logger.info('checking links %s', next_page)
        #     cookie={"fr":"0HnbcbGCcSFtgmQPP..BdBv7k..F04.1.0.BdOQI6.", "datr":"OGQMXYGO0j5wwEH4ZgCC33Px","_fbp":"fb.1.1561093183914.1172904390"}
        #     yield scrapy.Request(next_page, cookies=cookie, callback=self.parse)




    # def init_request(self):
    #     return scrapy.Request(
    #         url=self.login_url,
    #         callback=self.login,
    #     )


    # def login(self, response):
    #     yield scrapy.FormRequest.from_response(
    #         response=response,
    #         formid='login-form',
    #         formdata={
    #             'username': 'qkvhwprq@sharklasers.com',
    #             'password': 'gorosucks',
    #             'remember':1
    #         },
    #         method="POST",
    #         callback=self.initialized,
    #     )