#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scrapy
import time
import pandas as pd
from scrapy.crawler import CrawlerProcess
import numpy as np


# In[2]:


xml = 'https://www.coursera.org/sitemap~www~courses.xml'
links=[]
names=[]
ratings=[]
insts=[]
subjects=[]
#subjects_1=[]
#subjects_2=[] REVISIT
univs=[]
levels=[]
## times=[] REVISIT
langs=[]
subs=[]
sylls=[]


# In[3]:


class Course_Scrape(scrapy.Spider):
    name='Course_scraper'
    def start_requests(self):
        #print(xml)
        yield scrapy.Request(url=xml,callback=self.get_links)
        
    def get_links(self,response):
        data = response.xpath('//text()').extract()
        #data2=response.xpath('//url/text()').extract()
        #print(data2)
        for i in data:
            if len(i)>10:
                links.append(i)
    
        for link in links:
            yield response.follow(url=link, callback= self.get_data)
    
    def get_data(self,response):
        name = response.xpath('//h1[@class="banner-title banner-title-without--subtitle m-b-0"]//text()').extract()
        names.append(name)
        
        rating= response.xpath('//span[@class="_16ni8zai m-b-0 rating-text number-rating number-rating-expertise"]//text()').extract()
        ratings.append(rating)
        
        inst = response.xpath('//div[@class="_1qfi0x77"]/span//text()').extract()
        insts.append(inst)
        
        sub= response.xpath('//div[@class="_1ruggxy"]//text()').extract()
        subjects.append(sub)
        
        univ= response.xpath('//h3[@class="headline-4-text bold rc-Partner__title"]//text()').extract()
        univs.append(univ)
        
        level= response.xpath('//div[@class="_16ni8zai m-b-0 m-t-1s"]//text()').extract()
        levels.append(level)
    
        #time= response.xpath('//div[@class="_16ni8zai m-b-0 m-t-1s"]//text()')
        
        lang= response.xpath('//div[@class="_16ni8zai m-b-0"]//text()').extract()
        langs.append(lang)
        
        sub= response.xpath('//div[@class="_16ni8zai m-b-0"]/span//text()').extract()
        subs.append(sub)
        
        syll = response.xpath('//div[@class="Syllabus"]//text()').extract()
        sylls.append(syll)


# In[4]:


process= CrawlerProcess()
process.crawl(Course_Scrape)
process.start()


# In[ ]:





# In[ ]:




