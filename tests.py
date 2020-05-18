#-*- coding:utf-8 -*-
from scrapy_script import Job, Processor
from crawler.crawler.spiders.ccidcom import CcidcomSpider

job = Job(CcidcomSpider)
processor = Processor(settings=None, get_data=False)
processor.run([job])
print(processor.data())