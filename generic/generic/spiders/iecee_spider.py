import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import tldextract

class QuotesSpider(scrapy.Spider):
    name = "iecee"
    domain=""
    allowed_domains = ['etsystems.com']
   # start_urls = ['http://www.etsystems.com/']
    custom_settings = {
#   'LOG_FILE' :'logs/quotes.log',
#   'LOG_LEVEL':'DEBUG',
   'DEPTH_LIMIT': 1,
   'ROBOTSTXT_OBEY': False
    }
    def __init__(self, url='', *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]
        a=tldextract.extract(url)
        # domain with or without subdomain
        self.domain=".".join([x for x in  a  if x is not ''])
        self.allowed_domains = [self.domain]

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'result/'+self.domain+'-ey-%s.html' % page
        name = self.domain+'/%s.html' % page
        with open(filename, 'wb') as f:
            yield {
                'page': name,
                'url': response.css('.bt-www::text').getall()
            }
            #f.write(response.body)
            #f.write(response.body)
        self.log('Saved file %s' % filename)
        pages = response.css ('a::attr(href)').getall()
        for page  in pages:
            next_page = response.urljoin(page)
            yield scrapy.Request(next_page, callback=self.parse)
