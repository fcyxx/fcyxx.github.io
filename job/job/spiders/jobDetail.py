# -*- coding: utf-8 -*-
import scrapy
import time
import json
from selenium import webdriver
from scrapy.selector import Selector
from job.items import JobItem
from scrapy.selector import Selector
from scrapy.http import Request


class JobdetailSpider(scrapy.Spider):
    name = 'jobDetail'
    # allowed_domains = ['http://www.highpin.cn/zhiwei/']
    # start_urls = ['http://www.highpin.cn/zhiwei/']
    headers = {
    'Host': 'data.highpin.cn',
    'Referer': 'http://www.highpin.cn/zhiwei/?Q%EF%BC%9APYTHON',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    def start_requests(self):
        # for i in range(1,11):
        url = 'http://data.highpin.cn/api/JobSearch/Search'
        for i in range(1,151):
            yield scrapy.FormRequest(
                url = url,
                formdata = {
                    'Q':'python开发工程师',
                    'pageIndex': '%s' %(i),
                    'pageSize': '20',
                    'ReferrerType': '',
                    'qTitle':' 1',
                    'JobLocation':'', 
                    'CompanyIndustry':'', 
                    'JobType': '',
                    'AnnualSalaryMin': '-1',
                    'AnnualSalaryMax': '-1',
                    'CompanyType': '',
                    'ReleaseDate':''
                },
                callback = self.parse,
                dont_filter = True
            )

    def parse(self, response):
        print("00000000000000000000")
        rawData = response.text
        data = json.loads(rawData)
        data = data['body']['JobList']
        URL = 'http://www.highpin.cn/job/h'
        end = '.html'
        for i in range(len(data)):
            detailID = data[i]['JobID']
            fullUrl = URL + str(detailID) + end
            yield Request(fullUrl,callback=self.detailParse,dont_filter = True)
    def detailParse(self,response):
        print('解析界面，获取想要的数据.......')
        jobName = response.xpath('//*[@id="main"]/div[1]/div[1]/div[2]/div/h1/span[1]/text()').extract_first()
        companyName = response.xpath('//*[@id="main"]/div[1]/div[2]/div[3]/ul/li[1]/@title').extract_first()
        baseInfo = response.xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/ul[1]/li/@title').extract()
        yealAnn = response.xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[2]/ul/li/span[2]/a/text()').extract()
        relTime = response.xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/ul[1]/li[4]/span[2]/text()').extract()
        jobDetail = response.xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[3]/div/div/div/p/text()').extract()
        comDetail = response.xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[5]/p/text()').extract_first()
        addr = response.xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/ul[1]/li[3]/a/text()').extract_first()
        item = JobItem()
        item['jobName'] = jobName
        item['companyName'] = companyName
        item['relTime'] = relTime
        item['baseInfo'] = baseInfo
        item['yealAnn'] = yealAnn
        item['jobDetail'] = jobDetail
        item['comDetail'] = comDetail
        yield item
        
