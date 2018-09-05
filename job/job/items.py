# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = scrapy.Field()
    companyName = scrapy.Field()
    baseInfo = scrapy.Field()
    relTime = scrapy.Field()
    yealAnn = scrapy.Field()
    jobDetail = scrapy.Field()
    comDetail = scrapy.Field()
    
