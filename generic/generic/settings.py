# -*- coding: utf-8 -*-
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'generic'

SPIDER_MODULES = ['generic.spiders']
NEWSPIDER_MODULE = 'generic.spiders'

# JOBDIR="crawl/jobs"
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 3

# automatically throttling crawling speed https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED= True
AUTOTHROTTLE_START_DELAY= 3
AUTOTHROTTLE_MAX_DELAY= 60
CONCURRENT_REQUESTS_PER_DOMAIN= 5

DEFAULT_REQUEST_HEADERS = {
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
'Accept': '*/*',
'Accept-Language': 'zh-CN,en;q=0.8,es;q=0.5,en-US;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'X-Requested-With': 'XMLHttpRequest',
'DNT': 1,
'Connection': 'keep-alive',
}


LOG_FILE="logs/scrapy.log"
# LOG_LEVEL="DEBUG"
LOG_LEVEL="ERROR"

CONCURRENT_REQUESTS_PER_DOMAIN = 1
RETRY_TIMES = 2

# Enable Images pipeline
# necessary for image pipeline
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
IMAGES_STORE='./images'
IMAGES_EXPIRES = 90
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}
IMAGES_MIN_HEIGHT = 200
IMAGES_MIN_WIDTH = 200

COOKIES_ENABLED =True
COOKIES_DEBUG= True

# PROXY
PROXY = 'http://127.0.0.1:33485'

# https://docs.scrapy.org/en/latest/topics/extensions.html

EXTENSIONS = {
    'scrapy.extensions.closespider.CloseSpider': 500
}



# export proxy


# SPLASH_URL = 'http://localhost:8050'
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy_splash.SplashCookiesMiddleware': 723,
#     'scrapy_splash.SplashMiddleware': 725,
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
# }
# SPIDER_MIDDLEWARES = {
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
# }
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'


