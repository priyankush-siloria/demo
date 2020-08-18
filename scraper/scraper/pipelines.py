# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class ScraperPipeline:
#     def process_item(self, item, spider):
#         return item

from job_app.models import SearchedLinks

class SearchPipeline(object):
    def process_item(self, item, spider):
        # the cleaning magic starts!
  
        # finish!
        item.save()
        return item