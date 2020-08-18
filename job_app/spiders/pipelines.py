from job_app.items import SearchedItem
# Django model imports
from job_app.models import SearchedLinks

class SearchPipeline(object):
    def process_item(self, item, spider):
        # the cleaning magic starts!
  
        # finish!
        item.save()
        return item