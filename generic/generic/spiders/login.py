import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import tldextract
from scrapy_splash import SplashRequest



class LoginSp(scrapy.Spider):
	name = "loginsp"
	domain=""
	allowed_domains = ['wow-trend.com']
	start_urls = ['http://www.wow-trend.com/Join/login']
	custom_settings = {
	#   'LOG_FILE' :'logs/quotes.log',
	#   'LOG_LEVEL':'DEBUG',
	'DEPTH_LIMIT': 1,
	'ROBOTSTXT_OBEY': False
	}
	def start_requests(self):
		SplashRequest("http://www.wow-trend.com/Join/login", self.loginurl,args={'wait': 0.5})
		# scrapy.Request("http://www.wow-trend.com/Join/login", callback= self.parse_login)
		return [scrapy.FormRequest("http://www.wow-trend.com/Join/login",
	    							formdata={'acount': '15197081015', 'password': 'li123456'},
	                               callback=self.logged_in)]

	def loginurl(self,response):
		print("status login url")
		print (response.css(".login-status"))

	def logged_in(self,response):
		print("status")
		print (response.css(".login-status"))

	def parse(self,response):
		print ("result")
		print(reponse.css("a.head-login-btn"))

