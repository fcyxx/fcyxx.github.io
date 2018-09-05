# -*- coding: utf-8 -*-
import scrapy
import time
from selenium import webdriver
from scrapy.selector import Selector
from job.items import JobItem
from scrapy.selector import Selector
from scrapy.http import Request

class DetailSpider(scrapy.Spider):
    name = 'detail'
    allowed_domains = ['www.highpin.cn']
    start_urls = ['http://www.highpin.cn/zhiwei/']

    def parse(self, response):
        url = response.url
        driver = webdriver.PhantomJS()
        driver.get(url)
        html = driver.page_source
        with open('ccc.html','w') as f:
           f.write(html)
        
