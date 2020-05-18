# -*- coding:utf-8 -*-
from scrapy_script import Job, Processor
from crawler.crawler.spiders.ccidcom import CcidcomSpider
import json
job = Job(CcidcomSpider)
processor = Processor(settings=None, item_scraped=True)
processor.run([job])
print(json.dumps(processor.data(), indent=4, ensure_ascii=False))
